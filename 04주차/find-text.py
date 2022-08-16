text ="Some tings don't work Some tings are bound to be Some tings, they hurt And they tear apart me You left your diary at my house And I read those pages, do you really love me, baby? Some tings don't work Some tings are bound to be Some tings, they hurtAnd I cried at the curbWhen you first said, Oel ngati kameie"
word = input('찾을 문자를 입력하세요 ')

def count_word(text, word):
    findWord = text.count(word)
    print(findWord)
count_word(text, word)