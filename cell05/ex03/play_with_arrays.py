#!/usr/bin/env python3
def main():
    org_arr = [2, 8, 9, 48, 8, 22,-12, 2]
    new_arr = set()
    for i in org_arr:
        if i > 5:
            if i+2 not in new_arr:
                new_arr.add(i+2)
    print(f"{org_arr}\n{new_arr}")

main()
