#PYTHON PROGRAM TO CREATE FUNCTION OF TAKEN ORDER FROM USER:
print("*********************************ABC ELECTRONIC SHOP************************************")
print("we have AC, Refrigerators,Waashing Machines Of the following reliable companies:")
print("HAIER","PEL&","ORIENT")
print("===========================PLEASE PLACE YOUR ORDER==================")
product = input("ENTER THE NAME OF THE PRODUCT YOU WANT TO PURCHASE FROM OUR SHOP:")
size= input("ENTER THE SIZE :")
color = input("ENTER THE COLOUR OF YOUR CHOICE:")
manufacturing_co = input("ENTER THE COMPANY NAME:")
model_no = input("ENTER MODEL NO.:")
no_of_units =int(input("ENTER HOW MANY UNITS YOU WANT TO BUY:"))
def order_fromuser(product, size, colour, companyname, modlno, units):
    print("YOU HAVE ORDERED",product,"AND ITS DETAIL ARE AS FOLLOWS:")
    print("SIZE:",size)
    print("COLOR:",color)
    print("MANUFACTURING CO.:",manufacturing_co)
    print("MODEL NO.:",model_no)
    print("NO OF UNITS:",no_of_units)
order_fromuser(product, size, color, manufacturing_co, model_no, no_of_units)
#PYTHON PROGRAM TO CREATE FUNCTION OF BILL CALCULATION;
def bill_calculation(product, size, no_of_units, manufacturing_co):
    if product.lower() == "refrigerator" and size.lower() == "large" and manufacturing_co.lower() == "haier":
        unit_price = 60000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "refrigerator" and size.lower() == "medium" and manufacturing_co.lower() == "haier":
        unit_price = 50000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "refrigerator" and size.lower() == "small" and manufacturing_co.lower() == "haier":
        unit_price = 400000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "refrigerator" and size.lower() == "large" and manufacturing_co.lower() == "orient":
        unit_price = 550000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "refrigerator" and size.lower() == "medium" and manufacturing_co.lower() == "orient":
        unit_price = 45000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "refrigerator" and size.lower() == "small" and manufacturing_co.lower() == "orient":
        unit_price = 300000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "refrigerator" and size.lower() == "large" and manufacturing_co.lower() == "pel":
        unit_price = 60000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "refrigerator" and size.lower() == "medium" and manufacturing_co.lower() == "pel":
        unit_price = 50000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "refrigerator" and size.lower() == "small" and manufacturing_co.lower() == "pel":
        unit_price = 400000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "large" and manufacturing_co.lower() == "haier":
        unit_price = 400000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "medium" and manufacturing_co.lower() == "haier":
        unit_price = 350000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "small" and manufacturing_co.lower() == "haier":
        unit_price = 250000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "large" and manufacturing_co.lower() == "orient":
        unit_price = 300000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "medium" and manufacturing_co.lower() == "orient":
        unit_price = 250000
        total_price = unit_price*no_of_units 
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "small" and manufacturing_co.lower() == "orient":
        unit_price = 250000
        total_price = unit_price*no_of_units 
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "large" and manufacturing_co.lower() == "pel":
        unit_price = 40000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "medium" and manufacturing_co.lower() == "pel":
        unit_price = 35000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "AC" and size.lower() == "small" and manufacturing_co.lower() == "pel":
        unit_price = 300000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "washing mmachine" and size.lower() == "large" and manufacturing_co.lower() == "orient":
        unit_price = 25000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "washing machine" and size.lower() == "medium" and manufacturing_co.lower() == "orient":
        unit_price = 20000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "washing machine" and size.lower() == "small" and manufacturing_co.lower() == "orient":
        unit_price = 30000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "washing machine" and size.lower() == "large" and manufacturing_co.lower() == "pel":
        unit_price = 25000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "washing machine" and size.lower() == "medium" and manufacturing_co.lower() == "pel":
        unit_price = 18000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "washing machine" and size.lower() == "small" and manufacturing_co.lower() == "pel":
        unit_price = 12000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "washing machine" and size.lower() == "large" and manufacturing_co.lower() == "haier":
        unit_price = 35000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.lower() == "washing machine" and size.lower() == "medium" and manufacturing_co.lower() == "haier":
        unit_price = 25000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    elif product.upper() == "washing machine" and size.lower() == "small" and manufacturing_co.lower() == "haier":
        unit_price = 20000
        total_price = unit_price*no_of_units
        print("unit price:",unit_price)
        print("total price:",total_price)
    else:
        print("the above product is not available in our shop!")    
bill_calculation(product, size, no_of_units, manufacturing_co) 
#python program to offer discount to customer:
total_price=int(input("ENTER THE TOTAL PRICE OF CLIENT:"))
def discount(total_price):
    if total_price > 50000:
        discount=total_price*50/100
        print("the discount you avail is:",discount) 
    elif total_price >= 25000:
        discount=total_price*25/100
        print("the discount you avail is:",discount) 
    else:
        print("sorry! YOU DON'T AVAIL ANY DISCOUNT OFFER")  
discount(total_price) 
print("THANK YOU FOR THE SHOPPING!")  
print("WE ARE LOOKING FORWARD TO SEE YOU AGAIN!")      
               

        


        






        


     


        








        


     


        








        


     


        







        


        






        


     


        








        


     


        








        


     


        







