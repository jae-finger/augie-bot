import random
import tweepy

def randomBark(twit_api):
    """
    This function creates a random bark when called if the roll is correct.
    """
    rand_tweet = random.randint(1, 25)

    if rand_tweet == 1:
        bark_num = random.randint(0, 7)
        tweet_barks = ['woof', 'arf', 'bark', 'murfph', 'woof!', 'arf!', 'bark!', 'murfph!']
        print(f'I rolled a {rand_tweet} and will tweet: {tweet_barks[bark_num]}')
        # twit_api.update_status(tweet_barks[bark_num])
        print(tweet_barks[bark_num])
    else:
        print(f'I rolled a {rand_tweet} so I will stay quiet')