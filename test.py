# import webapp2

# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.write("Namaste World!")

# app = webapp2.WSGIApplication([('/')], debug=True)

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Namaste User.!")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
