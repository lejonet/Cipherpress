#!/usr/bin/env python
#-*- coding:utf-8 -*-
from markdown import *
from model import *

class Post:
	"""Class to make the posts into objects"""
	def __init__(self):
		setup_all()
		self._posts = Posts.query.all()
		self._titles = []
		self._bodies = []
		for post in self._posts:
			self._titles.append(post.title)
			self._bodies.append(post.body)
		print self._titles, type(self._titles)
		print self._bodies, type(self._bodies)
		print self._posts, type(self._posts)
			
	def markdown_titles(self):
		return self._titles
		
	def html_titles(self):
		return markdown(title)

	def markdown_bodies(self):
		return self._bodies

	def html_bodies(self):
		return markdown(body)
