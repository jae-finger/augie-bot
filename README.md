# AugieBot
## Author: Jonathan Finger
This is AugieBot. My attempt at a basic [twitter](https://twitter.com/AugietheDog) bot about my dog, Augie.

AugieBot is built using the tweepy package (and others) in python 3.9. As of 1/19/2021, AugieBot is still very under construction and has limited capabilities.

### __Current Version (01/21)__
+ A random Augie-Fact is tweeted out when `augie_facts.py` is run. 
+ It can also bark, I guess.
+ The owner deal is blank... for now.


## Misc.
### A Few Tweepy Notes
A status is a tweet.
A friendship is a follow-follower relationship.
A favorite is a like.

### Flask Usage
#### Mac:
```
FLASK_APP=web_app flask run
```

#### Windows:
```
Export FLASK_APP=hello.py # one time set of environmental variable
flask run
```