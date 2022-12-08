#pig_latin example: boy -> oybay

vowel = 'aeiouy'

print("Welcome to the Piglatin Maker\n")

while True:

    word = input("type word you want to make piglatin: ")

    i = 0
    j = 1

    for i in word:
        #버그 수정 부분
        if word[0:1] == vowel[i:j]:
            print("\n\n")
            print(word + "way")
            print("\n\n")
            j += 1

        elif word[0:1] != vowel[i:j]:
            for n in range(vowel):
                for j in range(word):
                    if word[0] == n:
                        pigLatin = word.replace(j, '')
                        print("\n\n")
                        print(pigLatin)
                        print("\n\n")
            j += 1            
    #버그 수정 부분
    
    
    
    tryAgain = input("\n\nTry again? (Press Enter else 'quit' to quit)\n")
    if tryAgain.lower() == "quit":
        break

input("\nPress Enter to exit.")