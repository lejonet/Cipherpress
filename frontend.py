#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Blog Frontend - A simple frontend for the blog platform, shows a list of posts, individual posts and enables submitting posts
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

import web
from web import form
from posts_object import *
from model import *

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
		s = submit_form()
		if s.validates():
			safe_title = s['title'].value.replace('<', '&lt;')
			safe_body  = s['body'].value.replace('<', '&lt;')
			setup_all()
			DB_Posts(title=safe_title,body=safe_body)
#			DB_Posts(title=s['title'].value,body=s['body'].value)
			session.commit()
			return "Success!\nPOST title: %s %s POST body: %s %s" % (s['title'].value,type(s['title'].value),s['body'].value,type(s['body'].value))
		else:
			return render.submit(s)
			

