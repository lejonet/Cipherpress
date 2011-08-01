#!/usr/bin/env python
#-*- coding:utf-8 -*-
from elixir import *

metadata.bind = "sqlite:///posts.sdb"
metadata.bind.echo = False

class DB_Posts(Entity):
    """Model for the post table in the database"""
    title = Field(Unicode(64), required=True)
    body = Field(UnicodeText, required=True)
    
    def __repr__(self):
        return u'<Post title: "%s" post: "%s" types: %s %s>' % (self.title,self.body,type(self.title),type(self.body))
