def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)
try:
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
except ValueError :
    print("Enter a number")
if ValueError:
    break


result=input("add,substract,multiply or divide:")
try:
    if result=="add":
        print(a,"+",b,"=",add(a,b))

    elif result=="substract":
        print(a,"-",b,"=",sub(a,b))

    elif result=="multiply":
        print(a,"*",b,"=",multiply(a,b))

    else:
        print(a,"/",b,"=",divide(a,b))

except ZeroDivisionError:
    print("No dividing by 0")