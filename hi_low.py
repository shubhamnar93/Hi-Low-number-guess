import os
import random
from hi_low_art import logo
Score=0
def number_hidden():
    number= random.randint(1,100)
    return number
def number_check(Score):
    os.system('cls')
    number_shown=random.randint(1,100)
    print(logo)
    print (f"score: {Score}")
    print(f"number: {number_shown}")
    guess= input("guess next number will be high or low and type 'hi' or 'low': ")
    num=number_hidden()
    if guess=="hi" and number_shown<num:
       Score+=1
       number_shown=num
       number_check(Score)
    elif guess=="low" and number_shown>num:
       Score+=1
       number_shown=num
       number_check(Score)
    else:
        print(f"your final score is {Score}")
while input("do you want to play 'y' for yes and 'n' for no: ")=='y':
   number_check(Score)
