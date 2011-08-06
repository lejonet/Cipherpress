#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Post Object class - A class to put the posts into a mutable python object
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

from markdown import *
from model import *

class Post_Object:
	"""Class to fetch the posts from db and make them into objects, htmlized or raw"""
	def __init__(self, pid = False):
		self._pid = pid
		setup_all()
		if (pid):
			self._db_post = DB_Posts.query.filter_by(id=pid).one()
			self._title   = self._db_post.title
			self._body    = self._db_post.body
			self._pid     = self._db_post.id
		else:
			self._db_posts = DB_Posts.query.all()
			self._pids   = []
			self._titles = []
			self._bodies = []
			for row in self._db_posts:
				self._pids.append(row.id) 
				self._titles.append(row.title)
				self._bodies.append(row.body)
			
	def raw_titles(self):
		if (self._pid):
			return self._title
		else:
			return self._titles
		
	def html_titles(self):
		if (self._pid):
			return markdown(self._title)
		else:
			self._html_titles = []
			for title in self._titles:
				self._html_titles.append(markdown(title))
			return self._html_titles

	def raw_bodies(self):
		if (self._pid):
			return self._body
		else:
			return self._bodies

	def html_bodies(self):
		if (self._pid):
			return markdown(self._body)
		else:
			self._html_bodies = []
			for body in self._bodies:
				self._html_bodies.append(markdown(body))
			return self._html_bodies
		
	def raw_list(self):
		if (self._pid):
			self._list = [ self._pid, self._title, self._body ]
			return self._list
		else:
			return self._db_posts

	def html_list(self):
		if (self._pid):
			self._list = [ self._pid, markdown(self._title), markdown(self._body) ]
			return self._list
		else:
			return None

