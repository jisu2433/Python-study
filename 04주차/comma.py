# 풀이1
def make_comma(num): 
    num = format(int(num),',')  
    print(num)

try:
    num = int(input("숫자를 입력해주세요: "))
    make_comma(num)

except:
    print("숫자로 입력해주세요")

# 풀이2
def make_comma2(number):
    number = str(number)
    length = len(number)
    num_comma = length //3
    if length % 3 == 0:
        num_comma = num_comma -1
    
    new_number = ""
    n = -1
    while num_comma != 0:
        new_number = number[n] + new_number
        if n % 3 == 0:
            new_number = "," + new_number
            num_comma = num_comma -1
        n=n-1
    print(number[:n+1]+new_number)

number = input('숫자를 입력하시오 :')
make_comma2(number)