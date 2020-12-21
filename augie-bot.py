# Augie Bot v0.0
# Author: JAEFinger

# Package Imports
import os
import tweepy
import pandas
import numpy
import random

# Custom features

from features.augie_bark import AugieBark

# Environmental Variables
from dotenv import load_dotenv
load_dotenv()

# Load environment variables
consumer_key = os.getenv("TW_CONS_KEY")
consumer_secret = os.getenv("TW_CONS_SEC")
access_token = os.getenv("TW_ACCESS_TOKEN")
access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")

# Set authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Instantiate tweepy api
api = tweepy.API(auth)

# Get public tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


if __name__ == "__main__":
    tweet_quote()

# Randomly bark
AugieBark(api)
