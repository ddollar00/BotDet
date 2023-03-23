from datetime import datetime
from itertools import dropwhile, takewhile
import csv
import json
import instaloader
import pandas as pd
import csv
from dateutil.relativedelta import relativedelta

def instacollection(a):
       bot = instaloader.Instaloader()
       #loading usernames count(8) at a time to pull profile information
       username=a
       current_date=datetime.now()
       with open("userig2.csv", mode = 'w', encoding='utf-8')as f:
            #loading the profile of each user 
            try:
                    profile = instaloader.Profile.from_username(bot.context, username)
            except:
                    print("Stop")
           #loading the posts of each user within the certain date points
            posts = instaloader.Profile.from_username(bot.context, username).get_posts()
           # SINCE = datetime(2022,9,3)
            SINCE = current_date - relativedelta(months=1)
            #UNTIL = datetime(2022,10,13)
            UNTIL = current_date
            #setting a variable to an empty string
            p2 = " "
            #creating a statement to allow post to be printed based on the dates set
            for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
            #adding the posts to a string in case there are multiple posts
                p2 += str(post.date)+ "\n"
                
        #writing the data into the csv file
            writer =csv.writer(f, delimiter =',', quoting= csv.QUOTE_MINIMAL)
            writer.writerow(['Username','User ID','Number of Posts','Followers Count','Following Count','Bio','External URL','Verified','Profile Pic','Posts_Dates'])
        #using instaloader class to pull certain key information
            writer.writerow([profile.username,profile.userid,profile.mediacount,profile.followers,profile.followees,profile.biography,profile.external_url,profile.is_verified,profile.get_profile_pic_url(), p2])


def pic(a):
 
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
