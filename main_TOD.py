#!/usr/bin/env python
import time
import datetime
import string
import requests
import logging
import tweet_with_db
import urllib3

from bs4 import BeautifulSoup


def main():
    logging.basicConfig(filename='/home/ryan/github/TOD/tweet.log', level=logging.INFO)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    url = "https://fuckinghomepage.com/"
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content, "html.parser")
    tweet_str = soup.p.text
    # strip off the vulgar text
    tweet_str = tweet_str[tweet_str.index('.') - len(tweet_str) + 2:].lower()
    # 12/4/2019 noticed that they stopped putting the little tip at the top
    # just going to check on this for now
    if not 'fucking' in tweet_str:
        #tweet_str = string.capwords(tweet_str)
        # now we tweet it
        logging.basicConfig(filename='tweet.log', level=logging.INFO)
        logging.info('Tweet log for: ' + st)
        # tweet_with_db.tweet_it(tweet_str)
        print(tweet_str)


    # next we tweet the words of wisdom
    row = soup.find_all('p')[1:7]
    tweet_str = row[1].string.lower()
    tweet_with_db.tweet_it(tweet_str)


if __name__ == '__main__':
    main()
