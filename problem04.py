#!/usr/bin/env python

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]

big_a, big_b, max_seen = 0, 0, 0

for a in range(999, 99, -1):
	for b in range(a, 99, -1):
		if a * b < max_seen: continue
		if is_palindrome(a * b):
			big_a, big_b, max_seen = a, b, a * b
print big_a,big_b,max_seen 