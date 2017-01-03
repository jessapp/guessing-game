# Put your code here
from random import randint

print "Hello! What's your name?"

name = raw_input("> ")

play_again = True

best_score = 100

while play_again == True:
    number = randint(1, 100)

    print "%s, I'm thinking of a number between 1 and 100. \nTry to guess my number." % (name)

    num_guesses = 0

    guessed = False

    while not guessed:
        try:
            guess = int(raw_input(">  "))
        except ValueError:
            print "That's not a valid number! Try Again! (Hint: is it a decimal? I don't like decimals.)"
            continue

        num_guesses += 1
        if guess == number:
            print "Congratulations! You guessed the number in %s guesses!" % (num_guesses)
            guessed = True
            if num_guesses < best_score:
                best_score = num_guesses
                print "This is your best score yet!"
            else:
                print "Your best score so far is %s" % (best_score)

            print "Would you like to play again?"
            play_again = raw_input("Y or N: ").upper()
            if play_again == "Y":
                play_again = True
            elif play_again == "N":
                play_again = False
            else:
                print "That's not a valid answer! Try again."
        elif guess < 1 or guess > 100:
            print "Can't you read?! Guess again, in the range!"
        elif guess < number:
            print "Too Low!"
        elif guess > number:
            print "Too High!"
        else:
            print "Sorry, I don't understand that input!"
   