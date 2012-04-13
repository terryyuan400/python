#!/usr/bin/python

number = 23
guess = int(raw_input("Enter an integer:"))

if guess == number:
    print "you guess it."
elif guess < number:
    print "higer"
else:
    print "lower"

print "Done"
