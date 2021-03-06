# Problem Set 2, hangman.py
# Name: Cherif SEYE
# Time spent: ...

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from pyfiglet import *
from termcolor import colored
a = figlet_format('Hangman')
print(colored(a, color="red"))
import random
import string

WORDLIST_FILENAME = "words.txt"
list_ = []
    


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    check = all(letter in letters_guessed for letter in secret_word)
    
    return check





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    list_ = []
    for letters in secret_word:
        list_.append(letters)

    for i in range(len(list_)):
          if list_[i] not in letters_guessed:
            list_[i] = '_'
    return ''.join(list_)          



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    list_3 = []
    string_ = string.ascii_lowercase
    list_2 = list(letters for letters in string_)
    for j in range(len(list_2)):
        if list_2[j] not in letters_guessed:
              list_3.append(list_2[j])
    return ''.join(list_3)          

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    warnings = 3
    guesses_left = 6
    length = len(secret_word)
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(length))
    print('-------------------------------------')
    print(f'you have {guesses_left} guess left')
    letters_guessed = []
    get_guessed_word_ = get_guessed_word(secret_word, letters_guessed)
    available_letters = get_available_letters(letters_guessed)
    print(f'Available letters: {available_letters}')
    score = len(secret_word)
    play = True
    while guesses_left > 0 and get_guessed_word_ != secret_word:
        guess = input("please guess a letter: ")
        guess = guess.lower()
        if guess not in string.ascii_lowercase: 
            warnings -= 1
            print('Oops! That is not a valid letter.You have {} warnings left:'.format(warnings))
            print(f'you have {guesses_left} guess left')
            print('--------------------')

        elif guess in letters_guessed:
           warnings -= 1
           print("Oops! You've already guessed that letter. You have {} warnings left".format(warnings))
           print(f'you have {guesses_left} guess left')
           print('--------------------')

        else:        
            letters_guessed.append(guess)
            get_guessed_word_ = get_guessed_word(secret_word, letters_guessed)
            available_letters = get_available_letters(letters_guessed)
            if guess in secret_word:
                print(f"Good gues: {get_guessed_word_}")
                print(f'you have {guesses_left} guess left')
                print('--------------------')
                print('availableletters: {} '.format(available_letters))
      
            else:
                print(f'Oops! That letter is not in my word: {get_guessed_word_}') 
                if guess in 'aeiou': 
                    guesses_left -= 2
                else:
                    guesses_left -=1       
                print(f'you have {guesses_left} guess left')
                print('--------------------')
                print('availableletters: {} '.format(available_letters))

        if warnings == 0:
            print(f'You got 3 warnings now you you lose 1 guesses') 
            guesses_left -=1
            print(f'you have {guesses_left} guess left')
            print('--------------------')

    if get_guessed_word_ == secret_word:
        message = figlet_format("Congratulations!! 🎉")
        message2 = figlet_format("YOU WON")
        print(colored(message, color="red"))
        print(colored(message2, color='yellow'))
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
        print(f'Your total score for this game is: {guesses_left}')
        print('--------------------')
    else:     
        print("The hidden word was {}".format(secret_word))
        print('--------------------')
            






# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    list_m = list(letter for letter in my_word)
    list_o = list(lettre for lettre in other_word)
    if len(list_m) != len(list_o):
        return False
        
    for i in range(len(list_m)):
        if list_m[i] == '_':
            list_o[i] = '_'
    my_word = ''.join(list_m)
    other_word = ''.join(list_o)

    return my_word == other_word
              




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    list_word = list(letter for letter in my_word)
    list_b = list(i for i in wordlist if len(i) == len(my_word))
    list_c = list()
    for j in list_b:
        k = list(letter for letter in j)
        for l in range(len(k)):
            if list_word[l] == '_':
                k[l] = '_'
            if k == list_word:
              list_c.append(j)
    list__ = []
    for word_ in list_c:
      if word_ not in list__:
        list__.append(word_)          
    return list__        



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guesses_left = 6
    length = len(secret_word)
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(length))
    print('-------------------------------------')
    print(f'you have {guesses_left} guess left')
    letters_guessed = []
    get_guessed_word_ = get_guessed_word(secret_word, letters_guessed)
    available_letters = get_available_letters(letters_guessed)
    print(f'Available letters: {available_letters}')
    score = len(secret_word)
    play = True
    while guesses_left > 0 and get_guessed_word_ != secret_word:
        guess = input("please guess a letter: ")
        guess = guess.lower()
        if guess not in string.ascii_lowercase and guess != '*': 
            warnings -= 1
            print('Oops! That is not a valid letter.You have {} warnings left:'.format(warnings))
            print(f'you have {guesses_left} guess left')
            print('--------------------')

        elif guess in letters_guessed:
           warnings -= 1
           print("Oops! You've already guessed that letter. You have {} warnings left".format(warnings))
           print(f'you have {guesses_left} guess left')
           print('--------------------')

        elif guess == '*':
          list_3 = show_possible_matches(get_guessed_word_)
          string_ = ' '.join(list_3)
          print("Possible word matches are:"
             "\n {} ".format(string_))
          print(f'you have {guesses_left} guess left')
          print('--------------------')
          print('availableletters: {} '.format(available_letters))   

        else:        
            letters_guessed.append(guess)
            get_guessed_word_ = get_guessed_word(secret_word, letters_guessed)
            available_letters = get_available_letters(letters_guessed)
            if guess in secret_word:
                print(f"Good gues: {get_guessed_word_}")
                print(f'you have {guesses_left} guess left')
                print('--------------------')
                print('availableletters: {} '.format(available_letters))
      
            else:
                print(f'Oops! That letter is not in my word: {get_guessed_word_}') 
                if guess in 'aeiou': 
                    guesses_left -= 2
                else:
                    guesses_left -=1       
                print(f'you have {guesses_left} guess left')
                print('--------------------')
                print('availableletters: {} '.format(available_letters))

        if warnings == 0:
            print(f'You got 3 warnings now you you lose 1 guesses') 
            guesses_left -=1
            print(f'you have {guesses_left} guess left')
            print('--------------------')

    if get_guessed_word_ == secret_word:
        message = figlet_format("Congratulations!! 🎉")
        message2 = figlet_format("YOU WON")
        print(colored(message, color="red"))
        print(colored(message2, color='yellow'))
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳"
          "\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
        print(f'Your total score for this game is: {guesses_left}')
    else:
        print("You lost")
        print("🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲"
          "\n🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲"
          "\n🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲"
          "\n🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲"
          "\n🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲"
          "\n🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲🥲")
        print("The hidden word was {}".format(secret_word))
        print('--------------------')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    print(secret_word)
    hangman_with_hints(secret_word)
    
