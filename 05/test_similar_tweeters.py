import unittest

from similar_tweeters import similar_tweeters, tokenize_tweets, get_corpus, calc_similarity_score
from tweets import Tweet, TWEETS, TEST_TOKENS, TEST_CORPUS  # mock data

class TestSimilarTweeters(unittest.TestCase):

    def test_tokenize_tweets(self):
        tokens = tokenize_tweets(TWEETS)
        self.assertEqual(tokens, TEST_TOKENS)

    def test_get_corpus(self):
        corpus = get_corpus(tokenize_tweets(TWEETS))
        self.assertEqual(corpus, TEST_CORPUS)

    def test_calc_similarity_score(self):
        t1 = t2 = tokenize_tweets(TWEETS)
        score = calc_similarity_score(t1, t2)
        self.assertEqual(score, 0.9999999999999998)