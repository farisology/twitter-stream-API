#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#these are the user credentials to access Twitter API 
access_token = "access_token of your application"
access_token_secret = "access_token_secret of your application"
consumer_key = "consumer_key"
consumer_secret = "consumer_key"


#basic listener to print received tweets
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #Twitter authetification and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Here we filter the tweets based on the keywords: 'money', 'love'
    stream.filter(track=['love','money'])