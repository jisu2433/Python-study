n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))

for i in range(n, m) :
    if i%2==0 :
        print(f'{i} 짝수')
