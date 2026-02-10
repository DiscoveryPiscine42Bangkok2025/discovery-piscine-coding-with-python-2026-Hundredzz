#!/usr/bin/env python3
import sys
def shrink(txt:str):
    print(txt[:8])

def enlarge(txt:str):
    print(txt + ("Z" * (8-len(txt))))

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        if len(i)< 8:
            enlarge(i)
        elif len(i) > 8:
            shrink(i)
        else:
            print(i)
else:
    print("none")