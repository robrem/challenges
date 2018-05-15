import xml.etree.ElementTree as ET
from collections import defaultdict

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    tags = defaultdict(int)
    e = ET.parse(RSS_FEED).getroot()
    for category in e.iter('category'):
        print(category.text.replace('-', ' '))
        tags[category.text] += 1
    return tags


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    pass


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    pass


if __name__ == "__main__":
    # tags = get_tags()
    # top_tags = get_top_tags(tags)
    # print('* Top {} tags:'.format(TOP_NUMBER))
    # for tag, count in top_tags:
    #     print('{:<20} {}'.format(tag, count))
    # similar_tags = dict(get_similarities(tags))
    # print()
    # print('* Similar tags:')
    # for singular, plural in similar_tags.items():
    #     print('{:<20} {}'.format(singular, plural))
    pass