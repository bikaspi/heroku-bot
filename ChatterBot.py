# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = '8VKWmAFdU2LLxjNVdgNinqjzd'
consumer_secret = 'kdazEP2a845PlT5JWedslTim48SDgbovjEFdN5GdLIQuAzlRJM'
access_token = '980980635744354304-qTGhWz2CXJeHZE7xZt8ttbe9SHvR5hd'
access_token_secret = '3bQiV5Ttroo4MrJoqyJ3byM83XGBYs3k1ZXATMy8XHv8a'
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
# Create a function that tweets
# def TweetOut(tweet_number):
#     api.update_status(
#         "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
#         tweet_number)

# Create a function that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1

# comment