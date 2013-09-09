#!/usr/bin/env python
# -*- coding: utf-8 -*-

phonebook = {}
prompt = "phonebook> "

class NoFunction(Exception):
	pass

def main():
	inp = ''
	while not inp == "quit":
		try:
			inp = raw_input(prompt)
			elements = inp.split(' ')
			function = elements[0]
			args = elements[1:len(elements)]
			if not function in ['add', 'alias', 'change', 'save', 'load',
					'lookup', 'save', 'quit']:
				raise NoFunction
			if function == 'add':
				phonebook[elements[0]] = elements[1]
			elif function == 'lookup':
				print phonebook[elements[0]]
			elif function == '
		except(NoFunction):
			print 'no such function'



