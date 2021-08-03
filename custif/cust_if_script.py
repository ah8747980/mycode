#!/usr/bin/env python3

message = 'You got '

# wrap connection in a float() to accept decimals as numbers
grade = float(input("What is your numerical grade?"))

# if input value was higher or equal to 25
if grade >= 100:
    message = message + 'a perfect score!'
elif grade >= 90:
    message = message + 'an A'
elif grade >= 80:
    message = message + 'a B'
elif grade >= 70:
    message = message + 'a C'
elif grade >= 60:
    message = message + 'a D'
elif grade >= 50:
    message = message + 'an F'
else:
    message = message + 'assignment incomplete'
print(message)


