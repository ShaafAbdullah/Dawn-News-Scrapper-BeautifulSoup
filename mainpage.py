"""
Created on Sun Jun 28 20:45:50 2020
@author: SHAAF ABDULLAH
"""
import urllib
import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep
import datetime
stock_time=datetime.datetime.now()
date=datetime.datetime.now().date()
day=date.day
month=date.month
fileName = "dawn_simple.csv"
f = open(fileName,"w")
headers = "headline, date\n"
f.write(headers)
for year in range(2020,2021):
    for month in range(month,month+1):
        for day in range(day-2,day+1):
            if(month < 9 and day > 9):
                url_to_scrape = "https://www.dawn.com/archive/"+str(year)+"-0"+str(month)+"-"+str(day)+"/"
            elif(month>9 and day < 9):
                url_to_scrape = "https://www.dawn.com/archive/"+str(year)+"-"+str(month)+"-0"+str(day)+"/"
            elif(month<9 and day <9):
                url_to_scrape = "https://www.dawn.com/archive/"+str(year)+"-0"+str(month)+"-0"+str(day)+"/"
            else:
                url_to_scrape = "https://www.dawn.com/archive/"+str(year)+"-"+str(month)+"-"+str(day)+"/"

            try:
                #create connection with url
                client_page = uReq(url_to_scrape)
                sleep(2)
            except urllib.error.HTTPError as e:
                if e.getcode() == 404: # check the return code
                    continue
            page_html = client_page.read()
            client_page.close()
            #parse html recieved
            page_soup = soup(page_html,"html.parser")

            #retrieving top stories from parsed html
            top_stories = page_soup.find_all("article",{"data-layout":"story"})

            for news in top_stories:

                headline = news.h2.text
                headline.encode("utf-8")
                try:
                    date = (news.find_all("span",{"class":"timeago"}))[0].text
                    date.encode("utf-8")
                except:
                    break
                headline = headline.replace(","," ")
                headline = headline.replace("\n"," ")
                f.write(headline+","+date.replace(","," ")+"\n")
f.close()
