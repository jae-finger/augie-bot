# Import packages
import random
import tweepy
import os
import time

# Load Environmental Variables
from dotenv import load_dotenv

def AugieFact():
    """
    Tweets a random augie fact.
    """

    load_dotenv()

    # Set desired time interval
    interval = 86400  # seconds in 24 hours

    # Create credentials from environmental variables
    consumer_key = os.getenv("TW_CONS_KEY")
    consumer_secret = os.getenv("TW_CONS_SEC")
    access_token = os.getenv("TW_ACCESS_TOKEN")
    access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")

    # Set Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Instantiate Tweepy API
    api = tweepy.API(auth)

    # Create list of augie facts
    augie_facts = [
        'Hello -- my name is Augie the doggy.',
        'I am an apricot, purebred miniature poodle.',
        'My favorite toy is my stuffed sheep.',
        'My favorite treats are my bison burgs.',
        "My nickname is 'poof head'.",
        'I enjoy going to obedience class each week.',
        'My best friends are Cosmo and Siri.',
        'I realllllly love walks.',
        'I spend most of my days sleeping on the couch.',
        'My favorite treats are bison burgers.',
        'I prefer winter over summer; walks are so much cooler then.',
        'For some reason, everybody thinks I am a goldendoodle.',
        'I know sit, down, stay, come, shake, high-five, and more...',
        'I enjoy going to obedience class each week!',
        'I am owned and maintained by: @datakage <3',
        "I like to bark when I do tricks -- sometimes I'm extra spicy.",
        'I live outside Chicago, Illinois.',
        'I was born on June 10th, 2020 on a farm in central Illinois.',
        'I am beloved by @allie_rae_muses .',
        'Sometimes, people stop their cars to tell me how cute I am.',
        'What personality do I have? I just want everyone to love me.',
        'My favorite food: anything with sweet potato!!',
        "When my hair gets too long, it covers my eyes and I can't see!",
        "I like to play with my toys so violently that I often damage the floor.",
        "When I get really excited I squeeeeeeeeaaak~",
        "My worst nightmare is having to go to the groomer :(.",
        "I have some low-IQ back legs.",
        "Maybe someday I'll get a chance to dog agility like the ones on TV...",
        "When my hair isn't brushed, it gets matted, and then the groomer has to shave it off T_T.",
        "I love it when someone puts cooked pumpkin on my food!"
    ]

    while True:
        print('Getting a random fact...')
        rand_fact = augie_facts[random.randint(0, len(augie_facts) - 1)]
        print(f'Attempting to tweet fact # {len(augie_facts) - 1}')
        api.update_status(rand_fact)
        time.sleep(interval)


if __name__ == '__main__':
    AugieFact()
