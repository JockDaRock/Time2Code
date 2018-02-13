#!/usr/bin/python
from wsgiref.handlers import CGIHandler
import os
from ide_server import app

query_params = os.getenv("Http_Query", default="")
whole_path = os.getenv("Http_Path", default="/ip")
split_path = whole_path.split('/')
if len(split_path) > 3:
    route_path = '/' + '/'.join(split_path[3:])
else:
    route_path = "/"
http_method = os.getenv("Http_Method", default="GET")


class ProxyFix(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SERVER_NAME'] = "127.0.0.1"
        environ['SERVER_PORT'] = "8080"
        environ['REQUEST_METHOD'] = http_method
        environ['SCRIPT_NAME'] = ""
        environ['PATH_INFO'] = route_path
        environ['QUERY_STRING'] = query_params
        environ['SERVER_PROTOCOL'] = "HTTP/1.1"
        environ['Http_X_Forwarded_For'] = os.getenv("Http_X_Forwarded_For", "127.0.0.1")
        return self.app(environ, start_response)


class HeaderRewriterFix(object):

    def __init__(self, app, remove_headers=None, add_headers=None):
        self.app = app
        self.remove_headers = set(x.lower() for x in (remove_headers or ()))
        self.add_headers = list(add_headers or ())

    def __call__(self, environ, start_response):
        def rewriting_start_response(status, headers, exc_info=None):
            new_headers = []
            return start_response(status, new_headers, exc_info)
        return self.app(environ, rewriting_start_response)

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.wsgi_app = HeaderRewriterFix(app.wsgi_app)
    CGIHandler().run(app)
