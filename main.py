import math
x=int(input("Введите у "))
y=int(input("Введите х "))
res=abs(x**(y/x)-(y/x)**1/3)+(y-x)
print(res)