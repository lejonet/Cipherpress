#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Database table model - A database model to automatically generate the database table/s needed
# Copyright (C) 2011 Daniel Kuehn <daniel@kuehn.se>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

from elixir import *

metadata.bind = "sqlite:///posts.sdb"
metadata.bind.echo = False

class DB_Posts(Entity):
    """Model for the post table in the database"""
    title = Field(Unicode(64), required=True)
    body = Field(UnicodeText, required=True)
    
    def __repr__(self):
        return u'<Post title: "%s" post: "%s" types: %s %s>' % (self.title,self.body,type(self.title),type(self.body))
