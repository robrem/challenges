import sys

from usertweets import UserTweets

def similar_tweeters(user1, user2):
    """TODOs:
        - [x] Retrieve last n tweets for each user
        - [ ] Token tweet words and filter for stop words, URLs, digits, punctuation, etc.
        - [ ] Extract main subjects each user tweets about
        - [ ] Compare subjects and calculate a similarity score"""
    tokens1 = tokenize_tweets(UserTweets(user1))
    tokens2 = tokenize_tweets(UserTweets(user2))
    subjects1 = extract_subjects(tokens1)
    subjects2 = extract_subjects(tokens2)
    return calc_similarity_score(subjects1, subjects2)

def tokenize_tweets(user_tweets):
    tokens = []
    return tokens

def extract_subjects(tokens):
    subjects = []
    return subjects

def calc_similarity_score(subjects1, subject2):
    pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
