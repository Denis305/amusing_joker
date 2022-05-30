import random
from words import words

# list of hangman images
HANGMAN = [
    '''
    +---+
    |   |
        |
        |
        |
        |
=========''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
=========''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========''']

print('Hangman Game')
print('Python Portfolio Project By: Denis Zambrano')
high_score = 0


def get_valid_word(words):  # function to get a valid word
    word = random.choice(words)  # get a random word from the list
    while ' -' in word or ' ' in word:  # it will not include words with hyphens or spaces
        word = random.choice(words)
    return word.upper()


word = get_valid_word(words)


class player():  # class for player name and score
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'{self.name} - {self.score}'

    def player_name(self):
        print('\nEnter your name: ')
        self.name = input()
        return self.name

    def player_score(self):
        print(f'\nHi {self.name}, your score is {self.score}')


def hangman(word):  # function for the game
    word = get_valid_word(words)
    word_letters = set(word)  # get a set of letters from the word
    word_length = len(word)
    word_guessed = set()
    wrong_guesses = 0
    high_score = 0
    player_name = player('', 0)
    player_name.player_name()
    # get the number of wrong guesses
    max_wrong_guesses = len(word_letters - word_guessed)
    print(f'\nWelcome to Hangman, {player_name.name}!')
    print("Good luck! You're going to need it!")
    print('\n')
    print('Current High Score: {}'.format(high_score))  # print the high score
    print('\n')
    print('The word is {} letters long.'.format(
        word_length))  # print the length of the word
    print('\n')
    print(HANGMAN[wrong_guesses])  # print the hangman image
    print('\n')
    # print the number of wrong guesses
    print('You have {} wrong guesses left.'.format(max_wrong_guesses))
    print('\n')
    print('The word is: {}'.format(get_display_word(
        word, word_guessed)))  # print the display word
    print('\n')
    # while the wrong guesses are less than the max guesses and the word is not guessed
    while wrong_guesses < max_wrong_guesses and word_guessed != word_letters:
        print('You have {} wrong guesses left.'.format(
            max_wrong_guesses - wrong_guesses))
        print('Available letters: {}'.format(set(chr(i)
              for i in range(ord('A'), ord('Z') + 1)) - word_guessed))
        guess = input('Please guess a letter: ').upper()
        if guess in word_guessed:  # if the letter has already been guessed
            print("Oops! You've already guessed that letter: {}".format(
                get_display_word(word, word_guessed)))
            print(HANGMAN[wrong_guesses])
        elif guess in word_letters:  # if the letter is in the word
            word_guessed.add(guess)
            print('Good guess: {}'.format(get_display_word(word, word_guessed)))
            print(HANGMAN[wrong_guesses])
        else:
            wrong_guesses += 1  # if the letter is not in the word
            print('Oops! That letter is not in my word: {}'.format(
                get_display_word(word, word_guessed)))
            print(HANGMAN[wrong_guesses])
        print('-------------')
    if word_guessed == word_letters:  # if the word is guessed
        print(f'Congratulations {player_name.name}, you won!')
        print('Your total score for this game is: {}'.format(
            max_wrong_guesses - wrong_guesses))
        if max_wrong_guesses - wrong_guesses > high_score:  # if the score is higher than the high score
            high_score = max_wrong_guesses - wrong_guesses
            print('New High Score: {}'.format(high_score))
    else:  # if the word is not guessed
        print('Sorry, you ran out of guesses. The word was {}.' .format(word))
    print('\n')
    print('Current High Score: {}'.format(high_score))
    print('\n')
    print(f'{player_name.name}, would you like to play again?')
    print('\n')
    # ask if the player wants to play again
    play_again = input('Enter Yes or No: ').upper()
    if play_again == 'YES' or play_again == 'Y':
        hangman(word)
    else:
        print('Thanks for playing!')


def get_display_word(word, word_guessed):  # function to get the display word
    return ''.join(letter if letter in word_guessed else '_' for letter in word)


if __name__ == '__main__':  # if the file is run directly
    hangman(get_valid_word(words))
    input('Press Enter to exit.')
    exit()
