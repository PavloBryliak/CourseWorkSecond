import json
import requests
from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='6c8d6c5d795342a39577b3df56004f07')

top_headlines = newsapi.get_top_headlines(#q='bitcoin',
                                          #category='business',
                                          #language='en',
                                          country='us',
                                          from_param='2018-04-24')


all_articles = newsapi.get_everything(q='bitcoin',
                                      domains='bbc.co.uk',
                                      from_parameter='2018-05-24',
                                      to='2018-05-24',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

sources = newsapi.get_sources()
print(top_headlines)