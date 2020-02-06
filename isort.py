import time
import random
import matplotlib.pyplot as plt

record = []
nums = []

def insertionSort1():

	tstart = time.time()
	n = 10
	randomer = random.sample(range(0, n), n)

	for i in range(1,n):
		current_value = randomer[i]
		pos = i
		while pos>0 and randomer[pos-1]>current_value:
			randomer[pos]=randomer[pos-1]
			pos = pos-1

		randomer[pos] = current_value

	print(randomer)
	tend = time.time()

	timelapse = tend-tstart
	print("Runtime:",timelapse)
	nums.append(n)
	record.append(timelapse)

insertionSort1()

def insertionSort2():

	tstart = time.time()
	n = 100
	randomer = random.sample(range(0, n), n)

	for i in range(1,n):
		current_value = randomer[i]
		pos = i
		while pos>0 and randomer[pos-1]>current_value:
			randomer[pos]=randomer[pos-1]
			pos = pos-1

		randomer[pos] = current_value

	print(randomer)
	tend = time.time()

	timelapse = tend-tstart
	print("Runtime:",timelapse)
	nums.append(n)
	record.append(timelapse)

insertionSort2()

def insertionSort3():

	tstart = time.time()
	n = 1000
	randomer = random.sample(range(0, n), n)

	for i in range(1,n):
		current_value = randomer[i]
		pos = i
		while pos>0 and randomer[pos-1]>current_value:
			randomer[pos]=randomer[pos-1]
			pos = pos-1

		randomer[pos] = current_value

	print(randomer)
	tend = time.time()

	timelapse = tend-tstart
	print("Runtime:",timelapse)
	nums.append(n)
	record.append(timelapse)

insertionSort3()

def insertionSort4():

	tstart = time.time()
	n = 10000
	randomer = random.sample(range(0, n), n)

	for i in range(1,n):
		current_value = randomer[i]
		pos = i
		while pos>0 and randomer[pos-1]>current_value:
			randomer[pos]=randomer[pos-1]
			pos = pos-1

		randomer[pos] = current_value

	print(randomer)
	tend = time.time()

	timelapse = tend-tstart
	print("Runtime:",timelapse)
	nums.append(n)
	record.append(timelapse)

insertionSort4()

print(nums)
print(record)

plt.plot(nums,record, 'ro')
plt.axis([0, 10000, 0, 20])
plt.ylabel('Insertion Sort')
plt.show()