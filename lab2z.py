#!/usr/bin/env python3
import sys

# Check if exactly 2 arguments are provided
#if len(sys.argv) == 0:
   # print(f"Usage: {sys.argv[0]} <name> <age>")
    #sys.exit(1)

if len(sys.argv) <= 2:
    print(f"Usage: {sys.argv[0]} <name> <age>")
    sys.exit(1)

# Assign the first argument (sys.argv[1]) to the string object 'name'
name = sys.argv[1]

# Assign the second argument (sys.argv[2]) to the integer object 'age'
age = sys.argv[2]

# Print the exact output
print(f"Name: {name}\nAge: {age}")

