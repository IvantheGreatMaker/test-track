#!/usr/bin/env python
# coding: utf-8

# High Low game

# In[1]:


import random
num = random.randrange(0,101)
ll=0
ul=100
guess = input("Guess an integer from 0-100 inclusive:")
guess = int(guess)
while(num != guess):
    if(num>guess):
        ll = guess
        print("You guessed too low the number is between ",ll," and ",ul)
        guess=input("Guess again:")
        guess = int(guess)
    else:
        ul= guess
        print("You guessed too high number is between ",ll," and ",ul)
        guess=input("Guess again:")
        guess = int(guess)
        
print("Congrats the number was ",num)


# In[ ]:





# In[ ]:




