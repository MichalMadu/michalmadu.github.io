import tweepy

consumer_key = 'IFuUGrtAHS4PYZHInGz20w8i5'
consumer_secret = 'UApOBPTqFd3yoen1MEkH0IVIFJ7Kv5B6LSjQBscMo6qjSYPe6b'

access_token = '1413986080764923916-D9Cx0frKLgEMVqKQQLjjQWI4k0qE3F'
access_token_secret = 'Df1zdk7uy3orR7uzJ3dk0Bxb3hc1CSNCzgbwGBBH3ZGrQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)