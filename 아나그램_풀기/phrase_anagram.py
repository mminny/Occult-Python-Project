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
    Ask yser to input word or start over
    If user input can be made from remaining letters:
        Accept choice of new word of words from user
        Remove letters in choice from letters in name 
        Return choice and remaining letters in name 
    If choice is not a valid selection:
        Ask user for new choice or let user start over
    Add choice to phrase and show to user
    Generate new list of word and repeat process 
"""

