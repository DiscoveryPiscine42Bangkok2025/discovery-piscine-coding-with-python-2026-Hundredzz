#!/usr/bin/env python3
def main():
    num = int(input("Enter number less than 25\n"))
    if num > 25:
        print("Error")
        return 0
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1

main()
