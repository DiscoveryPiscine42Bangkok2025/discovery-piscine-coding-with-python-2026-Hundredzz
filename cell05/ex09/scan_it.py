#!/usr/bin/env python3
import sys
import re
if len(sys.argv) == 3:
    x = re.findall(sys.argv[1],sys.argv[2])
    if x:
        print(len(x))
    else:
        print("none")
else:
    print("none")