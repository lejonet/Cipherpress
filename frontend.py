 #!/usr/bin/env python
#-*- coding:utf-8 -*-
import web
from posts_object import *

urls = ('/', 'index'
	'/post/(.*)', 'posts')
render = web.template.render('templates/')
web_frontend = web.application(urls, globals())

if __name__ == "__main__":
	web_frontend.run()

class index:
	"""The function that routes what goes where"""
	def GET(self):
		posts_obj = Post_Object()
		return render.index(posts_obj.raw_dict())

class posts:
	"""The function to display posts"""

	def GET(self, pid):
		post_obj = Post_Object(pid)
		return render.post(post_obj.raw_list())
		
