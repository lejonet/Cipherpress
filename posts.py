#!/usr/bin/env python
#-*- coding:utf-8 -*-
import markdown

class Post:
	"""Class to make the posts into objects"""
	def __init__(self, path_to_post):
		self._path_to_post = path_to_post
		self._f = open(self._path_to_post, 'r')
		self.text = self._f.read()
			
	def markdown(self):
		return self.text
		
	def html(self):
		self.html = markdown.markdown(self.text)
		return self.html
