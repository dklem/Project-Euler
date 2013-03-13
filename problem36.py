#!/usr/bin/env python

def is_pal(number):
    string_number = str(number)
    return (string_number == string_number[::-1])

def dec2bin(n):
    s = ''
    while n:
        s = str(n % 2) + s
        n = n / 2
    return s

decimal = 1
palindromes = []
while decimal < 1000000:
    binary = dec2bin(decimal)
    if is_pal(decimal) & is_pal(binary):
        print decimal,
        print binary
        palindromes.append(decimal) 
    decimal += 1

print sum(palindromes)