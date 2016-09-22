
from flask import Flask,render_template,request,session,url_for,redirect
from flask.ext.sqlalchemy import SQLAlchemy
import os
import urllib2
import re
from bs4 import BeautifulSoup
import sys
import operator
import re
import nltk
from collections import Counter
import requests

app = Flask(__name__)


#can set the os.environ to get the config from enviroment variable
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)


from scrape_url import call_count   #this imports the module which performs the scraping
from models import *



# @app.route('/')
# def index():
#     return render_template('welcome.html')


# # The display page
# # Input : Takes the Input URL Through the html page and stores the output to posts db.
@app.route('/', methods=['GET','POST'])

def fetch_result():
	errors = []
	results = {}
	res = []

	if request.method == "POST":
		
		try:
		    url_ = request.form['url']
		    html = urllib2.urlopen(str(url_)).read()
		except:
		    errors.append(
		        "Unable to get URL. Please make sure it's valid and try again."
		    )
		    return render_template('welcome.html', errors=errors)
		if html:
			results,raw_word_count = call_count(html)
			raw_word_count = dict(raw_word_count)
			
			try:
			    result = ScrapePost(
			        url_=url_,
			        count=str(raw_word_count)
			        
			    )
			    errors.append("{} have been saved successfully to database. To view the entry press saved button".format(url_))
			    db.session.add(result)
			    db.session.commit()
			    
		        
			except Exception, e:
				errors.append("Unable to add item to database.")

		
	return render_template('welcome.html', errors=errors, results=res)




# To view the saved data in the DB
# Input : Takes the entry through checkbox through html page and outputs the data in a form of dictionary

@app.route('/getdata',methods = ['GET','POST'])
def getdata():
	data_ = [] 
	if request.method == "POST":
		url_ = db.session.query(ScrapePost).all()
		value = request.form.getlist("check")
		if len(value) == 0:
			
			return redirect(url_for('getdata'))

		for v in value:
			
			que = db.session.query(ScrapePost).get(int(v))
			data_.append(que)
		return 	render_template('display.html', results=data_)
	elif request.method == "GET":

		posts = db.session.query(ScrapePost).all()
		
		return render_template('new.html',posts = posts)
	else:
		pass

# To Delete the entry from the database
@app.route("/deleteconfig",methods = ['GET','POST'])
def deleteconfig():
	if request.method == "POST":
		value = request.form.getlist('check') 
		print value
		if len(value)==0:
			return redirect(url_for('deleteconfig'))
		for v in value:
			db.session.query(ScrapePost).filter(ScrapePost.id == int(v)).delete(synchronize_session=False)
		db.session.commit()
		return redirect(url_for('saveconfig'))
	elif request.method == "GET":
		posts = db.session.query(ScrapePost).all()
		
		return render_template('new2.html',posts = posts)
	else:
		pass

# To view the data stored in the database
# Output : List of all the links saved in the database 
@app.route("/saveconfig",methods = ['GET','POST'])
def saveconfig():
	posts = db.session.query(ScrapePost).all()
	return render_template('all_record.html',posts = posts)

if __name__ == "__main__":
    app.run(debug = True)