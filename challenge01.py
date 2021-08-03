#!/usr/bin/python3

#print welcom
print("Test Your Naval History Knowledge")

round = 0
answer = " "

# augment our while condition to test if "Ahoy" or "Shipmate" was the input
# you could reduce the complexity of this conditional with some "break" statements
while round < 3 and (answer != "Ahoy" and answer != "Shipmate"):
    round += 1     # increase the round counter by 1
    answer = input('What was the first USN vessel named after a woman who served in the Navy?').capitalize()

    answer = answer.capitalize() # this line inserted to line 8 will make all
                                 # user input starts with an uppercase
    if answer == "USS Higbee": # logic to check if user gave correct answer
        print("Correct!")
    elif answer == "Ahoy":
        print("You gave the super secret answer!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was USS Higbee.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

