#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NegativeError(Exception):
	pass

def sockerkaka(antal):
	"""Printa ett recept pa sockerkaka,
	funkar inte pa negativa tal
	"""

	if antal < 0:
		raise NegativeError

	pers = antal / 4.0

	# int(x + 0.5) avrundar x till narmasta heltal
	print "* %s st ägg" % int(3 * pers + 0.5)
	print "* %s dl strösocker" % (3 * pers)
	print "* %s tsk vaniljsocker" % (2 * pers)
	print "* %s tsk bakpulver" % (2 * pers)
	print "* %s g smör" % (75 * pers)
	print "* %s dl vatten" % pers
	print "* %s dl vetemjöl" % (3 * pers)
	print ""

print "för fyra personer:"
sockerkaka(4)
print "för sju personer:"
sockerkaka(7)
