#!/usr/bin/env python

number = 2**1000

total = 0
for x in str(number):
	total = total + int(x)
print total