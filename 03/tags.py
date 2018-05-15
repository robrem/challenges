
import xml.etree.ElementTree as ET
import itertools
from difflib import SequenceMatcher
from collections import Counter

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tags = []
    e = ET.parse(RSS_FEED).getroot()
    for category in e.iter('category'):
        tags.append(category.text.replace('-', ' ').lower())
    return tags


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    tags = Counter(tags)
    return tags.most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    similar_tags = []
    tags = list(set(tags))
    for pair in itertools.combinations(tags, 2):
        # Short circuit if first chars don't match
        if pair[0][0] == pair[1][0]:
            if SequenceMatcher(None, *pair).ratio() > SIMILAR:
                similar_tags.append(sorted(pair))
    return similar_tags

if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))