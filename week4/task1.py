#!/usr/bin/env
"""
    Week 4 Assignment, task 1

    Write a program that counts down from 10.

    Implement your program first
    with a while loop.

    Now implement your program with a for loop.

    Include both versions in your submission file.

"""
print("countdown loop with while...loop")
n=10
while n>=0:
    print(n)
    n-=1
print("done")

print("countdown loop with for...loop")
for n in range(10,0,-1):
    print(n)
print("done")
