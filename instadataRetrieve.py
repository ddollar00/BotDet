from datetime import datetime
from itertools import dropwhile, takewhile
import csv
import json
import instaloader
import pandas as pd
import csv

def instacollection(a):
       bot = instaloader.Instaloader()
       #loading usernames count(8) at a time to pull profile information
       username=a
       current_date=datetime.now()
       with open("userig2.csv", mode = 'w', encoding='utf-8')as f:
            #loading the profile of each user 
            profile = instaloader.Profile.from_username(bot.context, username)
           #loading the posts of each user within the certain date points
            posts = instaloader.Profile.from_username(bot.context, username).get_posts()
            SINCE = datetime(2022,9,3)
            #SINCE = datetime(current_date.year,current_date.month-1,3)
            UNTIL = datetime(2022,10,13)
            #UNTIL = datetime(current_date.year,current_date.month,20)
            #setting a variable to an empty string
            p2 = " "
            #creating a statement to allow post to be printed based on the dates set
            for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
            #adding the posts to a string in case there are multiple posts
                p2 += str(post.date)+ "\n"
                
        #writing the data into the csv file
            writer =csv.writer(f, delimiter =',', quoting= csv.QUOTE_MINIMAL)
            writer.writerow(['Username','User ID','Number of Posts','Followers Count','Following Count','Bio','External URL','Verified','Profile Pic','Real or Fake','Posts_Dates'])
        #using instaloader class to pull certain key information
            writer.writerow([profile.username,profile.userid,profile.mediacount,profile.followers,profile.followees,profile.biography,profile.external_url,profile.is_verified,profile.get_profile_pic_url(),"  ", p2])
