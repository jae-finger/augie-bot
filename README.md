# AugieBot
## Author: Jonathan Finger
This is AugieBot. My attempt at a basic [twitter](https://twitter.com/AugietheDog) bot about my dog, Augie.

AugieBot is built using the tweepy package and flask, primarily. As of 5/1/21, AugieBot is still under construction and has limited capabilities.

# __Current Version (05/21)__
    + The current iteration is deployed on my free heroku account [here](https://augiebot.herokuapp.com/).
    + If it is has been at least 24 hours since the last Augie fact, then it will tweet a random fact.
    + Still some issues: can't control if a fact has been tweeted about lately, nothing to display on the web-server side, and the app has to be open on heroku (not asleep) to work.

# Misc.
## Stack
1. Python 3.9
2. Tweepy Package
3. Flask

# To Do:
    - Continue rewriting this ReadMe with installation and use instructions
    - Rewrite core to be user-authenticated, tweets or barks based on time in DB automatically, have a dashboard on the frontpage with a gallery
    - Address issues
    - Add dashboard part
    - Add more Augie facts when I'm less depressed about his latest haircut
    - Think of a way/how/why to make it bark again
