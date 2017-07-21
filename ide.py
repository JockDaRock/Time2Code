from flask import Flask, request, render_template, Markup
import requests
from urllib.parse import urlparse
import markdown
from wsgiref.handlers import CGIHandler

app = Flask(__name__)


@app.route('/')
def time2code():
    url = "https://raw.githubusercontent.com/JockDaRock/Time2Code/master/Sample.md"
    r = requests.get(url)
    mark = r.text

    content = Markup(markdown.markdown(mark))
    return render_template('index-panel.html', markd=content)


class ProxyFix(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['SERVER_NAME'] = "localhost"
        environ['SERVER_PORT'] = "8080"
        environ['REQUEST_METHOD'] = "GET"
        environ['SCRIPT_NAME'] = ""
        environ['PATH_INFO'] = "/"
        environ['QUERY_STRING'] = ""
        environ['SERVER_PROTOCOL'] = "HTTP/1.1"
        return self.app(environ, start_response)

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CGIHandler().run(app)
