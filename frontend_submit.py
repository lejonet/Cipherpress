#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cipherpress Submit Frontend - A simple submit frontend for Cipherpress
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
from model import *

def csrf_protected(f):
    def decorated(*args,**kwargs):
        inp = web.input()
        if not (inp.has_key('csrf_token') and inp.csrf_token==web_session.pop('csrf_token',None)):
            raise web.HTTPError("400 Bad request", {'content-type':'text/html'}, '"""Cross-site request forgery (CSRF) attempt (or stale browser form).<a href="/submit">Back to the form</a>."""')
        return f(*args,**kwargs)
    return decorated

def csrf_token():
    if not web_session.has_key('csrf_token'):
        from uuid import uuid4
        web_session.csrf_token=uuid4().hex
    return web_session.csrf_token

urls = ('/', 'submit')
render = web.template.render('templates/', globals={'csrf_token':csrf_token})
submit_form = form.Form(form.Textbox('title', form.notnull), form.Textarea('body', form.notnull), form.Button('Submit!'))
web_frontend = web.application(urls, globals())

if web.config.get('_session') is None:
    web_session = web.session.Session(web_frontend, web.session.DiskStore('sessions'), {'count': 0})
    web.config._session = web_session
else:
    web_session = web.config._session


if __name__ == "__main__":
    web.internalerror = web.debugerror
    web_frontend.run()

class submit:
	"""Submit function that handles the submit form"""
 
	def GET(self):
            print 'Session: ', web_session
            web_session.count += 1
            print 'Session.count: %s' % web_session.count
            s = submit_form()
            return render.submit(s)
        @csrf_protected
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
			
