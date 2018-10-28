import tweepy
from tweepy import OAuthHandler
from init import TweeterWrapper as Init
import csv

from model import User

TweeterWrapper = Init.TweeterConnection()
auth = OAuthHandler(TweeterWrapper.get_consumer_key(), TweeterWrapper.get_consumer_secret())
auth.set_access_token(TweeterWrapper.get_access_secret(), TweeterWrapper.get_access_secret())
api = tweepy.API(auth)


def collect_data(current_user):
    new_tweets = api.user_timeline(current_user)
    print(new_tweets)
    out_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in new_tweets]
    write_csv(current_user, out_tweets)


def write_csv(current_user, tweets):
    with open('%s_tweets.csv' % current_user, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(tweets)
    pass


collect_data("@realDonaldTrump")
