import re
import string
import sys
from collections import Counter

import nltk
from nltk.corpus import stopwords

from usertweets import UserTweets

def similar_tweeters(user1, user2):
    """TODOs:
        - [x] Retrieve last n tweets for each user
        - [ ] Tokenize tweet words and filter for stop words, URLs, digits, punctuation, etc.
        - [ ] Extract main subjects each user tweets about
        - [ ] Compare subjects and calculate a similarity score"""
    tokens1 = tokenize_tweets(UserTweets(user1).tweets)
    tokens2 = tokenize_tweets(UserTweets(user2).tweets)
    subjects1 = extract_subjects(tokens1)
    subjects2 = extract_subjects(tokens2)
    return calc_similarity_score(subjects1, subjects2)

def tokenize_tweets(user_tweets):
    """Tokenize words for each tweet text in user_tweets filtering out stop words, URLs, digits, punctuation,
        words that only occur once or are less than 3 characters."""
    # TODO: url patterms like //t.co/2tkf4zwija are unfiltered
    tweets = ' '.join([tweet.text for tweet in user_tweets])
    stop_words = set(stopwords.words('english'))
    url_pattern = '(.*?)http.*?\s?(.*?)'
    tokens = [token.lower() for token in nltk.word_tokenize(tweets)
              if token not in stop_words
              and token not in string.punctuation
              and len(token) > 3
              and not token.isdigit()
              and not re.match(url_pattern, token)]
    # Remove tokens that only occur once. Multiples records True if token occurs multi times in tokens, False
    # otherwise. Then, add only tokens that occur mult times back in to tokens list.
    multiples = Counter(tokens)
    final_tokens = []
    for token, count in multiples.items():
        if count > 1:
            for _ in range(count):
                final_tokens.append(token)
    return final_tokens

def extract_subjects(tokens):
    """Extract the main subjects found in tokens."""
    # TODO: reduce to stem words?
    subjects = []
    return subjects

def calc_similarity_score(subjects1, subject2):
    """Calculate a similarity score comparing subjects1 and subjects2."""
    pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
