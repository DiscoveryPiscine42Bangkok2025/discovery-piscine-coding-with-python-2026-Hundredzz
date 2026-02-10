#!/usr/bin/env python3
import sys
import re
if len(sys.argv) == 2:
    argu = re.findall("z", sys.argv[1])
    if argu:
        for i in argu:
            print(i, end="")
    else:
        print("none")
else:
    print("none")