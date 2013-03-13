#!/usr/bin/env python

def is_pyt(a, b, c):
	"""Check if satisfies pythagorean theorem"""
	if a**2 + b**2 == c**2:
		return True

for x in range(1,1000):
	for y in range(1,1000):
		z = 1000 - x - y
		if is_pyt(x,y,z):
			print x*y*z