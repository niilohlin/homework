#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# def _insert(a,b, mylist):
# 	if mylist == []:
# 		mylist.append((a, b))
# 		return mylist
# 	upper = len(mylist)
# 	lower = 0 
# 	while True:
# 		i = (upper + lower) / 2
# 		if mylist[i] < a:
# 			lower = i
# 		elif mylist[i] > a:
# 			upper = i
# 		else:
# 			return mylist
# 
# 		if upper == lower + 1 or upper == lower:
# 			if mylist[i] < a:
# 				mylist.insert(i + 1, (a, b))
# 			else:
# 				mylist.insert(i, (a, b))
# 			return mylist
# 
# def _get(a, mylist):
# 	upper = len(mylist)
# 	lower = 0
# 	while True:
# 		i = (upper + lower) / 2
# 
# 		if mylist[i][0] < a:
# 			lower = i
# 		elif mylist[i][0] > a:
# 			upper = i
# 		else:
# 			return mylist[i][1]

def _handle(option, a, mylist, b=None):
	if option == "insert":
		if mylist == []:
			mylist.append((a, b))
			return mylist
	upper = len(mylist)
	lower = 0
	while True:
		i = (upper + lower) / 2

		if mylist[i][0] < a:
			lower = i
		elif mylist[i][0] > a:
			upper = i
		else:
			if option == "get":
				return mylist[i][1]
			elif option == "insert":
				return mylist

		if option == "insert":

			if upper == lower + 1 or upper == lower:
				if mylist[i][0] < a:
					mylist.insert(i + 1, (a, b))
				else:
					mylist.insert(i, (a, b))
				return mylist

_mylist = []
def insert(k, v):
	global _mylist
	_mylist = _handle('insert', k, _mylist, v)

def get(k):
	global _mylist
	return _handle('get', k, _mylist)

