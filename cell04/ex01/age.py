def main():
    age = int(input("Please tell me your age: "))
    print("You are currently 15 years old.")
    for i in range(10, 31, 10):
        print(f"In {i} years, you'll be {age + i} years old.")

main()