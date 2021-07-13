import tweepy

consumer_key = 'IFuUGr'
consumer_secret = 'UApOBPTqFd3yoen1'

access_token = '1413986080764923916-D9Cx0frKLgEMVq'
access_token_secret = 'xb3hc1CSNCzgbwGBBH3ZGrQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)