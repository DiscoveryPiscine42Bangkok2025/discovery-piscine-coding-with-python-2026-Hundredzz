#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    print("none")
else:
    first_num = 0
    while first_num <= 10:
        second_num = 0
        print(f"Table de {first_num}:",end=" ")
        while second_num < 10:
            print(second_num * first_num, end=" ")
            second_num += 1
        print(second_num * first_num)
        first_num += 1