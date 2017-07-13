"""import time
from flask import Flask, request"""
import sys
import os
from io import StringIO
import contextlib


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf


if(__name__ == "__main__"):
    st = get_stdin()
    # print(st)
    with stdoutIO() as s:
        exec(st)
    print(s.getvalue())
