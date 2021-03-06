import random
import string

WORDLIST_FILENAME = "words.txt"
MAXIMUM_GUESSES = 8

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print 'Loading word list from file...'
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print '  ', len(wordlist), 'words loaded.'
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    # asserts to validate parameters
    assert secretWord is not ' ', 'secretWord can not be null'
    assert isinstance(secretWord, basestring), 'secretWord needs to be string'

    secretLetters = []

    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
        else:
            pass

    return True

def getGuessedWord():
     guessed = ''

     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available

def hangman(secretWord):
    # asserts to validate parameters
    assert secretWord is not ' ', 'secretWord can not be null'
    assert isinstance(secretWord, basestring), 'secretWord needs to be string'

    guesses = MAXIMUM_GUESSES
    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    while isWordGuessed(secretWord, lettersGuessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -= 1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) is True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

secretWord = loadWords().lower()
hangman(secretWord)
