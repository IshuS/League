#!/usr/bin/python

from random import *
import sys

flag = [1]
team = [[0.75, 0.5], [0.75, 0.5], [0.75, 0.5], [0.75, 0.5], [0.75, 0.5], \
[0.75, 0.5], [0.75, 0.5], [0.75, 0.5], [0.75, 0.5], [0.75, 0.5], [0.75, 0.5], \
[0.75, 0.5], [0.75, 0.5], [0.75, 0.5], [0.75, 0.5], [0.75, 0.5]]

def match(a_in, b_in):
    a = randint(0, 100 * float(team[int(a_in)][0]))
    b = randint(0, 100 * float(team[int(b_in)][1]))
    return a,b

if __name__ == "__main__":
    while int(flag[0]):
        try:
            flag = raw_input().split(' ')
            print flag[1], flag[2], match(flag[1], flag[2])
        except Exception as e:
            print 'Exception raised: ', e
            
