import random
games = int(input("몇 판을 진행하시겠습니까? : "))

inputs = {0:'가위', 1:'바위', 2:'보'}
results = ['무승부', '패배', '승리']
draw = 0
i_lose = 0
i_win = 0

for game in range(games) :
    try:
        def rsp(i, com):
            print(f'나: {inputs[i]}')
            print(f'컴퓨터: {inputs[com]}')
            print(f'{game+1} 번째 판 나의 {results[com-i]}!')
            if results[com-i] == '무승부' :
                draw+=1
            elif results[com-i] == '패배' :
                i_lose+=1
            elif results[com-i] == '승리' :
                i_win+=1       
        my = int(input("0:가위, 1:바위, 2:보 : "))
        cp = random.randint(0, 2)
        rsp(my, cp)
    except:
        continue
print(f'나의 전적: {i_win}승 {draw}무 {i_lose}패')
    
