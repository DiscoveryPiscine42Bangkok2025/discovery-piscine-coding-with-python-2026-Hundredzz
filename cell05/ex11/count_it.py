#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    argu = sys.argv[1:]
    print(f"parameters: {len(argu)}")
    for i in argu:
        print(f"{i.strip()}: {len(i.strip())}")
else:
    print("none")