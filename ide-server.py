from flask import Flask, request, render_template, Markup
import requests
from urllib.parse import urlparse
import markdown

app = Flask(__name__)


@app.route('/time2py')
def time2py():
    return render_template('base_test_server.html', code_exec="time2py")


@app.route('/time2go')
def time2go():
    return render_template('base_test_server.html', code_exec="time2go")


@app.route('/')
def time2code():
    url = "https://raw.githubusercontent.com/joyent/triton/master/README.md"
    r = requests.get(url)
    mark = r.text

    content = Markup(markdown.markdown(mark))
    return render_template('index.html', markd=content)


@app.route('/code/python', methods=['POST'])
def codepy():
    if request.method == 'POST':
        data = request.data
        hosturl = urlparse(request.url)
        host = hosturl.hostname
        # url = "http://%s:8080/function/time2py" % host
        url = "http://127.0.0.1:8080/function/time2py"
        print(url)
        headers = {"Content-Type": "text/plain"}

        code_exec = requests.post(url, data=data, headers=headers)

        resp = code_exec.text

        # print(resp)

        return resp


@app.route('/code/golang', methods=['POST'])
def codego():
    if request.method == 'POST':
        data = request.data
        hosturl = urlparse(request.url)
        host = hosturl.hostname
        # url = "http://%s:8080/function/time2py" % host
        url = "http://127.0.0.1:8080/function/time2go"
        print(url)
        headers = {"Content-Type": "text/plain"}

        code_exec = requests.post(url, data=data, headers=headers)

        resp = code_exec.text

        # print(resp)

        return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)
