n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))

for i in range(n,m+1):
    count = 0
    for k in range(1, i+1):
        if i%k == 0:
            count += 1
    if count <= 2:
        print(f'소수 {i}')

