"""
pseudocode

Load digital dictionary file as a list of words
 Create an empty list to hold palindromes
 Loop through each word in the word list:
    If word sliced forward is the same as word sliced backward:
        Append word to palindrome list
Print palindrome list 
"""

"""Find palindromes (letter version) in a dictionary file."""

import load_dictionary

word_list = load_dictionary.load('/Users/gimminseong/Desktop/Occult Python Project/팔린그램_주문_찾기/2of12.txt')
"""If you get a error message such 'No such file or directory: , you should try to copy file's path and paste!!!"""
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep= '\n')