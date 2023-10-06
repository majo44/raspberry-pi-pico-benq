if (window.LR) {
    import('./live-reload.js');
}
let lastTimeCheck;

/**
 * @type {Array<HTMLButtonElement>}
 */
const buttons = Array.from(document.querySelectorAll('button'));

/**
 * @type {HTMLButtonElement}
 */
const powerBtn = document.querySelector('button[data-command="pow"]');

const getCommandData = (btn) => {
    const command = btn.dataset['command'];
    const commandValue = btn.dataset['value'];
    const commandType = btn.dataset['commandType'];
    return {
        command,
        commandValue,
        commandType
    }
}

/**
 * @param {Array<string>} commands
 * @return {Promise<Array<string>>}
 */
const sendCommands = async (...commands) => {
    const response = await fetch('/cmd', {
        method: 'POST',
        body: JSON.stringify(commands),
        headers: {
            "Content-Type": "application/json",
        }
    });
    const res = await response.json();
    return res;
}

const checkStateOfButtons = async () => {
    lastTimeCheck = Date.now()
    document.body.classList.add('loading');
    buttons.forEach(btn => btn.disabled = true);
    const commands = buttons.reduce((requests, btn) => {
        const command = btn.dataset['command'];
        const commandType = btn.dataset['commandType'];
        if (commandType !== 'trigger' && commandType !== 'custom' && !requests.find(({command: c}) => c === command)) {
            return [
                ...requests,
                { command, commandType, request: `${command}=?` }
            ]
        }
        return requests
    }, []);
    const results = await sendCommands(...commands.map(({ request }) => request));
    results.forEach((value, index) => commands[index].result = value);
    buttons.forEach(btn => {
        const { command, commandType, commandValue } = getCommandData(btn);
        const value = commands.find(({command: c}) => c === command)?.result;
        if (value) {
            switch (commandType) {
                case 'onoff': {
                    if (value.endsWith('=on')) {
                        btn.classList.add('on');
                    } else if (value.endsWith('=off')) {
                        btn.classList.remove('on');
                    }
                    break;
                }
                case 'oneof': {
                    if (value.endsWith(commandValue)) {
                        btn.classList.add('on');
                        btn.disabled = false;
                    } else {
                        btn.classList.remove('on');
                        btn.disabled = false;
                    }
                    break;
                }
            }
        }
        btn.disabled = false;
    });

    document.body.classList.remove('loading');
}

const init = async () => {
    document.body.classList.add('loading');
    buttons.forEach(btn => btn.disabled = true);
    const [powStatus] = await sendCommands('pow=?');
    if (powStatus.endsWith('=on')){
        powerBtn.classList.add('on');
        await checkStateOfButtons();
    } else if (powStatus.endsWith('=off')){
        powerBtn.disabled = false;
        buttons.forEach(btn => btn.classList.remove('on'));
        document.body.classList.remove('loading');
    } else {
        setTimeout(init, 1000)
    }
}

buttons.forEach(btn => {
    btn.addEventListener('click', async () => {
        if (!btn.disabled) {
            document.body.classList.add('loading');
            buttons.forEach(b => b.disabled = true);
            const { command, commandType, commandValue } = getCommandData(btn);
            const isOn = btn.classList.contains('on');
            if (command === 'pow') {
                if (btn.classList.contains('on')) {
                    await sendCommands('pow=off');
                } else {
                    await sendCommands('pow=on');
                }
                setTimeout(init, 2000);
                return;
            }
            if (command === 'refresh') {
                await init();
                return;
            }
            if (commandType === 'trigger') {
                document.body.classList.add('loading');
                await sendCommands(commandValue ? `${command}=${commandValue}` : command);
                document.body.classList.remove('loading');
                buttons.forEach(b => b.disabled = false);
                return;
            }
            if (commandType === 'oneof') {
                document.body.classList.add('loading');
                await sendCommands(`${command}=${commandValue}`);
                await checkStateOfButtons();
                return;
            }
            if (commandType === 'onoff') {
                document.body.classList.add('loading');
                await sendCommands(`${command}=${isOn ? 'off' : 'on'}`);
                await checkStateOfButtons();
            }
        }
    });
})

window.onfocus = () => {
    if (Date.now() - lastTimeCheck > 20000) {
        init();
    }
}
init();