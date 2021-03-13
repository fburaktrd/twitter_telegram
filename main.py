import tweepy
from time import *
import teleg
import os
import datetime as dt

#Your Twitter API's keys.
#If you going to use this bot on cloud (Google cloud etc.)I used OS library for safety to get all this keys/tokens from local environment variables.
#If you don't want to do that and you'll run this code on your local, you can define all thoose variables as a string.

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("accsess_token")
access_token_secret = os.getenv("access_token_secret")

#Tweepy
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

name = "elonmusk" #Account name that you want to get tweets from.

tweets = api.user_timeline(screen_name = name, count=1, tweet_mode = "extended")

for i in tweets:
    ft_link = "https://twitter.com/"+ name +"/status/" + str(i._json["id"])

with open("ftweet.txt","r+") as tw:
    if len(tw.readlines()) != 0:
        tw.seek(0)
        if ft_link != tw.readlines()[0]:
            tw.seek(0)
            #tweet_link = "https://twitter.com/" + name + "/status/" + str(i._json["id"])
            tw.write(ft_link)
    else:
        tw.write(ft_link)

while True:
    
    tweets = api.user_timeline(screen_name = name, count=1, tweet_mode="extended")
    
    if len(tweets)==0:#If we could not get informations from API.
        sleep(2)
        continue 

    current_time = dt.datetime.utcnow()
    #Checking tweet's date.
    time = tweets[0]._json["created_at"].replace("+0000 ","")[4:]
    cnv_time = dt.datetime.strptime(time, '%b %d %H:%M:%S %Y')#Converting to datetime object.
    dif = current_time-cnv_time # diffrence
    
    for i in tweets:
        
        t_tlink = "https://twitter.com/" + name + "/status/" + str(i._json["id"])
        
        if t_tlink != ft_link and dif.seconds <= 300:
            
            ft_link = t_tlink

            tweet_link = "https://twitter.com/" + name + "/status/" + str(i._json["id"])

            teleg.message(tweet_link)
            
            with open("ftweet.txt","w") as tw:
                tw.write(ft_link)
    sleep(60)
