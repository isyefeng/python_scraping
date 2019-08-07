#!/usr/bin/env python3
'''rexge test'''
import re

def QQ_login():
	name = input('plasere input your QQ number:')
	flag = re.match('[0-9]{1,12}$',name)
	if not flag:
		print('please input correct QQ number!')
	else:
		password = input('plasere input your password:')
		flag = re.match('[A-Z].*\.*',password)
		if not flag:
			print('plasere input correct password!')
		else:
			print('login succeed')


QQ_login()
