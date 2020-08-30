import tweepy

consumer_key = "XXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
key = "XXXXXXXXXXXXXXXXXXXXX-7S4aSCzUks64BQECoP33dQD45iXm9A"
secret = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth)

hashtag = "python"

tweetnum = 5

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnum)

for tweet in tweets:
    tweet.retweet()
