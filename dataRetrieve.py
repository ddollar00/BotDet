import tweepy
import json
import csv

import configparser
import pandas as pd
import os
# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
print("enter user:")
user =  input()

userw=api.get_user(screen_name=user)

  
ID=userw.id_str
screenname=userw.screen_name
desc=userw.description
url=userw.url
followers_count=userw.followers_count
friends_count=userw.friends_count
listed_count=userw.listed_count
created_at=userw.created_at
verified=userw.verified
statuses_count=userw.statuses_count
try:
  status=userw.status
except:
  status="none"
name=userw.name


# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create excel file





#############################################################
with open('test6.csv',mode='w',encoding='utf-8') as filee:
     
       writer=csv.writer(filee,delimiter=',',quoting=csv.QUOTE_MINIMAL)
       writer.writerow(['screen_name','description','url','followers_count','friends_count',
       'verified','statuses_count','status','name'])
       writer.writerow([screenname,desc,url,followers_count,friends_count,verified,statuses_count,status,name])
 
print("Done, all profile data collected")
#os.system('python3 TBotDetection.py')

