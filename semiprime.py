import math as M
def isprime(num):
    sq=int(M.squrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
        return True
def issemiprime(num)
