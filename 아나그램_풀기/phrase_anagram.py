# pseudocode
"""
Load dictionary file
Accept name from user
Set limit = length of name 
Start empty list to hold anagram phrase
While length of phrase < limit:
    Generate list of dictionary words that fit in name 
    Present words to user
    Present remaining letters to user 
    Present current phrase to user 
    Ask user to input word or start over
    If user input can be made from remaining letters:
        Accept choice of new word of words from user
        Remove letters in choice from letters in name 
        Return choice and remaining letters in name 
    If choice is not a valid selection:
        Ask user for new choice or let user start over
    Add choice to phrase and show to user
    Generate new list of word and repeat process 
"""

import sys
from collections import Counter
import load_dictionary

dict_file = load_dictionary.load('/Users/gimminseong/Desktop/Occult Python Project/아나그램_풀기/2of12.txt')
# ensure "a" & "I" (both lowercase) are included
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

ini_name = input("Enter a name: ")

def find_anagram(name, word_list):
    """Read name & dictionary file & display all anagram IN name"""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower()) 
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)

    print(*anagrams, sep='¥n')
    print()
    print("Remaining letters = {}".format(name))
    print("Number of remaining letters = {}".format(len(name)))
    print("Number of remaining (real word) anagrams = {}".format(len(anagrams)))

def process_choice(name):
    """Check uer choice for validity, return choice & leftover letters."""
    while True:

        choice = input('\nMake a choice else Enter to start over or # to end: ')

        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())

        left_over_list = list(name)
        
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won' work! Mae another choice!", file=sys.stderr)

    name = ''.join(left_over_list) # makes display mre readable
    return choice, name

def main():
    






