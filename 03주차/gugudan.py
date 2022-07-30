num=int(input("몇 단?:"))
gugudan=1
print(num, "단")
for gugudan in range(1, 10, 2) :
    if num*gugudan <= 50 :
        print (num, "X", gugudan, "=",  num*gugudan)
        gugudan+=1


