# Put your code here
from random import randint

print "Hello! What's your name?"

name = raw_input("> ")

number = randint(1, 100)

print "%s, I'm thinking of a number between 1 and 100. \nTry to guess my number." % (name)

guess = raw_input("> ")

num_guesses = 0

guessed = False

#while guessed == False: