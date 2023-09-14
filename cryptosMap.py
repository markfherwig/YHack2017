#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:34:44 2017

@author: markherwig
"""


file = open('crypto_w_abrev.txt')
full_to_abrev = {}

for line in file.readlines():
    temp = line.split()
    abbreviation = temp[-1]
    full_name = ''
    for i in range(len(temp) - 1):
        full_name += temp[i]
    full_to_abrev[full_name] = abbreviation
print(full_to_abrev)