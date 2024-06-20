#!/usr/bin/env python3
"""
"""
import signal
import sys


status_code = [200, 301, 400, 401, 403, 404, 405, 500]
status_dict = {
                "200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0
                }
count = 0

file_size = 0

try:
    for line in sys.stdin:
        print("File size: {}".format(file_size))
        striped = line.split(" ")
        file_size += int(striped[len(striped) - 1])
        status = striped[7]
        for key, value in status_dict.items():
            if status == key:
                status_dict[key] += 1
        for key in status_dict:
            print("{}: {}".format(key, status_dict[key]))

finally:
    print("File size: {}".format(file_size))
    for key in status_dict:
        print("{}: {}".format(key, status_dict[key]))
