#!/usr/bin/env python3
"""
    Week4 assignment, task 4
    (c) 2021 Sam Caldwell.  All Rights Reserved
"""
for x in range(1,10):
    line=""
    for y in range(1,10):
        a = x * y
        line=f"{line} {a:2}"
    print(line)

