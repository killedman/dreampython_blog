#! /usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Text, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "mysql+pymysql://username:passwd@localhost/dreampython_blog"



db = create_engine(db_string)
base = declarative_base()


class Post(base):
    __tablename__ = 'blog_post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    content = Column(Text)
    post_timestamp = Column(DateTime, default=func.now())
    modifyed_timestamp = Column(DateTime, default=func.now())
    author = Column(String(200), nullable=False)
    mail = Column(String(200))


#class User(base):
#    __tablename__ = 'users'
    
#    id = Column(Integer, primary_key=True, autoincrement=True)
#    user_name = Column(String(200))
#    mail = Column(String(200))

def main():
    Session = sessionmaker(db)
    session = Session()

    base.metadata.create_all(db)

    # create
    post_1 = Post(title='title_1', content='content_1', author='author_1')
    session.add(post_1)
    session.commit()

    # Read
    posts = session.query(Post)
    for post in posts:
        print(post.title, post.content, post.post_timestamp, post.author, post.mail)

# Update
#post_1.title = 'new_title_1'
#session.commit()

# Delete
#session.delete(post_1)
#session.commit()


if __name__ == "__main__":
    main()
