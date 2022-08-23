# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


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
    L=list(secret_word)
    SL=[]
    for i in L:
        if i not in SL:
            SL.append(i)

    if sorted(SL)==sorted(letters_guessed):
        return True
    else:
        return False
    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    ls=[]
    L=list(secret_word)
    for i in L:
        if i in letters_guessed:
            ls.append(i)
        else:
            ls.append("_")
    return ls



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters 
        have not yet been guessed.
    '''
    alpha=list("abcdefghijklmnopqrstuvwxyz")
    for char in letters_guessed:
        if char.isalpha()==True:
            alpha.remove(char)
    return alpha

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, lets the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user starts with 6 guesses

    * Before each round, displays to the user how many guesses
      s/he is left with and the letters that the user has not yet guessed.
    
    * Asks the user to supply one guess per round. Makes
      sure that the user puts in a letter!
    
    * The user receives feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, displays to the user the 
      partially guessed word so far.
    
    '''
    letters_guessed=[]
    L=list(secret_word)
    count=0
    while count<6:
        s=get_guessed_word(secret_word,letters_guessed)
        print(s)
        print("You have", 6-count, "guesses left")
        print("Letters that you haven't guessed are...", 
              get_available_letters(letters_guessed))
        g= input("Enter your guess:")
        x=0
        letters_guessed.append(g)
        if g in L:
            for char in L:
                if char==g:
                    s[x]==g
                    print("Correct!")
                x=x+1
        else:
            print("Wrong!")
            count=count+1
        if is_word_guessed(secret_word,letters_guessed)==True:
            print("Yayyy! You won.")
            break


    if count==6:
        print("Sorry... You lost. Better luck next time!")  
    print ("The word was...", secret_word)
            


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    a=list(my_word)
    b=list(other_word)
    if len(a)==len(b):
        for i in range(len(a)):
            if a[i].isalpha()== True:
                if a[i]!=b[i]:
                    return False
                
    else:
        return False
    return True
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word

    '''
    L=[]
    for word in wordlist:
        if match_with_gaps(my_word, word)== True:
            L.append(word)
    return L



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, lets the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user starts with 6 guesses
    
    * Before each round, displays to the user how many guesses
      s/he is left with and the letters that the user has not yet guessed.
    
    * Asks the user to supply one guess per round. Makes sure to check that the user 
      guesses a letter
      
    * The user receives feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, displays to the user the partially guessed word so far.
      
    * If the guess is the symbol *, prints out all words in wordlist that
      matches the current guessed word. 

    '''
    letters_guessed=[]
    L=list(secret_word)
    count=0
    while count<6:
        s=get_guessed_word(secret_word,letters_guessed)
        print(s)
        print("You have", 6-count, "guesses left")
        print("Letters that you haven't guessed are...", 
              get_available_letters(letters_guessed))
        g= input("Enter your guess:")
        x=0
        letters_guessed.append(g)
        if g in L:
            for char in L:
                if char==g:
                    s[x]==g
                    print("Correct!")
                x=x+1
        elif g=="*":
            p=show_possible_matches(''.join(s))
            print(''.join(s))
            print(p)
        else:
            print("Wrong!")
            count=count+1
        if is_word_guessed(secret_word,letters_guessed)==True:
            print("Yayyy! You won.")
            break


    if count==6:
        print("Sorry... You lost. Better luck next time!")  
    print ("The word was...", secret_word)



if __name__ == "__main__":   
    secret_word = choose_word(wordlist)
    opt = input("Do you want to play hangman with hints? (y/n): ")
    if opt == "y":
        hangman_with_hints(secret_word)
    elif opt == "n":
        hangman(secret_word)
    else:
        print("Invalid input")
