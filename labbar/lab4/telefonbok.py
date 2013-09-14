#!/usr/bin/env python
# -*- coding: utf-8 -*-

phonebook = {}
prompt = "phonebook> "

class NoFunction(Exception):
	pass

def parse(text, pbook):
	elements = text.split(' ')
	function = elements[0]
	args = elements[1:len(elements)]
	if not function in ['add', 'alias', 'change', 'save', 'load',
			'lookup', 'save', 'quit']:
		raise NoFunction

	resbook = pbook
	if function == 'add':
		resbook[elements[0]] = elements[1]
		return resbook
	elif function == 'lookup':
		return pbook[elements[0]]
	elif function == 'alias':
		resbook[elements[1]] = pbook[elements[0]]
		return resbook
	elif function == 'change':
		resbook[

def main():
	inp = ''
	while not inp == "quit":
		try:
			inp = raw_input(prompt)
		except(NoFunction):
			print 'no such function'



