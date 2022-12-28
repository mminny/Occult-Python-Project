import load_dictionary

word_list = load_dictionary.load('/Users/gimminseong/Desktop/Occult Python Project/아나그램_풀기/2of12.txt')

anagram_list = []

# input a SINGLE word or SINGLE name below to find its anagram(s):
name = input('what your name?')
print("Input name = {}".format (name)) 
name = name.lower()
print("Using name = {}".format (name))

# sort name & find anagrams
name_sorted = sorted(name) 
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

# print out list of anagram
print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =", *anagram_list, sep='\n')

