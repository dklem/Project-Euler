#!/usr/bin/env python

import operator

x = range(100,0,-1)
y = str(reduce(operator.mul, x))  # Multiply each item in list

sum = 0 
for num in y:
	sum = sum + int(num)
print sum