n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))

def count_prime_number(n, m):
    cnt = 0 # 소수 개수
    for i in range(n, m+1):
        if i <= 1: # 0과 1은 소수가 아님
            continue
        
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            cnt += 1
    return f"소수개수 {cnt}"

print(count_prime_number(n, m))

