# Augie Bot v0.0
# Author: JAEFinger

# Package Imports
import os
import tweepy
import pandas
import numpy

from dotenv import load_dotenv
load_dotenv()

# Load environment variables
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

# if __name__ == '__main__':
print('woof!')