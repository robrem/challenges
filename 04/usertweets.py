from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', ['id_str', 'created_at', 'text'])

class UserTweets(object):
    """TODOs:
    - [x] create a tweepy api interface
    - [x] get all tweets for passed in handle
    - [x] optionally get up until 'max_id' tweet id
    - [ ] save tweets to csv file in data/ subdirectory
    - [ ] implement len() an getitem() magic (dunder) methods"""
    def __init__(self, handle, max_id=None):
        self.handle = handle
        self.max_id = max_id
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.tweets = self.get_tweets()
        self.output_file = f'{DEST_DIR}/tweets_{self.handle}.{EXT}'

    def get_tweets(self):
        tweets = []
        statuses = self.api.user_timeline(screen_name=self.handle, count=5, max_id=self.max_id)
        for status in statuses:
            tweet = Tweet(status.id_str, status.created_at, status.text)
            tweets.append(tweet)
        return tweets


    def save_tweets(self):
        with open(self.output_file, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerows(self.tweets)

    def __len__(self):
        pass

    def __getitem__(self, item):
        pass


if __name__ == "__main__":

    # for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
    #     print('--- {} ---'.format(handle))
    #     user = UserTweets(handle)
    #     for tw in user[:5]:
    #         print(tw)
    #     print()
    pass