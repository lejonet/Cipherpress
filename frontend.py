#!/usr/bin/env python
#-*- coding:utf-8 -*-
import web
from web import form
from posts_object import *

urls = ('/', 'index',
	'/post/(.*)', 'posts',
	'/submit', 'submit')
render = web.template.render('templates/')
web_frontend = web.application(urls, globals())
submit_form = form.Form(form.Textbox('title', form.notnull), form.Textarea('body', form.notnull), form.Button('Submit!'))

if __name__ == "__main__":
	web.internalerror = web.debugerror
	web_frontend.run()

class index:
	"""Index function that shows the post list"""
	def GET(self):
		posts_obj = Post_Object()
		return render.index(posts_obj.raw_list())

class posts:
	"""The function to display posts"""

	def GET(self, pid):
		post_obj = Post_Object(pid)
		return render.post(post_obj.html_list())
	
class submit:
	"""Submit function that handles the submit form"""
 
	def GET(self):
		s = submit_form()
		return render.submit(s)
	def POST(self):
		pass
