#!/usr/bin/env python
#-*- coding:utf-8 -*-
from markdown import *
from model import *

class Post_Object:
	"""Class to make the posts into objects"""
	def __init__(self, pid = False):
		setup_all()
		if (pid):
			self._db_post = DB_Posts.query.filter_by(id=pid).one()
			self._title = self._db_post.title
			self._bodie = self._db_post.body
			self._pid   = self._db_post.id
		else:
			self._db_posts = DB_Posts.query.all()			
			self._titles = []
			self._bodies = []
			self._pids   = []
			for post in self._db_posts:
				self._pids.append(post.id)
				self._titles.append(post.title)
				self._bodies.append(post.body)
#		print self._titles, type(self._titles)
#		print self._bodies, type(self._bodies)
#		print self._posts, type(self._posts)
			
	def raw_titles(self):
		if (pid):
			return self._title
		else:
			return self._titles
		
	def html_titles(self):
		if (pid):
			return markdown(self._title)
		else:
			self._html_titles = []
			for title in self._titles:
				self._html_titles.append(markdown(title))
			return self._html_titles

	def raw_bodies(self):
		if (pid):
			return self._body
		else:
			return self._bodies

	def html_bodies(self):
		if (pid):
			return markdown(self._body)
		else:
			self._html_bodies = []
			for body in self._bodies:
				self._html_bodies.append(markdown(body))
			return self._html_bodies
