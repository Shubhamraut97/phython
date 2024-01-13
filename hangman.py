
# hangman()
import random
import string
from words import words

def get_validword(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_validword(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left. Used letters:", ' '.join(used_letters))
        word_display = ''.join([letter if letter.upper() in used_letters else '-' for letter in word])
        print(word_display)
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct guess!")
            else:
                lives -= 1
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print("You have already used that character.")
        else:
            print('Invalid character. Try again.')

    if lives == 0:
        print('You ran out of lives. Sorry, the word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!')

hangman()
