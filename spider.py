# encoding=utf8

import requests
import json
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",}

def spider_for_url(url):
	obj = {}
	obj['article'] = []
	for i in range(2,22):
		match = 0
		url = url + str(i)  # for different category
		r = requests.get(url,headers=headers) 

		soup = BeautifulSoup(r.text, "html.parser")
		print soup.prettify()

		for drink in soup.select('.title'):
			match += 1
			addItem = {'title': drink.get_text().encode(),'href' : drink.find('a').get('href').encode()}
			obj['article'].append(addItem)

		print match
		time.sleep(1)

	with open('article.json', 'w') as f:
		json.dump(obj,f, ensure_ascii=False,sort_keys = True ,indent = 4)

def 
def spider_for_article(url):

if __name__=='__main__':
    #spider('https://www.douban.com/explore/column/')