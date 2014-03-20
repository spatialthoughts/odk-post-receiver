"""Simple server that receives a POST request.

Copyright 2014 Ujaval Gandhi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
"""
import datetime
import json
import os
import jinja2
import webapp2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class PostMessage(ndb.Model):
  """NDB model to temporarily store the POST request."""
  content = ndb.StringProperty()
  timestamp = ndb.DateTimeProperty(auto_now_add=True)


class WipeData(webapp2.RequestHandler):
  """Handler for cron to delete posts older than 1 hour."""

  def get(self):
    now = datetime.datetime.now()
    onehourago = now - datetime.timedelta(seconds=3600)

    post_query = PostMessage.query(PostMessage.timestamp < onehourago)
    post_keys = post_query.fetch(keys_only=True)
    ndb.delete_multi(post_keys)

class GetData(webapp2.RequestHandler):
  """Handler to fetch the POST data from datastore."""

  def get(self):
    post_query = PostMessage.query().order(-PostMessage.timestamp)
    posts = post_query.fetch(100)

    template = JINJA_ENVIRONMENT.get_template('datatable.html')
    template_values = {'posts': posts}
    self.response.write(template.render(template_values))

    
class MainPage(webapp2.RequestHandler):
  """Main handler that receivers the POST request and also displays them."""

  def get(self):
    template = JINJA_ENVIRONMENT.get_template('index.html')
    template_values = {}
    self.response.write(template.render(template_values))

  def post(self):
    content = json.dumps(self.request.body)
    post = PostMessage()
    post.content = content
    post.put()


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/getdata', GetData),
    ('/wipedata', WipeData),
], debug=False)
