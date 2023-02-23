ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# 각각의 요소를 단어로 나눈다(글자로 나누는 것이 아님!!!)

cipherlist = list(ciphertext.split()) 

# 초기 변수 값 설정하기
COLS = 4 # 가로
ROWS = 5 # 세로
key = '-1 2 -3 4'
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

# key_int를 정수형 리스트로 변환
key_int = [int(i) for i in key.split()] 

# turn columns into items in list of lists
for k in key_int:
    if k < 0: # reading bottom-to-top of column
        col_items = cipherlist[start:stop] 
    elif k > 0: # reading top-to-bottom of column
        col_items = list((reversed(cipherlist[start:stop]))) 

    print(col_items) # type: ignore
    translation_matrix[abs(k) - 1] = col_items # type: ignore 
    start += ROWS
    stop += ROWS

print("\nciphertext = {}".format(ciphertext))
print("\ntranslation matrix =", *translation_matrix, sep="\n")
print("\nkey length = {}".format(len(key_int)))    

# loop through nested lists popping off last item to new list:
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop()) # type: ignore 
        plaintext += word + ''

print("\nplaintext = {}".format(plaintext))


    
