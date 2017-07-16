from flask import Flask, request, render_template
import requests
from wsgiref.handlers import CGIHandler

app = Flask(__name__)


@app.route('/time2code')
@app.route('/time2code/<name>')
def time2code(name='time2py'):
    return render_template('base_test.html', name=name)


@app.route('/code/py', methods=['POST'])
def time2py():
    if request.method == 'POST':
        data = request.data
        host = request.host
        url = "http://%s/function/time2py" % host
        headers = {"Content-Type": "text/plain"}

        code_exec = requests.post(url, data=data, headers=headers)

        resp = code_exec.text

        # print(resp)

        return resp


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
