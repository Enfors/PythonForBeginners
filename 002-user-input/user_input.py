# Example of how to get user input from keyboard
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you!")

age = input("How old are you? ")
# Use int() function to convert input to integer
age = int(age)  # age = int(input(...)) works too
print(f"Oh I see, you're {age} years old.")
