#!/usr/bin/python3
"""
Main Test file
"""

minOperations = __import__('0-minoperations').minOperations

n = 19170307
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
