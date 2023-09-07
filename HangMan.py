# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import random

def select_word():
    seriously = ["dick", "john", "thomas", "penis", "fallous", "phallous"]
    choice = random.choice(seriously)
    #print("random item from list is: ", choice)
    return choice.lower()


def guess():
     letter = input("Please enter a letter ==>  ").lower()
     if len(letter)!=1:
         print("You have entered an invalid response")
         letter = guess()
     if letter.isnumeric():
         print("You have entered an invalid response")
         letter = guess()
         
     return letter
 
def check(word,letter):
    if word.find(letter)!=-1:
        correct(word, letter)
    else:
        incorrect()
        
        

def correct(word, letter):
    print("You have guessed correctly")
    for i,c in zip(range(len(word)), word):
        if c == letter:
            found[i]= True
            
def incorrect():
    print("You have guessed incorrectly, please try again")
    global wrong_guess
    wrong_guess += 1
    
def endgame():
    cont = True
    if wrong_guess >= limit:
        cont = False
        print("You have lost this game! The word was " + word)
    elif all(found):
        cont = False
        print ("Congrats you have won this game!")
    return cont
        
def print_res(found, word):
    prt_str = ""
    for f, c in zip(found, word):
        if f:
            prt_str += c +" "
            
        else:
           prt_str += "_ " 
    print(prt_str)
    print("You have " + str(limit - wrong_guess) + " wrong attempts left.")
            
    
limit = 8
wrong_guess = 0
word = select_word()    
found = [False for letter in word]
print_res(found, word)


cont = True
while cont:
    letter = guess()
    check(word,letter)
    print_res(found, word)
    cont = endgame()
    
