# Put your code here
from random import randint

print "Hello! What's your name?"

name = raw_input("> ")

number = randint(1, 100)

print "%s, I'm thinking of a number between 1 and 100. \nTry to guess my number." % (name)


num_guesses = 0

guessed = False

while not guessed:
    try:
        guess = int(raw_input(">  "))
        break
    except ValueError:
        print "That's Not even a number! Try Again!"

    num_guesses += 1
    if guess == number:
        print "Congratulations! You guessed the number in %s guesses!" % (num_guesses)
        guessed = True
    elif guess < 1 or guess > 100:
        print "Can't you read?! Guess again, in the range!"
    elif guess < number:
        print "Too Low!"
    elif guess > number:
        print "Too High!"
    else:
        print "Sorry, I don't understand that input!"
