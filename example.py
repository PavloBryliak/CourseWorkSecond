from idlelib.multicall import r

import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2018-03-18&'
       'sortBy=popularity&'
       'apiKey=6c8d6c5d795342a39577b3df56004f07')

response = requests.get(url)

print(r.json)