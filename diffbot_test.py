#!/usr/bin/env python
import requests
import json

class diffbot(object):
    def __init__(self):
        self.more = ''
    def get_article(self,url,key):  #Fetch JSON for the article
        attempt=0
        while attempt<3:
            try:
              #Fetch the main page
              main='http://api.diffbot.com/v2/article?token='+key+'&url='+url
              print 'Fetching Page'
              raw = requests.get(main,timeout=20)
              raw_json=json.loads(raw.text)
              return raw_json
              break
            except requests.exceptions.SSLError:	#ConnectionError for requests
              print "SSL Error"
              attempt+=1
            except requests.exceptions.ConnectionError:#ConnectionError for requests
              print "ConnectionError"
              continue
              attempt+=1
            except requests.exceptions.Timeout:
              print "Timeout"
              attempt+=1
        return 2    #Error code
    def tags(self,raw): #Return the tags
        return raw['tags']
    def icon(self,raw): #Return the icon
        return raw['icon']
    def text(self,raw): #Return article text
        return raw['text']
    def date_created(self,raw): 
        return raw['date_created']
    def date(self,raw):
        return raw['date']
    def crawl_type(self,raw):
        return raw['type']
    def cid(self,raw):
        return raw['cid']
    def url(self,raw):
        return raw['url']
    def author(self,raw):
        return raw['author']
    def title(self,raw):
        return raw['title']
    def category(self,raw):
        return raw['category']
    def html(self,raw):
        return raw['html']
    def categories(self,raw):
        return raw['categories']
    def supertags(self,raw):
        return raw['supertags']
    def media(self,raw):
        return raw['media']

#Object of diffbot
df=diffbot()
#Diffbot API Key
api_key='api_key'
#URL for page
page_link='http://hackaday.com/2013/12/06/developed-on-hackaday-lets-build-some-hardware/'
raw_data=df.get_article(page_link,api_key)  #Get the JSON
article_text=df.text(raw_data)  #Show the article text
print article_text