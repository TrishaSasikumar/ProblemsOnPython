def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter any number"))
if n<0:
    print("negative")
else:
    print("the factorial is",fact(n))
