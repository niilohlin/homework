import time
import random
import benchmark
import array
import numpy


def quadratic(sequence):
	result = []
	for i in xrange(len(sequence)):
		for j in xrange(i,len(sequence) + 1):
			if sum(sequence[i:j]) > sum(result):
				result = sequence[i:j]
	return result

def linear(sequence):
	current = []
	largest = []
	for i in sequence:
		if sum(current) + i > 0:
			current.append(i)
		else:
			current = []
		if sum(current) > sum(largest):
			largest = current[:]
	return largest
		
#############################################

def part(arr):
	current = []
	largest = [] 
	csum = 0
	lsum = 0
	for a in arr:
		if csum + a > 0:
			current.append(a)
			csum += a
		else:
			current = []
			csum = 0
		if csum > lsum:
			largest = current[:]
			lsum = csum
	return largest

def linearoptimized(arr):
	arrlength = len(arr)
	current = numpy.array([0] * arrlength)
	cindex = 0
	csum = 0
	largest = numpy.array([0] * arrlength)
	lindex = 0
	lsum = 0
	for i in xrange(arrlength):
		a = arr[i]
		if csum + a > 0:
			current[cindex] = a
			cindex += 1
			csum += a
		else:
			current.fill(0)
			cindex = 0
			csum = 0

		if csum > lsum:
			lsum = csum
			largest = current.copy()
			lindex = cindex
	return largest[0:lindex]

def uberopti(arr):
	maxsum = 0
	maxbegin = 0
	maxend = 0
	tempsum = 0
	tempbegin = 0
	for end in xrange(len(arr)):
		c = arr[end]
		if tempsum + c > 0:
			tempsum += c
		else:
			tempsum = 0
			tempbegin = end + 1
			
		if tempsum > maxsum:
			maxsum = tempsum
			maxbegin = tempbegin
			maxend = end
	return arr[maxbegin:maxend + 1]



#############################################

class Bmark(benchmark.Benchmark):
	def setUp(self):
		self.n = 10000
		self.times = 50
		self.array = []
		random.shuffle(self.array)
				
		
#	def test_quad(self):
#		quadratic(self.array)
		
	def test_part(self):
		self.array = range(-self.n, self.n)
		random.shuffle(self.array)
		part(self.array)
#		part(numpy.array(self.array))
		
#	def test_linear(self):
#		self.array = range(-self.n, self.n)
#		random.shuffle(self.array)
#		linear(self.array)
	
	def test_uber(self):
		self.array = range(-self.n, self.n)
		random.shuffle(self.array)
		uberopti(self.array)
#	def test_opti(self):
#		for i in xrange(self.times):
#			self.array = range(-self.n, self.n)
#			random.shuffle(self.array)
#			linearoptimized(numpy.array(self.array))
	

if __name__ == '__main__':
	benchmark.main()
