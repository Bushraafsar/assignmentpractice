#PYTHON PROGRAM TO CREATE FUNCTION OF N FACTORIAL:
#USING USER DEFINDED FUNCTION AND while LOOP:
n = int(input("Enter Number:"))
def factorial(n):
    if n < 0:
        print("Factorial of negative number doesn't exist!")
    elif n == 0:
        result = 1    
        print("factorial of",n,"is:",result)
    elif n == 1:
        result = 1
        print("factorial of",n,"is:",result)
    else:
        a=n-1 
        while a!=0: 
           n = n*a
           a -= 1
        print("factorial is",n)
factorial(n)
#PYTHON PROGRAM TO CREATE FUNCTION OF N FACTORIAL:
#USING USER DEFINDED FUNCTION AND FOR LOOP:
n = int(input("Enter Number:"))
def factorial(n):
    if n < 0:
        print("Factorial of negative number doesn't exist!")
    elif n == 0:
        result = 1    
        print("factorial of",n,"is:",result)
    elif n == 1:
        result = 1
        print("factorial of",n,"is:",result)
    else:
        a = 1
        for i in range(n,0,-1):
            a = a*i
        print("factorial is",a)
factorial(n)        

            



            

