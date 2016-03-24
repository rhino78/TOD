import time
import datetime
import string
import requests
import logging
import tweet_with_db
from bs4 import BeautifulSoup

def main():
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    url = "http://fuckinghomepage.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    str = soup.p.text
    #strip off the vulgar text
    str = str[str.index('.')-len(str)+2:]
    str = string.capwords(str)
    #now we tweet it
    logging.basicConfig(filename='tweet.log', level=logging.INFO)
    logging.info('Tweet log for: '+st)
    tweet_with_db.tweet_it(str)
    #next we tweet the words of wisdom
    row = soup.find_all('p')[1:7]
    str = string.capwords(row[1].string)
    tweet_with_db.tweet_it(str)

if __name__ == '__main__':
    main()
