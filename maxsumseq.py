import time
import random


def quadratic(sequence):
	result = []
	for i in range(len(sequence)):
		for j in range(i,len(sequence) + 1):
			if sum(sequence[i:j]) > sum(result):
				result = sequence[i:j]
	return result

#oops, there is a bug here. [1, 2, 3, -1] is wrong
def linear(sequence):
	current = []
	largest = []
	for i in range(len(sequence)):
		if sum(current) + sequence[i] > 0:
			current.append(sequence[i])
		else:
			current = []
		if sum(current) > sum(largest):
			largest = current
	return largest
		
#############################################
def linearoptimized(arr):
	arrlength = len(arr)
	current = [0] * arrlength
	cindex = 0
	csum = 0
	largest = [0] * arrlength
	lindex = 0
	lsum = 0
	for i in range(arrlength):
		if csum + arr[i] > 0:
			current[cindex] = arr[i]
			cindex += 1
			csum += arr[i]
		else:
			current = [0] * arrlength
			cindex = 0
			csum = 0

		if csum > lsum:
			lsum = csum
			largest = current
	return largest[0:cindex]



#############################################
def stopwatch(f, n=10):
	arr = range(-n, n)
	random.shuffle(arr)
	t = time.time()
	f(arr)
	return time.time() - t

print "quadractic"
for i in range(20):
	print stopwatch(quadratic, n=i*10)
print
print "linear"
for i in range(20):
	print stopwatch(linear, n=i*10)


