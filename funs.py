def isSpy(num):
    s=0
    m=1
    while num:
        d=num%10
        num=num//10
        s+=d
        m*=d
    return m==s
num=int(input("enter a number"))
n=isSpy(num)
print(n)
