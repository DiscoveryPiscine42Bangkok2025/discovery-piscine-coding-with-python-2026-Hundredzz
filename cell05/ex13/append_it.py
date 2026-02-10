#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    argu = sys.argv[1:]
    for i in argu:
        if not i.endswith("ism"):
            print(i + "ism")
else:
    print("none")