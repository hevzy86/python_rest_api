import tornado.ioloop
import tornado.web
from employees.handlers.powhandler import PowHandler
from employees.lib.application import app, route

@app.make_routes()
class HelloHandler(PowHandler):
    @route(r'/hello', dispatch=["get"])
    def hello(self):
        self.write("Hello world!")