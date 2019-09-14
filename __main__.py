#! /usr/bin/evn python
# -*- coding: utf8 -*-

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello, {escape(name)}!'


if __name__ == "__main__":
    app.run()
