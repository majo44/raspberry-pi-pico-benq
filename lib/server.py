from random import randint
from config import web_port, verbose, live_reload
from microdot_asyncio import Microdot, send_file
from microdot_asyncio_websocket import with_websocket
from microdot_utemplate import render_template, init_templates
from rs import rs_send
from uasyncio import sleep_ms

init_templates('public')
version = randint(0, 99999)

def server_start(host="0.0.0.0", port=web_port):

    print("starting server", host, port, verbose)
    app = Microdot()
    
    @app.route('/public/<path:path>')
    async def static(request, path):
        if '..' in path:
            return 'Not found', 404
        return send_file('public/' + path) # , max_age=86400

    @app.post('/cmd')
    async def cmd(request):
        respones = []
        commands = request.json
        for item in commands:
            res = await rs_send(item)
            respones.append(res)
        return respones

    @app.route('/')
    async def hello(request):
        return render_template('index.html', lr = live_reload), {'Content-Type': 'text/html'}

    if live_reload:
        @app.route('/ping')
        @with_websocket
        async def ping(request, ws):
            while True:
                await sleep_ms(100)
                await ws.send(f'{version}')

    return app.start_server(host, port, verbose)

