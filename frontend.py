#!/usr/bin/env python
#-*- coding:utf-8 -*-
import web
import posts

urls = ('/(.*)', 'routing')
render = web.template.render('templates/')
web_frontend = web.application(urls, globals())

if __name__ == "__main__":
	web_frontend.run()

class routing:
	"""The function that routes what goes where"""
	def GET(self, name):
		if name == 'posts':
			post = posts.Post('/home/test/source/lulz/markdown/test.markdown')
			html_post = post.html()
			return html_post
		else:
			return render.index()
