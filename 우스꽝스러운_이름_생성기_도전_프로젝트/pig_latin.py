#pig_latin example: boy -> oybay

vowel = 'aeiouy'

print("Welcome to the Piglatin Maker\n")

while True:

    word = input("type word you want to make piglatin: ")

    #버그 수정 부분
    for i in range(word):
        if word[0] == vowel[i]:
            print("\n\n")
            print(word + "way")
            print("\n\n")

        elif word[0] != vowel[i]:
            for n in range(vowel):
                for j in range(word):
                    if word[0] == n:
                        pigLatin = word.replace(j, '')
                        print("\n\n")
                        print(pigLatin)
                        print("\n\n")
    #버그 수정 부분
    
    tryAgain = input("\n\nTry again? (Press Enter else 'quit' to quit)\n")
    if tryAgain.lower() == "quit":
        break

input("\nPress Enter to exit.")