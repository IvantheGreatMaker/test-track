#!/usr/bin/env python
# coding: utf-8

# importing needed libaries
import random
num = random.randrange(0,101) #Created the random number to test
ll=0 #set the lower limit for the range
ul=100 #set the upper limit for the range
guess = input("Guess an integer from 0-100 inclusive:") #prompt for number, this will be a string
guess = int(guess) #converting string to int
while(num != guess): #condition to keep guessing
    if(num>guess): #if the guess is less than the number 
        ll = guess #set the lower limit to the guess
        print("You guessed too low the number is between ",ll," and ",ul) #telling user of new range
        guess=input("Guess again:") #collecting the new response as a string
        guess = int(guess) #converting the string to an int
    else: #the guess has to be more than the number due to it not being equal or less than the guess.
        ul= guess #setting the upper limit to the gues
        print("You guessed too high number is between ",ll," and ",ul)  #telling user of new range
        guess=input("Guess again:") #collecting the new response as a string
        guess = int(guess) #converting the string to an int
        
print("Congrats the number was ",num) #telling user that their guess is correct and ending the program
