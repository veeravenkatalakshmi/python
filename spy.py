
def isspy(num):
    s=0
    m=1
    while num:
        d=num%10
        num=num//10
        s+=d
        m*=d
    return m==s

n=int(input())
res=isspy(n)
print(res)
