
# coding: utf-8

# In[ ]:

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

api_key = "FuzkA8SS76XPD6izHNRs1TVt8"
api_secret = "MtPZepdC3XGp1MUs8pHw6flg0OZiQJwmgaykLz5LMAhamyQpj6"
access_token_key = "2907029881-daxkNwOFEHhWUB6WkfE3ZpswnqR0afUAmKOjCOF"
access_token_secret = "6svj827OyNHRkd0EOvbHEHKcmwNhJnQPW8ZvFezNNAQfm"

class listener(StreamListener):
    def on_data(self,data):
        try: 
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print(tweet)
            TwitterFile = open('twitterDB.csv','a')
            TwitterFile.write(tweet)
            TwitterFile.write('\n')
            TwitterFile.close()
            return True
        except (BaseException, e):
            print ('Failed onData, ', str(e))
            time.sleep(5)
            
    def on_error(self, status):
        print(status)

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#ThisIsWhatAnxietyFeelsLike"])


# In[ ]:



