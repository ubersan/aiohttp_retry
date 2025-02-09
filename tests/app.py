from aiohttp import web


class App:
    def __init__(self):
        self.counter = 0

        app = web.Application()
        app.router.add_get('/ping', self.ping_handler)
        app.router.add_get('/internal_error', self.internal_error_handler)
        app.router.add_get('/not_found_error', self.not_found_error_handler)
        app.router.add_get('/sometimes_error', self.sometimes_error)

        app.router.add_options('/options_handler', self.ping_handler)
        app.router.add_head('/head_handler', self.ping_handler)
        app.router.add_post('/post_handler', self.ping_handler)
        app.router.add_put('/put_handler', self.ping_handler)
        app.router.add_patch('/patch_handler', self.ping_handler)
        app.router.add_delete('/delete_handler', self.ping_handler)

        self._web_app = app

    async def ping_handler(self, _: web.Request) -> web.Response:
        self.counter += 1
        return web.Response(text='Ok!', status=200)

    async def internal_error_handler(self, _: web.Request) -> web.Response:
        self.counter += 1
        raise web.HTTPInternalServerError()

    async def not_found_error_handler(self, _: web.Request) -> web.Response:
        self.counter += 1
        raise web.HTTPNotFound()

    async def sometimes_error(self, _: web.Request) -> web.Response:
        self.counter += 1
        if self.counter == 3:
            return web.Response(text='Ok!', status=200)

        raise web.HTTPInternalServerError()

    @property
    def web_app(self) -> web.Application:
        return self._web_app
