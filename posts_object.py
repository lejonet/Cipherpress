#!/usr/bin/env python
#-*- coding:utf-8 -*-
from markdown import *
from model import *

class Post_Object:
	"""Class to make the posts into objects"""
	def __init__(self):
#		self._db_posts = Posts()
#		self._posts = self._db_posts.query.all()
		self._titles = []
		self._bodies = []
		setup_all()
		self._db_posts = DB_Posts.query.all()
		for post in self._db_posts:
			self._titles.append(post.title)
			self._bodies.append(post.body)
#		print self._titles, type(self._titles)
#		print self._bodies, type(self._bodies)
#		print self._posts, type(self._posts)
			
	def raw_titles(self):
		return self._titles
		
	def html_titles(self):
		self._html_titles = []
		for title in self._titles:
			self._html_titles.append(markdown(title))
		return self._html_titles

	def raw_bodies(self):
		return self._bodies

	def html_bodies(self):
		self._html_bodies = []
		for body in self._bodies:
			self._html_bodies.append(markdown(body))
		return self._html_bodies
