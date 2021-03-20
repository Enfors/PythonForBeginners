# Make Python's "random" module available to us
import random

# In the random module, there's a function called
# randint. We can use it to give us any integer
# from 1 to 100.
number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")
print("Try to guess which one it is.")

# Let's give the guess variable a starting number
# that we know will never be correct.
guess = 0

# Until guess is equal to the number, repeat this
# loop:
while guess != number:
    guess = input("What's your guess? ")
    guess = int(guess)  # Convert guess to integer

    # Check if it is too low or too high
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")

# We have now exited the loop, which means that
# guess must be equal to number, IE, correct.
print("Correct! Well done!")
