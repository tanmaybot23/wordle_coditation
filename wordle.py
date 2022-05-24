import os
import sys
import random
import colorama
from colorama import Fore, Back, Style
import re

l_word = []
w_set = set(())

def random_Word(): 
    file = open(os.path.join(sys.path[0], 'sgb-words.txt'), 'r')
    for line in file:
            l_word.append(line[:-1])
            w_set.add(line[:-1])

    file.close()
    random_index = random.randint(0, len(l_word) - 1)
    return(l_word[random_index])

#generating random word
word = random_Word()

#initialize chances
count = 6

#command line colour for windows initialize
colorama.init(autoreset=True)

def validing_Input(guess):
    #validate no special character, numbers and word present in the file
    if re.match("^[a-z]{5}$", guess):
        if guess in w_set:
            return True
        else:
            print("Word is not present in the file!")

    return False


while True:
    if count == 0:
        print('lost. Better luck next time!')
        print('The word is ', word)
        break
    
    #list of all characters index at correct index 
    correctIndex = [] 
    #list of all characters index at wrong index 
    wrongIndex = [] 
    print('Total chances left: ', count)
    guess = input('Guess the 5 letter word: ')
    guess = guess.lower()

    if guess == word:
        print(Back.GREEN + word)
        print('Congo you won')
        break
    elif validing_Input(guess):
        for i in range(len(guess)):
            if guess[i] in word and guess[i] == word[i]:
                correctIndex.append(i)
            elif guess[i] in word:
                wrongIndex.append(i)

        for i in range(len(guess)):
            if i in correctIndex:
                print(Back.GREEN + guess[i], end='')
            elif i in wrongIndex:
                print(Back.YELLOW + guess[i], end='')
            else:
                print(guess[i], end='')

        print('')
        count = count - 1

    else:
        print('Give a 5 letter word.')
