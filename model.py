#!/usr/bin/env python
#-*- coding:utf-8 -*-
from elixir import *

metadata.bind = "sqlite:///posts.sdb"
metadata.bind.echo = True

class Post(Entity):
    """Model for the post table in the database"""
    title = Field(Unicode(64), required=True)
    body = Field(UnicodeText, required=True)
    
    def __repr__(self):
        return '<Post title: "%s" post: "%s">' % (self.title,self.post)
