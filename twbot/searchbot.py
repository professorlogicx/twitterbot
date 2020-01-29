import tweepy

consumer_key = "rjS5Rr0pZ3xrR7BSF9mgqGENy"
consumer_secret = "tvio2vFusmoqpxK5q1UCn4aj5LY1HRUw1ELfRQOlhMENq3Mlb2"
key = "1222464601700175872-7S4aSCzUks64BQECoP33dQD45iXm9A"
secret = "ZZXVd9GubnzMhSw3UQPhkgWYl61VRvZRJTAVGgseQmIov"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth)

hashtag = "python"

tweetnum = 5

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnum)

for tweet in tweets:
    tweet.retweet()
