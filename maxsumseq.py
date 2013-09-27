import time
import random


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
			largest = current
	return largest
		
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


