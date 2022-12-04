#pig_latin example: boy -> oybay

vowel = 'aeiouy'

print("Welcome to the Piglatin Maker\n")

while True:

    word = input("type word you want to make piglatin: ")

    for i in word:
        if word[0] == vowel[i]:
            print("\n\n")
            print(word + "way")
            print("\n\n")

        else: 
            print("A") #useless code
            #you must fill in this space...
    
    tryAgain = input("\n\nTry again? (Press Enter else 'quit' to quit)\n")
    if tryAgain.lower() == "quit":
        break

input("\nPress Enter to exit.")