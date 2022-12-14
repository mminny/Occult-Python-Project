# pseudocode
"""
Load digital dictionary as a list of words 
Start an empty list to hold palingrames
For word in word list:
    Get length of word
    If length > 1:
        Loop through the letters in the word:
            If reversed word fragment at front of word is in word list and letters 
            (idk)after form a palindromic sequence:
                Append word and reversed word to palingram list
            If reversed word fragment at end of word is in word list and letters
            (idk)before form a palindromic sequence:
                Append reversed word and word to palingram list
Sort palingram list alphabetically 
Print word-pair palingrams from palngram list
"""

"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary

word_list = load_dictionary.load('/Users/gimminseong/Desktop/Occult Python Project/팔린그램_주문_찾기/2of12.txt')

# ind word-pair palingrams 
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i]and rev_word[end-i:]in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:]and rev_word[:end-i]in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()
# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}", format(first, second))
