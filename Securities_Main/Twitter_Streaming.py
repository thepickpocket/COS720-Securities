from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from Authentication import Auth
from TIKMongoDriver import MongoDriver

Database = None

class StdOutListener(StreamListener):

    def on_data(self, data):
        global Database
        #Database.saveData(data)
        print data
        return True

    def on_error(self, status):
        print status


class TwitterStream:
    def __init__(self):
        global Database #Declares variable to be the global reference
        Database = MongoDriver()
        return None

    def getStream(self):
        #This handles Twitter authetification and the connection to Twitter Streaming API
        keys = Auth()
        l = StdOutListener()
        auth = OAuthHandler(keys.customerKey, keys.cutomerSecret)
        auth.set_access_token(keys.accessToken, keys.accessSecret)
        stream = Stream(auth, l)

        #This line filter Twitter Streams to capture data
        stream.filter(track=['me', 'the', 'a', ' '], async=True)