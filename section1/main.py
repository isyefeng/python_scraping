#!/usr/bin/env python3
'''scraping project'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

urlname = 'http://pythonscraping.com/pages/page1.html'
urlname1 = 'http://www.pythonscraping.com/pages/page1.html'

'''
html = urlopen(urlname1)
''''''html.parser 是一个解析器名字，BeautifulSoup方法的第一个参数是html文件/内容
第二个参数是解析器类型''''''
bs = BeautifulSoup(html, 'html.parser')

#print(html.read())
print(bs.h1)

'''

'''获取标签'''
def GetTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		print('No find this url')
		return None
	try:
		bs = BeautifulSoup(html, 'html.parser')
		title = bs.body.h1
	except AttributeError as e:
		print(e)
		return None
	return title
	
title = GetTitle(urlname1)
if title == None:
	print('No title')
else:
	print(title)

