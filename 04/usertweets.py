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
    - [x] save tweets to csv file in data/ subdirectory
    - [x] implement len() an getitem() magic (dunder) methods"""
    def __init__(self, handle, max_id=None):
        self.handle = handle
        self.max_id = max_id
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.tweets = self.get_tweets()
        self.output_file = f'{DEST_DIR}/tweets_{self.handle}.{EXT}'
        self.save_tweets()

    def get_tweets(self):
        statuses = self.api.user_timeline(screen_name=self.handle, count=NUM_TWEETS, max_id=self.max_id)
        tweets = [Tweet(status.id_str, status.created_at, status.text.replace('\n', ' ')) for status in statuses]
        return tweets


    def save_tweets(self):
        with open(self.output_file, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(['id_str', 'created_at', 'text'])
            wr.writerows(self.tweets)

    def __len__(self):
        return len(self.tweets)

    def __getitem__(self, item):
        return self.tweets[item]


if __name__ == "__main__":
    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()