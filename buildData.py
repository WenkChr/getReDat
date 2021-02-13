import praw
import os
import pandas as pd
from dotenv import load_dotenv

'''
Test for using python to scrape financial subreddits for trending stock tickers
Experiment to see trends over time

'''

#-----------------------------------------------------------------------------------------------
# Inputs

BASEDIR = os.getcwd()
load_dotenv(os.path.join(BASEDIR, 'environments.env'))

clientID = os.getenv('CLIENT_ID')
clientSecret = os.getenv('CLIENT_SECRET')
userAgent = os.getenv('USER_AGENT')

#-----------------------------------------------------------------------------------------------

posts = []
# Setup Reddit linkage with credentials from apps section of account
reddit = praw.Reddit(client_id= clientID, 
                    client_secret= clientSecret, 
                    user_agent= userAgent
                    )

for post in reddit.subreddit('CanadianInvestor').hot(limit=10):
    print(post.title)
    posts.append([post.title, 
                post.score, 
                post.id, 
                post.subreddit, 
                post.url,
                post.num_comments, 
                post.selftext, 
                post.created])

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

posts.to_csv(os.path.join(BASEDIR, 'test.csv'))
print(posts.head())

print('DONE')
