#!/usr/bin/env python3

import sys

#Author: Omoteniola Sokunbi
#Author ID: 176984219
#Date: 2024/06/05

time = 3 if len(sys.argv) == 1 else int(sys.argv[1])

while time >  0:
    print(time)
    time = time - 1

print ('blast off!')

