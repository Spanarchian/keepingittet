import tweepy
from tweepy import OAuthHandler

consumer_key = 'BoNSaXWtgDz2K4DuqkRfASNDY'
consumer_secret = '9olBHMNZOzA7anKLoTOXXmPyuLijYFzCG41DoursKjdwDFC6vw'
access_token = '1037467608327639040-wMubLYx8FITiWaTBSAvFp6aYWssk14'
access_secret = '6EYGBev3DBwMRuHToghmOfewREqick18BMG21QHpSGJ0I'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(1):
    # Process a single status
    print(status)


# for status in tweepy.Cursor(api.user_timeline, q="Spanarchian").items(10):
#     # Process a single status
#     print(status.text)


# for status in tweepy.Cursor(api.mentions_timeline).items(10):
#     # Process a single status
#     print(status.entities["hashtags"][0]["text"])
