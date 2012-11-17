#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
import xml.etree.ElementTree as etree

class MainHandler(webapp.RequestHandler):
	def get(self, group1):
		if group1 == '':
			self.response.out.write('usage;  http://twid2web.appspot.com/[twitter user-id]<br />')
			self.response.out.write('ex)  <a href="http://twid2web.appspot.com/92577084">http://twid2web.appspot.com/92577084</a>')
		else:
#			self.response.out.write(group1)
			url='http://api.twitter.com/users/show/'+group1
			xml=urlfetch.fetch(url).content
			et=etree.fromstring(xml)
			screen_name = et.findtext('.//screen_name')
			self.redirect('http://twitter.com/' + screen_name)


def main():
    application = webapp.WSGIApplication([('/(.*)', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
