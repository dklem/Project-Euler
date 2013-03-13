#!/usr/bin/env python

import re

names = open('names.txt').read().split(',')
names.sort()



abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
value = {}
start = 1

for letter in str(abc):
	value[letter] = start
	start += 1


position = 1
grandTotal = 0

for name in names:
	nameTotal = 0
	for letter in name:
		if letter != "\"":
			nameTotal += value[letter]
	grandTotal += nameTotal*position
	position += 1
print grandTotal