#!/usr/bin/env python3
import sys
if len(sys.argv) == 2:
    txt = input("What was the parameter? ")
    if txt.strip() == sys.argv[1].strip():
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")