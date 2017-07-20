from flask import Flask, request, render_template
import requests
from wsgiref.handlers import CGIHandler

app = Flask(__name__)


@app.route('/')
@app.route('/<code_exec>')
def time2py():
    code_exec = request.args.get('time2code')
    return render_template('base_test.html', code_exec="time2py")


@app.route('/time2go')
def time2go():
    return render_template('base_test.html', code_exec="time2go")


@app.route('/code/py', methods=['POST'])
def codepy():
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
        environ['QUERY_STRING'] = "time2code=time2go"
        environ['SERVER_PROTOCOL'] = "HTTP/1.1"
        return self.app(environ, start_response)

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CGIHandler().run(app)
