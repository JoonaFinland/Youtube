# Hangman game
import random, sys
from string import ascii_letters
import argparse

parser = argparse.ArgumentParser(description='Hangman')
parser.add_argument('-d', '--difficulty', help='The image directory', required=False, default='normal')
args=parser.parse_args()
difficulty = args.difficulty.lower()
difficulties = {'baby': [25,(1,5)],'easy': [10, (3,7)],'normal': [7, (4,10)], 'hard': [4, (5,13)], 'extreme': [2, (8,30)]}

if difficulty not in difficulties:
    print('Given difficulty unknown defaulting to Normal')
    difficulty = 'normal'

def generate_word(difficulty, difficulties, wordlist):
    words = []
    length = random.randint(difficulties[difficulty][1][0],difficulties[difficulty][1][1])
    with open(wordlist, 'r') as file:
        for line in file:
            if len(line) == length:
                words.append(line.rstrip())
    return random.choice(words)

def gui(currently, wrong, guess, max):
    print('_'*40)
    if guess == max:
        last='LAST TRY'
    else:
        last=''
    print('Attempt:',str(guess)+'/'+str(max),last)
    print('Current:',' '.join(currently))
    print('Wrong:',''.join(wrong))

def guess_input(word_to_guess, max):
    currently = ['_' for _ in word_to_guess]
    guess_letters = []
    guesses = 0
    bad_letters = []
    while guesses <= max:
        gui(currently, bad_letters, guesses, max)
        user_input = input('> ').lower()
        if len(user_input) != 1:
            if user_input == ''.join(word_to_guess):
                print('You win! The word was:',''.join(word_to_guess))
                break
            else:
                print("Sorry, that is not the word")
                guesses+=1

        elif user_input not in ascii_letters:
            print("Please input a letter in range a-z.")
        elif user_input in guess_letters:
            print("You have already inputted this letter before.")
        else:
            guess_letters.append(user_input)
            if user_input in word_to_guess:
                print("Nice! You guessed the right letter.")
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == user_input:
                        currently[i] = user_input
            else:
                print("Sorry, that was a wrong letter.")
                bad_letters.append(user_input)
                guesses += 1
            if '_' not in currently:
                print('You win! The word was:',''.join(word_to_guess))
                break
    if (guesses >= max):
        print('You lose! The word was:',''.join(word_to_guess))

guess_input(generate_word(difficulty, difficulties, 'wordlist.txt'), difficulties[difficulty][0])
