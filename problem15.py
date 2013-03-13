#!/usr/bin/env python

import operator

n = reduce(operator.mul, range(1,41))
m = reduce(operator.mul, range(1,21))

print n / (m*m)
