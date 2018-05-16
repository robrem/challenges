import unittest

from similar_tweeters import similar_tweeters, tokenize_tweets, extract_subjects
from tweets import Tweet, TWEETS  # mock data

class TestSimilarTweeters(unittest.TestCase):

    def test_tokenize_tweets(self):
        print(tokenize_tweets(TWEETS))