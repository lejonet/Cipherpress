#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form
from model import *

urls = ('/', 'submit')
render = web.template.render('templates/')
submit_form = form.Form(form.Textbox('title', form.notnull), form.Textarea('body', form.notnull), form.Button('Submit!'))

if __name__ == __main__:
    web.internalerror = web.debugerror
    web_frontend.run()

class submit:
	"""Submit function that handles the submit form"""
 
	def GET(self):
		s = submit_form()
		return render.submit(s)
	def POST(self):
		s = submit_form()
		if s.validates():
			safe_title = s['title'].value.replace('<', '&lt;').replace('>', '&gt;')
			safe_body  = s['body'].value.replace('<', '&lt;').replace('>', '&gt;')
			setup_all()
			DB_Posts(title=safe_title,body=safe_body)
#			DB_Posts(title=s['title'].value,body=s['body'].value)
			session.commit()
			return "Success!\nPOST title: %s %s POST body: %s %s" % (s['title'].value,type(s['title'].value),s['body'].value,type(s['body'].value))
		else:
			return render.submit(s)
			
