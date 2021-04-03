import tweepy
import os
from flask import Flask

# Load Environmental Variables
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
