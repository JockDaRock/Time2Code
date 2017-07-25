from flask import Flask, request, render_template, Markup
import requests
from urllib.parse import urlparse
import markdown
import os
import subprocess


app = Flask(__name__)

p1 = subprocess.Popen(["/sbin/ip", "route"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["awk", "/default/ { print $3 }"], stdin=p1.stdout, stdout=subprocess.PIPE)
faas = (p2.stdout).read().decode("utf-8").replace("\n", "")


@app.route('/')
def time2code():
    url = "https://raw.githubusercontent.com/JockDaRock/Time2Code/master/Sample.md"
    r = requests.get(url)
    mark = r.text

    content = Markup(markdown.markdown(mark))
    return render_template('index-panel.html', markd=content)


@app.route('/code/python', methods=['POST'])
def codepy():
    if request.method == 'POST':
        data = request.data
        hosturl = urlparse(request.url)
        host = hosturl.hostname
        # url = "http://%s:8080/function/time2py" % host
        url = "http://%s:8080/function/python" % faas
        # print(url)
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
        url = "http://%s:8080/function/golang" % faas
        # print(url)
        headers = {"Content-Type": "text/plain"}

        code_exec = requests.post(url, data=data, headers=headers)

        resp = code_exec.text

        # print(repr(resp))

        return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
