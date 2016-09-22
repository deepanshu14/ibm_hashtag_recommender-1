# Flask-scrapper

This Flask app basically scrape and then process the word counts from a webpage using the requests, BeautifulSoup, and Natural Language Toolkit (NLTK) libraries and also provides the option of viewing the scraped data with its url as well as deleting the data from the Database.

##STEPS

```sh
$virtualenv --no-site-packages venv
$source venv/bin/activate
$pip install -r requirement.txt
```

#Set Up DB
```sh
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

#Run
```sh
$python run.py
```
