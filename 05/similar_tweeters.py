import itertools
import re
import string
import sys
from collections import defaultdict

import nltk
from nltk.corpus import stopwords
from gensim import corpora, matutils

from usertweets import UserTweets

NUM_TWEETS = 100

def similar_tweeters(user1, user2, num_tweets=NUM_TWEETS):
    """TODOs:
        - [x] Retrieve last n tweets for each user
        - [x] Tokenize tweet words and filter for stop words, URLs, digits, punctuation, etc.
        - [ ] Extract main subjects each user tweets about
        - [ ] Compare subjects and calculate a similarity score"""
    tokens1 = tokenize_tweets(UserTweets(user1, num_tweets).tweets)
    tokens2 = tokenize_tweets(UserTweets(user2, num_tweets).tweets)
    return calc_similarity_score(tokens1, tokens2)

def tokenize_tweets(user_tweets):
    """
    Tokenize words for each tweet text in user_tweets filtering out stop words, URLs, digits, punctuation,
    words that only occur once or are less than 3 characters.

    :return: list of lists, each of which is a tokenized and filtered version of a single tweet text.
    """
    tweets = [filter_tweet(tweet.text) for tweet in user_tweets]

    # Remove tokens that only occur once.
    frequency = defaultdict(int)
    for tweet in tweets:
        for token in tweet:
            frequency[token] += 1

    return [[token for token in tweet if frequency[token] > 1] for tweet in tweets]

def filter_tweet(tweet_text):
    stop_words = set(stopwords.words('english'))
    basic_url_pattern = '(.*?)http.*?\s?(.*?)'
    twitter_url_pattern = '(.*?)//t\.co/?(.*?)'

    return [token.lower() for token in nltk.word_tokenize(tweet_text)
            if len(token) > 3
            and token not in stop_words
            and token not in string.punctuation
            and not token.isdigit()
            and not re.match(basic_url_pattern, token)
            and not re.match(twitter_url_pattern, token)]

def get_corpus(tokenized_tweets):
    '''
    Extract the subjects found in tokens and return a corpus-like structure where all documents have been flattened
    to a single list of tokens and counts.
    '''
    # TODO: reduce to stem words first?

    # assign unique integer IDs to each token
    dictionary = corpora.Dictionary(tokenized_tweets)

    # represent each tweet as counts of its tokens that appear in vocabulary in the form of tuples:
    # (id_of_token_in_vocabulary, count)
    corpus = [dictionary.doc2bow(tweet) for tweet in tokenized_tweets]

    return flatten(corpus)

def flatten(corpus):
    '''
    Transform corpus from a list of lists to a single list, accumulating the counts for a single token from
    all documents.
    :param corpus: a lists of lists, each of which represents a tokenized document in the form of tuples:
    (token_id, count).
    :return: the flattened corpus
    '''
    corpus_counts = defaultdict(int)

    for doc in corpus:
        for token_id, count in doc:
            corpus_counts[token_id] += count

    return [(token_id, count) for token_id, count in corpus_counts.items()]

def calc_similarity_score(tokens1, tokens2):
    '''
    Calculate a similarity score comparing tokens1 and tokens2 using cosine similarity.
    '''
    corpus1 = get_corpus(tokens1)
    corpus2 = get_corpus(tokens2)
    return matutils.cossim(corpus1, corpus2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    score = similar_tweeters(user1, user2)
    print(f'Similarity score: {score}')
