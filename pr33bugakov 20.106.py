a=424+2*(-2)*424+2*(-2)
print(a)


a=9**19
b=float(9**19)
c=int(b)
d=a-c
print(d)

X=int(input())
H=int(input())
M=int(input())
print(((H*60)+X+M)//60)
print((X+M)%60)

A=int(input())
B=int(input())
H=int(input())
while A>B:
    print("Некорректные данные")
    A=int(input())
    B=int(input())
    H=int(input())
if H<A :
    print("Недосып")
elif H>B :
    print("Пересып")
else:
    print("Это нормально")

year = int(input())
if (year % 4 == 0) and (year % 100 !=0) or (year % 400 ==0):
    print("Високосный")
else:
    print("Невисокосный")


a=float(input())
b=float(input())
c=str(input())
if c =="+":
    print(a+b)
elif c =="-":
    print(a-b)
elif c =="*":
    print(a*b)
elif c =="/" and b==0:
    print("Деление на 0 !")
elif c =="/" and b!=0:
    print(a/b)
elif c =="mod" and b==0:
    print("Деление на 0 !")
elif c =="mod" and b!=0:
    print(a % b)
elif c =="pow":
    print(a**b)
elif c =="div" and b==0:
    print("Деление на 0 !")
elif c =="div" and b!=0:
    print (a//b)


s=str(input())
sum1=int(s[0])+int(s[1])+int(s[2])
sum2=int(s[3])+int(s[4])+int(s[5])
if sum1==sum2:
    print("Счастливый билет")
else:
    print("Обычный билет")

    



