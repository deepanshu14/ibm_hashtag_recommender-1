import urllib2
import re
from bs4 import BeautifulSoup
import sys
import operator
import re
import nltk
from collections import Counter


def call_count(word_):
	url_ = "https://www.hashtags.org/analytics/{}/".format(word_)
	html = urllib2.urlopen(str(url_)).read()
	print html
	soup = BeautifulSoup(html, 'html.parser')
	for script in soup(["script", "style"]):
	    script.extract()    # rip it out
	    # "[document]","head","title"
	# get text
	text = soup.get_text()

    # break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	nltk.data.path.append('./nltk_data/')  # set the path
	tokens = nltk.word_tokenize(text)
	text = nltk.Text(tokens)
	# remove punctuation, count raw words
	print text
	user_ = re.findall(r'.*@(\w+)',str(text))
    
    
	print user_

call_count("food")

