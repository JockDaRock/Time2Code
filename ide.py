from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/time2code')
@app.route('/time2code/<name>')
def time2code(name='base'):
    return render_template('base_test.html', name=name)


@app.route('/code/py', methods=['POST'])
def time2py():
    if request.method == 'POST':
        data = request.data
        url = "http://pwd10-0-61-3-8080.host1.labs.play-with-docker.com/function/time2code"
        headers = {"Content-Type": "text/plain"}

        code_exec = requests.post(url, data=data, headers=headers)

        resp = code_exec.text

        print(resp)

        return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8181)

