import statistics
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))

def find_even_number(n,m):
    list = [n, m]
    for i in range(n, m) :
        if i%2==0 :
            print(f'{i} 짝수')
    if statistics.median(list)%2 == 0:
        print(f'{int(statistics.median(list))} 중앙값')    
find_even_number(n,m)