#default config
#add secret key here
class BaseConfig(object):
 	DEBUG = False
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
	# SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
	Debug = True

class ProductionConfig(BaseConfig):
	#to avoid server code to exposed
	Debug = False