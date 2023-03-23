import tweepy
import json
import csv

import configparser
import pandas as pd
import os
import io
import cloudscraper
from PIL import Image
# read configs

def collect(a):
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
  #print("enter user:")
  user =  a

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
 
  
#os.system('python3 TBotDetection.py')
def pic(a):
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
  #print("enter user:")
  user =  a
  userw=api.get_user(screen_name=user)
  url = "https://scontent-atl3-1.cdninstagram.com/v/t51.2885-19/334844346_672043391416102_183500895920340597_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=110&_nc_ohc=0NBIvVXfw_sAX8Nr7ma&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBP11Eau8YvWvKKOABxSWOyYwJOc2EYAWz82KA0LmGupA&oe=64209783&_nc_sid=8fd12b"
  jpg_data = (
    cloudscraper.create_scraper(
        browser={"browser": "firefox", "platform": "windows", "mobile": False}
    )
    .get(userw.profile_image_url)
    .content
  )
  pil_image = Image.open(io.BytesIO(jpg_data))
  png_bio = io.BytesIO()
  pil_image.save(png_bio, format="PNG")
  png_data = png_bio.getvalue()
  return png_data
  




