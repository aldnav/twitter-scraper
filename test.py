import sys

from twitter_scraper import get_tweets

user = 'kennethreitz'
if len(sys.argv) > 1:
    user = sys.argv[1]

print('Getting tweets for %s' % user)
print(list(get_tweets(user, pages=1))[0])

for tweet in get_tweets(user, pages=1):
    print(tweet)
