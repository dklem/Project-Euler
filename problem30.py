#!/usr/bin/env python

number = 2
final = []

while number <= 9**5*5:
    full = []
    string_number = str(number)
    for ch in string_number:
        full.append(int(ch)**5)
    if number == sum(full):
        print number
        final.append(number)
    number += 1
print sum(final)