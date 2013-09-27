import time
import random
import benchmark
import array
import numpy


def quadratic(sequence):
	result = []
	for i in range(len(sequence)):
		for j in range(i,len(sequence) + 1):
			if sum(sequence[i:j]) > sum(result):
				result = sequence[i:j]
	return result

def linear(sequence):
	current = []
	largest = []
	for i in range(len(sequence)):
		if sum(current) + sequence[i] > 0:
			current.append(sequence[i])
		else:
			current = []
		if sum(current) > sum(largest):
			# largest = current; copies the reference
			largest = [i for i in current] 
	return largest
		
#############################################
def part(arr):
	current = []
	largest = [] 
	csum = 0
	lsum = 0
	for i in range(len(arr)):
		a = arr[i]
		if csum + a > 0:
			current.append(a)
			csum += a
		else:
			current = []
			csum = 0
		if csum > lsum:
			largest = [i for i in current]
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
	for i in range(arrlength):
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

# there is another way, with two indexes and a sum



#############################################

class Bmark(benchmark.Benchmark):
	def setUp(self):
		self.n = 500
		self.times = 50
		self.array = []
		random.shuffle(self.array)
				
		
#	def test_quad(self):
#		quadratic(self.array)
		
	def test_part(self):
		for i in range(self.times):
			self.array = range(-self.n, self.n)
			random.shuffle(self.array)
			part(numpy.array(self.array))
		
	def test_linear(self):
		for i in range(self.times):
			self.array = range(-self.n, self.n)
			random.shuffle(self.array)
			#linear(numpy.array(self.array))# reeeeeally slow
			linear(self.array)
	
	def test_opti(self):
		for i in range(self.times):
			self.array = range(-self.n, self.n)
			random.shuffle(self.array)
			linearoptimized(numpy.array(self.array))

if __name__ == '__main__':
	benchmark.main()
