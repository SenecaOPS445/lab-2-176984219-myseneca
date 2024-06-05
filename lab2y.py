#!/usr/bin/env python3
# Author: Microsoft Copilot
# Author ID: copilot
# Date Created: 2024/06/04

import sys

# Assign the value 3 to the timer if no arguments are provided
timer = 3 if len(sys.argv) == 1 else int(sys.argv[1])

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

# Print the final blast off message
print("blast off!")

