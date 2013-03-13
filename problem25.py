#!/usr/bin/env python

a, b, count = 1, 1, 2

while True:
	count += 1
	a, b = b, a + b
	# print a, b, count
	if len(str(b)) > 999:
		print count
		break