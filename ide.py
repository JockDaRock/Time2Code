from flask import Flask, request, render_template
import requests

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

        print(resp)

        return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

