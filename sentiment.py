import tweepy
from textblob import TextBlob

consumer_key = 's5ObZD5UiSyjohChK8dGL44vm'
consumer_secret = 'AWcmmBNIDmuG8DJPztYMWvcRs61RsM6h5PubR1cwAbUxZLEt6X'

access_token = '818369802997796864-OHfvLB8YOAA4Uw5wte6pz2AOvFRmRid'
access_token_secret = 'BHVvYFwjlm1gsxUvkjQIezabe1tpWFGBxldRAu1uEx1Cv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
