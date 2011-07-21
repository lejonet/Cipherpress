#!/usr/bin/env python
#-*- coding:utf-8 -*-
from elixir import *

metadata.bind = "sqlite://posts.sdb"
metadata.bind.echo = True

class Post(Entity):
    """Model for the post table in the database"""
    post = Field(Text, required=True)

    def __repr__(self):
        return '<Post "%s">' % (self.post)
