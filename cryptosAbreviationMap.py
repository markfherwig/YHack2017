#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:34:44 2017

@author: markherwig
"""

def crypto_map():
    file = open('crypto_w_abrev.txt')
    full_to_abrev = {}

    for line in file.readlines():
        temp = line.split()
        abbreviation = temp[-1]
        full_name = temp[0]
        for i in range(1, len(temp) - 1):
            full_name += ' ' + temp[i]
        full_to_abrev[full_name] = abbreviation
    return full_to_abrev