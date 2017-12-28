# encoding=utf8

import requests
import json
from bs4 import BeautifulSoup
import time
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",}

data={
    'redir': 'https://www.douban.com',
    'form_email':'runnan1998@gmail.com',
    'form_password':'caonannan1004',
    'login':u'登录'
}

proxies = {
  "http": "http://176.122.182.43:443"
}

# the function need to be improved with login, otherwise we can only access one web at one time
def spider_for_url(url):
	# intialize json format for obj
	obj = {}
	obj['article'] = []

	 # for different category
	for i in range(12,13):
		match = 0
		url = url + str(i) 
		r = requests.get(url,headers=headers) 

		soup = BeautifulSoup(r.text, "html.parser")
		#print soup.prettify()

		# search for each candidate url, add to obj
		for drink in soup.select('.title'):
			match += 1
			addItem = {'title': drink.get_text().encode(),'href' : drink.find('a').get('href').encode()}
			obj['article'].append(addItem)

		#print match
		time.sleep(1) # to avoid being detected as a spider

	# save in .json
	with open('test.json', 'w') as f:
		json.dump(obj,f, ensure_ascii=False,sort_keys = True ,indent = 4)

# the function is not effective 
def login():
	url =  'https://accounts.douban.com/login'
	r = requests.post(url, data, headers=headers) #request with password
	page = r.text

	soup = BeautifulSoup(page,"html.parser")

	# for certidication photo, input by hand
	captcha_url = soup.find('img',id='captcha_image')['src'] 
	pattern = re.compile('<input type="hidden" name="captcha-id" value="(.*?)"/')
	captcha_id = re.findall(pattern, page)
	urllib.urlretrieve(captcha_url,"captcha.jpg")
	captcha = raw_input('please input the captcha:')

    # request with password and certificatation number
	data['captcha-solution'] = captcha
	data['captcha-id'] = captcha_id
	r = requests.post(url, data=data, headers=headers)

def url_scan():
	i = 1
	# read the json with url information to url_list
	with open('test.json','r') as f:
		url_list = json.load(f)

	#list_i = 100
	for url in url_list:
		#print url['href']s
		print i
		i = i + 1
		spider_for_article(url['href'],i)
		time.sleep(1)

	with open('article.json','r') as f:
		url_list = json.load(f)

	#list_i = 100
	for url in url_list:
		#print url['href']s
		print i
		i = i + 1
		spider_for_article(url['href'],i)
		time.sleep(1)
	#print i

def spider_for_article(url,i):

	# request and get the page
	r = requests.get(url, headers=headers,proxies=proxies)
	soup = BeautifulSoup(r.text,"html.parser")
	#print soup.prettify()

	# filename for save the content of the url i in i.txt 
	i_str=str(i) 
	filename=i_str+'.txt'
	f=open(filename,'w')

	# resolve it and save 
	for drink in soup.select('.note-container'):
		for par in drink.select('p'):
			string = unicode(par.string)	
			if(string != "None"):
				f.write(string+"\n")
	f.close()
	#print text.decoding(decode('utf-8'))

if __name__=='__main__':
	#login()
	#spider_for_url('https://www.douban.com/explore/column/')
	url_scan()
	#spider_for_article('https://www.douban.com/note/650521941/',1)




