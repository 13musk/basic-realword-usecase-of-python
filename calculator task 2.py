#calculater using python
a=int(input("enter first number:"))
b=int(input("enter second number:"))

c=input("enter the opration u want to perform:-")

if (c=="+" or c=="addition"):
    print("The value of",a,"+",b, "is:",a + b)
    
elif (c=="-" or c=="subtraction"):
    print("The value of",a,"-",b, "is:",a - b)
    
elif (c=="*" or c=="multiplication"):
    print("The value of",a,"*",b, "is:",a * b)
    
elif (c=="/" or c=="division"):
    print("The value of",a,"/",b, "is:",a / b)
    
elif (c=="%" or c=="remainder"):
    print("The value of",a,"%",b, "is:",a % b)
else:
    print("wrong opration")