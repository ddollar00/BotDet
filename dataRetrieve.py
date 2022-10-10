import tweepy
import json
import csv

import configparser
import pandas as pd

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
user =  []
for i in user:
   try:
      userw=api.get_user(screen_name=i)
   except:
      continue
   ID=userw.id_str
   screenname=userw.screen_name
   location =userw.location
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
   except AttributeError:
     status="none"
   default_profile=userw.default_profile
   default_profile_image=userw.default_profile_image
   extended_profile=userw.has_extended_profile
   name=userw.name
   bot=0

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create excel file





#############################################################
   with open('training_data_5.csv',mode='a',encoding='utf-8') as filee:
     
        writer=csv.writer(filee,delimiter=',',quoting=csv.QUOTE_MINIMAL)
       # writer.writerow(['id','screen_name','location','description','url','followers_count','friends_count','listed_count',
       # 'verified','statuses_count','lang','status','default_profile',
       # 'default_profile_image','extended_profile','name','bot'])
        writer.writerow([ID,screenname,location,desc,url,followers_count,friends_count,listed_count,verified,statuses_count,status,default_profile,
        default_profile_image,extended_profile,name,bot])
 
print("Done, all profile data collected")

