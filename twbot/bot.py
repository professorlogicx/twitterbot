import tweepy
import time

consumer_key = "rjS5Rr0pZ3xrR7BSF9mgqGENy"
consumer_secret = "tvio2vFusmoqpxK5q1UCn4aj5LY1HRUw1ELfRQOlhMENq3Mlb2"
key = "1222464601700175872-7S4aSCzUks64BQECoP33dQD45iXm9A"
secret = "ZZXVd9GubnzMhSw3UQPhkgWYl61VRvZRJTAVGgseQmIov"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)


api = tweepy.API(auth)

file_name = "last_id.txt"


def read_last_id(file_name):
    file_name_read = open(file_name, "r")
    last_used_id = int(file_name_read.read().strip())
    file_name_read.close()
    return last_used_id


def write_last_id(file_name, last_used_id):
    file_name_write = open(file_name, "w")
    file_name_write.write(str(last_used_id))
    file_name_write.close()
    return


def to_reply():
    recent = api.mentions_timeline(read_last_id(file_name))
    for tweet in reversed(recent):
        if "#tweet" in tweet.text:
            print("replied to ID: " + str(tweet.id))
            # will completely override the text file.
            api.update_status("@" + tweet.user.screen_name +
                              " It worked !", tweet.id)
            # "@" + tweet.user.screen_name + "content" , tweet.id
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            write_last_id(file_name, tweet.id)


while True:
    to_reply()
    time.sleep(2)
    print("In Progress....")
