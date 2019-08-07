#!/usr/bin/env python3
'''scraping project'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError,URLError
import re

urlname = 'http://pythonscraping.com/pages/page1.html'
urlname1 = 'http://www.pythonscraping.com/pages/page1.html'
bjpk10 = 'https://www.cjcp.com.cn/kaijiang/bjpk10/'
shopping = 'http://www.pythonscraping.com/pages/page3.html'

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
	
def GetHtmlCode(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		print('No find this url')
		return None
	except URLError:
		return None
	return html
	
def GetTagTree(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		print('No find this url')
		return None
	except URLError:
		return None
	
	bs = BeautifulSoup(html, 'html.parser')
	return bs
	
	
	
#title = GetTitle(urlname1)
#title = GetHtmlCode(bjpk10)
#tagtree = GetTagTree(urlname)
shopping_tree = GetTagTree(shopping)
#print(shopping_tree)


#保存到txt文件
html_name = 'html.html'
with open(html_name, 'w') as file_t:
	file_t.write(str(shopping_tree))



'''
print(shopping_tree.h1.get_text())
bs_tag = shopping_tree.find_all('sapn',{'calss':'green'})
ba_tag = shopping_tree.find(text='Totally Normal Gifts')
th_tag = shopping_tree.find_all(id = 'giftList')


print('bs_tag info:' + str(ba_tag))
print(bs_tag)
'''

#print(tagtree)
'''
if title == None:
	print('No title')
else:
	print(title)
'''

#使用正则表达式来查找图片
regexs = shopping_tree.find_all('img', {'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for regex in regexs:
	print(regex['src'])
	
print(regexs)







