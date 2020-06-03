#!/usr/bin/env python3

import string

def print_rangoli(size):
    if size == 1:
        print ("a")
    else:
        inc = 1
        i = 1
        while i > 0:
            centre = (size-1)*2
            for j in range (0, centre):
                delta = ((size)*2-i*2)-j
                if (delta%2 == 0 and j > centre-2*i):
                    print(string.ascii_lowercase[2*size-1-(j//2)-i], end="")
                else:
                    print("-", end="")
            print(string.ascii_lowercase[size-i], end="")
            for j in range (centre-1, -1, -1):
                delta = ((size)*2-i*2)-j
                if (delta%2 == 0 and j > centre-2*i):
                    print(string.ascii_lowercase[2*size-1-(j//2)-i], end="")
                else:
                    print("-", end="")
            print()
            i += inc
            if i == size:
                inc = -1

print_rangoli(26)
