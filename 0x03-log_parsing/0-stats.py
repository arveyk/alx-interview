#!/usr/bin/python3
"""
Log parsing module, processing of inputs from command line
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
interrupt = False
file_size = 0


def is_number(string: str) -> bool:
    """Function to check is a string can be converted to a number
    Args:
        string: the string to be checked
    Returns: True if yes, False if it cannot be conveted
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


try:
    for line in sys.stdin:
        striped = line.split(" ")
        file_s = striped[len(striped) - 1]
        # print("True or False\t{}, \t {}".format(is_number(file_s), file_s))
        if is_number(file_s) is True:
            file_size += int(file_s)
        print("File size: {}".format(file_size))
        status = striped[len(striped) - 2]
        for key, value in status_dict.items():
            if status == key:
                status_dict[key] += 1
        for key in status_dict:
            if status_dict[key] == 0:
                continue
            print("{}: {}".format(key, status_dict[key]))

except KeyboardInterrupt as e:
    print(e)
    """
    print("File size: {}".format(file_size))
    for key in status_dict:
        if status_dict[key] == 0:
            continue
        print("{}: {}".format(key, status_dict[key]))
        """
"""
finally:
    print("File size: {}".format(file_size))
    for key in status_dict:
        if status_dict[key] == 0:
            continue
        print("{}: {}".format(key, status_dict[key]))
"""
