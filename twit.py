from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
# from pymongo import MongoClient

ckey="OdxDK1K6lXgGDq9I2vvDEfnHe"
csecret="qyIMSJoUsVocVtpjuvIcXdcivkmbOrG94uCGymQ1npHlzce4zy"
atoken="3860930353-fE7sHffMJ36wq500d5J7JCUvgS3jZK914LlN65O"
asecret=" qzs97N5uGt0kXPs27RWNCuL49CSC0gqtCdrIs4SXbgzgS"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["india"])

# client = MongoClient()
# client = MongoClient('localhost', 27017)
# db = client.twitter
# db = client['twitter']
# collection = db.test
# collection = db['test']
