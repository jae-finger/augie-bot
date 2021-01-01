# Import packages
import random
import tweepy


def AugieFact(consumer_key, consumer_secret, access_token, access_token_secret):
    """
    Tweets a random augie fact.
    """
    # Set interval
    interval = 60 * 60 * 24

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
        'For some reason, everybody thinks I am a goldendoodle.'
    ]

    interval = 4

    if interval == 4:
        print('Getting a random fact...')
        rand_fact = augie_facts[random.randint(0, len(augie_facts)-1)]
        print(f'Attempting to tweet fact # {len(augie_facts)-1}')
        api.update_status(rand_fact)
        # time.sleep(interval)
        # print(rand_fact)

    # while True:
    # print('Getting a random fact...')
    # rand_fact = augie_facts[random.randint(0, len(augie_facts)-1)]
    # api.update_status(rand_fact)
    # time.sleep(interval)
