import random

def guess_numbers():
    number = random.randint(0,100)
    guess=1
    while True:
        num = input("숫자를 예측해보세요 :")
        if int(num) == number :
            print(f'{guess}차 시도')
            print(f'숫자를 맞추셨습니다! {number}는 최솟값입니다.')
            continue
        if int(num) != number :
            print(f'{guess+1}차 시도')
guess_numbers()
