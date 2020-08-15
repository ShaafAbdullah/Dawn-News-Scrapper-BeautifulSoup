"""
Created on Sun Jun 28 20:45:50 2020
@author: MOHSIN
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

fileName = "dawn_business_7.csv"
f = open(fileName,"w")
headers = "headline, date\n"
f.write(headers)
for year in range(2020,2021):
    for month in range(7,8):
        for day in range(1,12):

            if(month < 9 and day > 9):
                url_to_scrape = "https://www.dawn.com/newspaper/business/"+str(year)+"-0"+str(month)+"-"+str(day)+"/"
            elif(month>9 and day <= 9):
                url_to_scrape = "https://www.dawn.com/newspaper/business/"+str(year)+"-"+str(month)+"-0"+str(day)+"/"
            elif(month<9 and day <=9):
                url_to_scrape = "https://www.dawn.com/newspaper/business/"+str(year)+"-0"+str(month)+"-0"+str(day)+"/"
            else:
                url_to_scrape = "https://www.dawn.com/newspaper/business/"+str(year)+"-"+str(month)+"-"+str(day)+"/"

            headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/20.0'}
            #create connection with url
            try:
                client_page = requests.get(url_to_scrape,headers=headers)
            except:
                print("Request aborted due to unknown reason!")
                pass
            page_html = client_page.text
            client_page.close()
            #parse html recieved
            page_soup = soup(page_html,"html.parser")

            #retrieving top stories from parsed html
            top_stories = page_soup.find_all("article",{"data-layout":"story"})

            for news in top_stories:

                headline = news.h2.text
                first = headline.split()
                try:
                    if(first[0] =="Youtube" or first[1] =="gold"):
                        break
                    print(headline)
                except:
                    pass
                headline = headline.replace(","," ")
                headline = headline.replace("\n"," ")
                f.write(headline+","+str(year)+" "+str(month)+" "+str(day)+"\n")
f.close()
