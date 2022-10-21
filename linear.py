def linear(y, x): 
    for i in range(len(y)): 
        if y[i] == x: 
            return i
y =[10,9,8,6,2,1,5,7,3,0]
x=int(input("enter a number between 1 to 10: "))
print("the index position of the given number is is",linear(y,x))

