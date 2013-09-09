#!/usr/bin/env python
# -*- coding: ascii -*-

class NegativeException(Exception):
	pass

def bounce(a, b=0):
	if a < 0:
		raise NegativeException

	print(abs(a - b))
	if 2 * a == b:
		return
	else:
		bounce(a, b + 1)

def bounce2(a):
	for i in xrange(-a, a + 1):
		print abs(i)

