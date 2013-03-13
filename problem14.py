#!/usr/bin/env python

# Can definitely improve
# Start from 2, then record results in hash table for each value
# Requires less calculation for the higher numbers, since you can just look up the remaining bits

def process(number):
	"""Process alogrithm"""
	if number % 2 == 0:
		return number / 2
	else:
		return 3 * number + 1

# Initial values
largest = 1

# Start loop

for next in range(1000000,100000,-1):
	count = 1
	initialnext = next
	while next != 1:
		next = process(next)
		count += 1
	if count > largest:
		largest = count
		inext = initialnext

print "Largest Chain: ",
print largest
print "Initial Value: ",
print inext