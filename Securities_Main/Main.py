# COS 720 Securities
# Assignment by Jason R. Evans 13032608 & Vivian L. Venter 13238435

import sys
import tweepy
import Authentication

keys = Authentication.Auth()

# Starting the OAuth authentication with Twitter via Tweepy
auth = tweepy.OAuthHandler(keys.customerKey, keys.cutomerSecret)
auth.set_access_token(keys.accessToken, keys.accessSecret)
twitterAPI = tweepy.API(auth)

publicTweets = twitterAPI.home_timeline()
for tweet in publicTweets:
    print tweet.text