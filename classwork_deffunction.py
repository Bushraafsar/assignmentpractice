print("*********************userdef function ***************************")
#ADDITION:
print("additon")
num1 =int(input("enter first number:"))
num2 =int(input("enter second number:"))
def add(a,b):#recieving info/data,called parameter
    result_of_sum = a+b
    print("result=",result_of_sum)
add(num1,num2) #passing data called assignment
print("********************* userdef function ***************************")
print("subtraction")
num1 =int(input("enter first number:"))
num2 =int(input("enter second number:"))
def sub(a,b):
    result_of_sub = a-b
    print("result=",result_of_sub)
sub(num1,num2) 
print("*********************userdef function ***************************")
print("multiplication")
num1 =int(input("enter first number:"))
num2 =int(input("enter second number:"))
def multiply(a,b):
    result_of_multiply = a*b
    print("result=",result_of_multiply)
multiply(num1,num2)
print("*********************userdef function ***************************")
print("division:")
num1 =int(input("enter first number:"))
num2 =int(input("enter second number:"))
def divide(a,b):
    result_of_division = a/b
    print("result=",result_of_division)
divide(num1,num2)
print("*********************userdef function ***************************")
print("even or odd:")
num = int(input("ENTER NUMBER:"))
def even_or_odd(num):
    if num%2 == 0:
        result = "this number is prime"
    else:
        result = "this number is odd" 
    return result
output_of_function=even_or_odd(num)
print("result:",output_of_function)
print("*********************userdef function ***************************")
print("===============SINGLE ASTERIK===================")#STORE IN TUPLE
print("POSSITIONAL ARGUMENT:")
def pizza(crust,*topping):
    print("You Have ordered pizza with",crust,"crust and the following topping:")
    for each in topping:
        print(each)
pizza("thick","chicken","onion","green olives",) 
print("=============DOUBLE ASTERIK=====================")   #STOREIN DICTIONARY
print("KEYWORD ARGUMENT:")  
def pizza(crust,**topping):
        print("You Have ordered pizza with",crust,"crust and the following topping:")
        for i,j in topping.items():
            print(i,j)
pizza("thick",topping1 = "chicken",topping2 ="onion",topping3 = "capsicum")
print("DEFAULT ARGUMENT:")
def user_info(owner,pet,city="Karachi"):
    print("the owner of",pet,"is",owner,"they are from",city)
user_info(owner = "Zaid Ali",pet = "dog")    









