#!/usr/bin/env python
#-*- coding:utf-8 -*-
from markdown import *
from model import *

class Post_Object:
	"""Class to make the posts into objects"""
	def __init__(self):
		self._posts = Posts.query.all()
		self._titles = []
		self._bodies = []
		for post in self._posts:
			self._titles.append(post.title)
			self._bodies.append(post.body)
#		print self._titles, type(self._titles)
#		print self._bodies, type(self._bodies)
#		print self._posts, type(self._posts)
			
	def markdown_titles(self):
		return self._titles
		
	def html_titles(self):
		self._markdown_titles = []
		for title in self._titles:
			self._markdown_titles.append(markdown(title))
		return self._markdown_titles

	def markdown_bodies(self):
		return self._bodies

	def html_bodies(self):
		self._markdown_bodies = []
		for body in self._bodies:
			self._markdown_bodies.append(markdown(body))
		return self._markdown_bodies
