#!/usr/bin/env python
# -*- coding: ascii -*-

# This function is tail call optimized
def digit_sum(n, acc=0):
	"""Return the digit sum of a number"""
	if n == 0:
		return acc
	else:
		return digit_sum(n / 10, acc + n % 10)

def digit_sum2(n):
	s = 0
	while n != 0:
		s += n % 10
		n = n / 10
	return s

