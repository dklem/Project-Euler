#!/usr/bin/env python


fib = []
a, b = 0, 1
while b <= 4000000:
	if b % 2 == 0:
		fib.append(b)
	a, b = b, a + b
print sum(fib)