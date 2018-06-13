###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:
import random
digits = list(range(10))
random.shuffle(digits)
code = digits[:3]
print("Code has been genreated, please guess a 3 digit number.")

code_matched = False
while not code_matched:
    guess = list(map(int,[char for char in input("What is your guess?")]))
    # Think about how you will compare the input to the random number, what format
    # should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
    while len(guess) != 3:
        print("Guess must be three digits long.")
        guess = list(map(int,list(input("What is your guess?"))))
    digits_matched = 0
    for code_digit, guess_digit in zip(code, guess):
        if guess_digit == code_digit:
            digits_matched +=1
            print("Match")
        elif guess_digit in code:
            print("Close")
        else:
            print("Nope")
    if digits_matched == 3:
        code_matched = True
print("Thanks for playing!")
