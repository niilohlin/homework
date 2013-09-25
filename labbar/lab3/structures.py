#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AbstractStructure:
	def get(self, key):
		pass
	
	def set(self, key, val):
		pass

class MyTlist(AbstractStructure):
	def __init__(self):
		self._mylist = []
		
	@staticmethod
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

	def insert(self, k, v):
		self._mylist = _handle('insert', k, _mylist, v)

	def get(self, k):
		return _handle('get', k, self._mylist)

class MyPlist(AbstractStructure):
	def __init__(self):
		self._a = []
		self._b = []
	
	@staticmethod
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

	def insert(self, k, v):
		"""Insert into parallel list values k for key and v for value"""
		self._a, self._b = _handle('insert', k, self._a, self._b, v)

	def get(self, k):
		"""Return the corresponding element"""
		return _handle('get', k, self._a, self._b)



class MyDlist(AbstractStructure):
	def __init__(self):
		self._dictionary = {}
	
	def insert(self, k, v):
		self._dictionary[k] = v

	def get(self, k):
		return self._dictionary[k]

