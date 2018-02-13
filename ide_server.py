from flask import Flask, request, render_template, Markup
import requests
from urllib.parse import urlparse
import markdown
import os
import subprocess
import socket


app = Flask(__name__)


@app.route('/')
def time2code():
    text = request.args.get('code')
    lang = request.args.get('lang')
    straight_text = request.args.get('straight_text')
    code_text = ""

    if text:
        r_text = requests.get(text + "?raw=true")
        code_text = r_text.text
    elif straight_text:
        code_text = straight_text
    else:
        code_text = ""

    if lang:
        code_lang = lang
    else:
        code_lang = "python3"

    return render_template('index.html', code_text=code_text, code_lang=code_lang)


@app.route('/tutorial')
def tutorial():
    text = request.args.get('code')
    lang = request.args.get('lang')
    straight_text = request.args.get('straight_text')
    get_tut = request.args.get('tut')
    code_text = ""
    tut_url = ""
    mark = ""

    if get_tut:
        tut_url = get_tut + "?raw=true"
        r_tut = requests.get(tut_url)
        mark = r_tut.text
    else:
        tut_url = "https://raw.githubusercontent.com/JockDaRock/Time2Code/master/Sample.md?raw=true"
        r_tut = requests.get(tut_url)
        mark = r_tut.text

    if text:
        r_text = requests.get(text + "?raw=true")
        code_text = r_text.text
    elif straight_text:
        code_text = straight_text

    if lang:
        code_lang = lang
    else:
        code_lang = "python3"

    content = Markup(markdown.markdown(mark, extensions=['pymdownx.github', 'pymdownx.highlight']))
    return render_template('index-tutorial.html', markdown=content, code_text=code_text, code_lang=code_lang)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)

