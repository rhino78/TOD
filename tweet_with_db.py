import logging
import tweepy
import sqlite3
import tweet_creds


def tweet_it(status):
    auth = tweepy.OAuthHandler(tweet_creds.CONSUMER_KEY, tweet_creds.CONSUMER_SECRET)
    auth.set_access_token(tweet_creds.ACCESS_KEY, tweet_creds.ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(status=status)

