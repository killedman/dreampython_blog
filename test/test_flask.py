#! /usr/bin/env python
# -*- coding:utf8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Text, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from test_mysql import db_string, Post

app = Flask(__name__)

db = create_engine(db_string)
base = declarative_base()

Session = sessionmaker(db)
session = Session()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        post = Post(title=request.form.get("title"), 
                content=request.form.get("content"), 
                author=request.form.get("author"))
        session.add(post)
        session.commit()
        #print(request.form)
    posts = session.query(Post) 
    return render_template("home.html", posts=posts)

    
@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    post = session.query(Post).filter_by(title=oldtitle).first()
    post.title = newtitle
    session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    post = session.query(Post).filter_by(title=title).first()
    session.delete(post)
    session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
