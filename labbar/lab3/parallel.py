#!/usr/bin/env python
# -*- coding: utf-8 -*-
#######################
# This prorgam takes advantage of two parallel lists with 
# corresponding elements. It searches and inserts using a binary
# search  function
######################

# Change this so has the same functionality as the other ones

def _handle(option, a, alist, blist=None, b=None):
	if option == "insert":
		if alist == [] or blist == []:
			alist.append(a)
			blist.append(b)
			return (alist, blist)


	upper = len(alist)
	lower = 0
	while True:
		i = (upper + lower) / 2
		
		if alist[i] < a:
			lower = i
		elif alist[i] > a:
			upper = i
		else:
			if option == "insert":
				return (alist, blist)
			elif option == 'get':
				return blist[i]

		if option == 'insert':
		
			if upper == lower + 1 or upper == lower:
				if alist[i] < a:
					alist.insert(i + 1, a)
					blist.insert(i + 1, b)
				else:
					alist.insert(i, a)
					blist.insert(i, b)
				return (alist, blist)




def _sort(alist, blist):
	"""Assume that alist and blist already has corresponding
	elements, then sort after alist
	"""
	ares, bres = [], []
	for i in range(len(alist)):
		ares, bres = insert(alist[i], ares, blist[i], bres)
	return (ares, bres)

#############################################################
_a = []
_b = []
# 
# def insert(k, v):
# 	global _a, _b
# 	_a, _b = _insert(k, _a, v, _b)
# 
# def get(k):
# 	global _a, _b
# 	return _get_from(k, _a, _b)
# 
def insert(k, v):
	"""Insert into parallel list values k for key and v for value"""
	global _a, _b
	_a, _b = _handle('insert', k, _a, _b, v)

def get(k):
	"""Return the corresponding element"""
	global _a, _b
	return _handle('get', k, _a, _b)

if __name__ == "__main__":
	print "you can't run a library directly"
