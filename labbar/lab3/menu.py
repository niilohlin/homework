#!/usr/bin/env python
# -*- coding: utf-8
import structures

def main():
	print "0) Parallel lists"
	print "1) Tuple lists"
	print "2) Dictionary"
	print ""
	data = -1
	while not data in range(3):
		data = int(raw_input("choose datastructure: "))
	
	if data == 0:
		data_structure = structures.MyPlist()
	elif data == 1:
		data_structure = structures.MyTlist()
	else:
		data_structure = structures.MyDlist()

	mode = -1
	while not mode in range(3):
		while not mode == 2:

			print "0) Insert"
			print "1) Lookup"
			print "2) Exit"
			print ""

			mode = int(raw_input("choose alternative: "))
			
			
			if mode == 0:
				k = raw_input("word to insert: ")
				v = raw_input("description for %s: " % k)
				data_structure.insert(k, v)
			elif mode == 1:
				k = raw_input("Word to lookup: ")
				print "description for %s: %s" % (k, data_structure.get(k))
				print

if __name__ == '__main__':
	main()



