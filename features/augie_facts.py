# Import packages
import random
import tweepy


def AugieFact(consumer_key, consumer_secret, access_token, access_token_secret):
    # Set Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Instantiate Tweepy API
    api = tweepy.API(auth)

    # Create list of augie facts
    augie_facts = [
        'Hello -- my name is Augie the doggie.',
        'I am an apricot purebred miniature poodle.',
        'My favorite toy is my stuffed sheep.',
        'I am six months old!',
        'My favorite treats are my bison burgs.',
        "My nickname is 'poof head'.",
        'I enjoy going to obedience class each week.',
        'My best friends are Cosmo and Siri.'
    ]

    print(augie_facts[random.randint(0, len(augie_facts)-1)])