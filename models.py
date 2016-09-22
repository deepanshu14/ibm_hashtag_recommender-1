from app import db
import json
class ScrapePost(db.Model):
	__tablename__ ="posts"

	id = db.Column(db.Integer,primary_key = True)
	url_ = db.Column(db.String,nullable = False)
	count = db.Column(db.String,nullable = False)


	def __init__(self,url_,count):
		self.url_ = url_
		self.count = count

	def __repr__(self):
		return "<id {}  {}>".format(self.url_,self.count)
	