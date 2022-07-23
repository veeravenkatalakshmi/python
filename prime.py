def fun(n):
    if n<= 0:
        return 
    fun(n-1)
    print(n)
    fun(n-2)

print(fun(5))