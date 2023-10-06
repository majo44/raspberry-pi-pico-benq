let version;

const checkReloadNeeded = (newVersion) => {
    if (version) {
        if (newVersion !== version) {
            location.reload();
        }
    }
    version = newVersion
}


const connect = () => {
    const ws = new WebSocket(
        `ws://${location.host}/ping`
    );

    ws.onopen = function(e) {
        console.log('[lr] connected')
        ws.send('');
    };
    ws.onmessage = function(event) {
        checkReloadNeeded(event.data);
    };
    ws.onclose = function(event) {
        console.log('[lr] connection died');
        setTimeout(function() {
            connect();
        }, 100);
    };
    ws.onerror = function(err) {
        console.error('[lr] socket encountered error: ', err.message);
        ws.close();
    };
}

connect();