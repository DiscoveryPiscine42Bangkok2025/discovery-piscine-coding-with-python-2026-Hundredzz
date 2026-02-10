#!/usr/bin/env python3
import sys
if len(sys.argv) == 3:
    arr = list(range(int(sys.argv[1]), int(sys.argv[2])+1))
    print(arr)
else:
    print("none")