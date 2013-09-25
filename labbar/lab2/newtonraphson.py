#!/usr/bin/env python
# -*- coding: ascii -*-

def derivative(f, x, h):
	return (f(x + h) - f(x - h)) / (2 * h)

def _almost_equal(a, b, h):
	if abs(a - b) < h:
		return True
	else:
		return False

def solve(f, x, h):
	old_x = x
	while not _almost_equal(f(x), 0, h):
		try:
			x = x - f(x) / derivative(f, x, h)
		except:
			print "oops, division by zero"
			print "x were %s. and f'(x) were %s" %(x, derivative(f, x, h))
			break
		if _almost_equal(x, old_x, h):
			return x
	return x



