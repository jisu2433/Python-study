import random

rsp = ['가위', '바위', '보']
computer = random.randint(0, 2)
computer_rsp = rsp[computer]
print(computer_rsp)

def user_rsp():
    rsp = input('가위 바위 보: ')
    return rsp
rsp = user_rsp()

if computer_rsp == user_rsp:
    print('무승부')
elif computer_rsp == '가위':
    if user_rsp == '바위':
        print('사람 승리!')
    else:
        print('컴퓨터 승리!')
elif computer_rsp == '바위':
    if user_rsp == '보':
        print('사람 승리!')
    else:
        print('컴퓨터 승리!')
elif computer_rsp == '보':
    if user_rsp == '가위':
        print('사람 승리!')
    else:
        print('컴퓨터 승리!')
