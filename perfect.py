import math as M
def isperfect(num):
    res=1
    i=2
    sq=int(M.sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            res+=i
            res+=num//i

    return res==num

num = int(input("enter a number \n"))

boo = isperfect(num)
print(boo)



