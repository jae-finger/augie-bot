# Augie Bot v0.0
# Author: JAEFinger


# Package Imports
import os
import tweepy
import pandas
import numpy
import random

# Import Custom features
# from features.augie_bark import AugieBark
from features.augie_facts import AugieFact

# Load Environmental Variables
from dotenv import load_dotenv
load_dotenv()

# Create credentials from environmental variables
consumer_key = os.getenv("TW_CONS_KEY")
consumer_secret = os.getenv("TW_CONS_SEC")
access_token = os.getenv("TW_ACCESS_TOKEN")
access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")

# # Set Authentication
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# # Instantiate Tweepy API
# api = tweepy.API(auth)

if __name__ == "__main__":
    # Tweet a random augie fact
    AugieFact(consumer_key, consumer_secret, access_token, access_token_secret)