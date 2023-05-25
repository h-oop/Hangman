#hangmannnn wassup

#TO DO LIST
    # 'draw' hangman
        # add parts each incorrect guess
        # maybe have a whole guy drawn out for each thing, and print each for the # of wrongs. position of the list is the # of wrongs, which works with the 0 position. I can use tripple quotes """ey""" to print multiple lines
    #how many wrongs? 6? 7 seems good
#   /¯¯¯¯I
#   |    0(O)
#   |   /|\
#   |    |
#   |   / \
#   ⌈¯¯¯¯¯¯¯¯¯¯⌉
    #option for someone to input a word?
    #set up a game loop

#SETUP THINGS

import random
import os


global score
score = 0

guessed_word = ""
word_list = ['salad bowl', 'gynophobia', 'gentrification','floccinaucinihilipilification','lollypop','woman','gerrymandering','kerfuffle','bequath','gruntled','renography','moist','hippopotamus','washing machine','graphic design','builders league united','peanuts','reliable excavation demolition','d']

HANGMAN = (
  """
  /¯¯¯¯I
  |    
  |    
  |    
  |   
  ⌈¯¯¯¯¯¯¯¯¯¯⌉
  |          |
  """,
  """
  /¯¯¯¯I
  |    O
  |    
  |    
  |   
  ⌈¯¯¯¯¯¯¯¯¯¯⌉
  |          |
  """,
  """
  /¯¯¯¯I
  |    O
  |    |
  |    
  |   
  ⌈¯¯¯¯¯¯¯¯¯¯⌉
  |          |
  """,
  """
  /¯¯¯¯I
  |    O
  |   /|
  |    
  |   
  ⌈¯¯¯¯¯¯¯¯¯¯⌉
  |          |
  """,
  """
  /¯¯¯¯I
  |    O
  |   /|\\
  |    
  |   
  ⌈¯¯¯¯¯¯¯¯¯¯⌉
  |          |
  """,
  """
  /¯¯¯¯I
  |    O
  |   /|\\
  |    |
  |   
  ⌈¯¯¯¯¯¯¯¯¯¯⌉
  |          |
  """,
  """
  /¯¯¯¯I
  |    O
  |   /|\\
  |    |
  |   / 
  ⌈¯¯¯¯¯¯¯¯¯¯⌉
  |          |
  """,
  """
  /¯¯¯¯I
  |    |
  |    0
  |   /|\\
  |    |
  ⌈¯¯|/ \\|¯¯⌉
  |         |
  """
)

####################
def main():
    menu = True
    global word

    while menu:
        print("\nChoose how to play:\n1. ALONE\n2. WITH A FRIEND\n0. QUIT")
        selection = int(input("> "))
        
    #selections
        if selection == 1:
        # SINGLE PLAYER
            word = word_list[random.randrange(0,len(word_list))]

            gamegame()

        elif selection == 2:
        # MULTI PLAYER
            print("PLAYER 1: input a word for player 2 to guess")
            word = input("> ")
            # clears the console so p2 can't see it
            os.system('cls')

            gamegame()

        elif selection == 0:
            print("Thanks for playing!")
            menu = False
        else:
            print("Try again")

    
# PROBLEMS RN:
# 




######################

def censor_word(word):
    guessed = ''
    for letter in word.lower():
        if letter == '\'':
            guessed += '\''
        if letter == ' ':
            guessed += ' '
        else:
            guessed += '_'
    return guessed


def gamegame():
    playing = True
    score = 0
    letters_guessed = []
    guessed_word = censor_word(word)
    
    while playing:
        print(f'LETTERS TRIED:{letters_guessed}')
        print(HANGMAN[score])
        print(guessed_word)
        if score >= 7:
            playing = False
            print(f'You LOST! The word was {word}')
            break
        if guessed_word == word:
            playing = False
            print(f'You won! The word was {word}')
            break   
    
        # ONLY ONE LETTER INPUT
        while True:
            letter = input("Input a letter> ").lower()

            if letter.isalpha() == True and len(letter) == 1:
                print(letter)
                break
            else:
                print('Enter a single letter to continue.')
                continue

        new = ""
        if letter not in letters_guessed:
            letters_guessed.append(letter)
            if letter not in word:
                print("Oops, nope!")
                print(guessed_word)
                score += 1
                for l in range(len(word)):
                    new += guessed_word[l]

                guessed_word = new

            elif letter in word:
                for l in range(len(word)):
                    if letter == word[l]:
                        new += letter
                    else:
                        new += guessed_word[l]
                guessed_word = new


        # if the letter HAS been guessed before
        else:
            print("LETTER HAS BEEN USED, TRY AGAIN")
            for l in range(len(word)):
                new += guessed_word[l]
            guessed_word = new




#ok so the game doesn't like setting the score and stuff I probably shoulda thought abt some of this before defining things willy nilly


main()