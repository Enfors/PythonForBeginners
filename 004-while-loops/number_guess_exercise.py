# Make Python's "random" module available to us
import random

# keep_playing will tell us if the player wants to
# continue or not. For now, let's assume "yes".
keep_playing = "y"

# To allow the player to play many times, we add a
# while loop around the game code itself. Please
# note that this means that all our previous code
# has to be indented another four spaces, to tell
# the computer that it's part of the new while
# loop
while keep_playing == "y":

    max_number = input("Highest number for guess? ")
    max_number = int(max_number)

    # In the random module, there's a function called
    # randint. We can use it to give us any integer
    # from 1 to max_number.
    number = random.randint(1, max_number)

    print(f"I'm thinking of a number between 1 and {max_number}.")
    print("Try to guess which one it is.")

    # Let's give the guess variable a starting number
    # that we know will never be correct.
    guess = 0

    # Keep track of how many guesses the player has used.
    num_guesses = 0

    # Until guess is equal to the number, repeat this
    # loop:
    while guess != number:
        guess = input("What's your guess? ")
        guess = int(guess)  # Convert guess to integer

        # num_guesses += 1 is a shorthand for:
        # num_guesses = num_guesses + 1
        num_guesses += 1

        # Check if it is too low or too high
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")

    # We have now exited the loop, which means that
    # guess must be equal to number, IE, correct.
    print(f"Correct! Well done! It took {num_guesses} guesses.")

    keep_playing = input("Play another (y/n)? ")
