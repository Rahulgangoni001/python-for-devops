# for_loop_practice.py

#numbers = [1, 2, 3, 4, 5]

numbers= input("Enter a list of numbers separated by spaces: ")


# 1. Loop over a list
for number in numbers:
    print(f"Number: {number}")

print()

# 2. Loop with range()
for i in range(1, 6):
    print("*" * i)

print()

# 3. Loop over strings
words = ["apple", "banana", "cherry"]
for word in words:
    print(word.capitalize())

print()

# 4. Nested loops
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()