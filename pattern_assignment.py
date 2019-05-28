# sunday 26 may 2019:
# ASSIGNMENT:
# PRINT NUMBER AND STAR PATTERN BY USING NESTED LOOP:
print("------------pattern : 1----------------")
n = int(input(" ENTER THE NO. OF ROWS:"))
for i in range(1,n+1):
    for j in range (1,i+1):
        print(j,end=' ')
    print()
print("------------pattern : 2----------------")
n = int(input(" ENTER THE NO. OF ROWS:"))
for i in range(1,n+1):
    for j in range (1,i+1):
        print(i,end=' ')
    print()
print("----------pattern : 3-------------------")   
n = int(input("ENTER THE NO. OF ROWS:"))  
for i in range(1,n+1) :
    for j in range(1,i+1):
        print("*",end=' ') 
    print()
print("---------pattern : 4---------------------") 
print("========DAIMOND PATTERN=============") 
n = 5  
for rows in range(1,n+1):#1 to 5 rows
    for space in range(0,n-rows):
        print(" ",end=" ")
    for stars in range((rows*2)-1):
        print("*",end=" ")
    print() 
for rev_row in range(n-1,0,-1):#6 to 9 rows
    for space in range(0,n-rev_row):
        print(" ",end=" ")
    for stars in range((rev_row*2)-1):
        print("*",end=" ")
    print() 
print("--------------OR--------------") 
n =5
for i in range(1,n+1):
    for j in range(n-i+1):
        print(end=" ")
    for j  in range(i):
        print("*",end=" ") 
    print()       
for i in range(n-1,0,-1):
    for j in range(n-i+1):
        print(end=" ")
    for j  in range(i):
        print("*",end=" ") 
    print()    
             
          
