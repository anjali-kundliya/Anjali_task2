a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operation=str(input("Enter the operation you want to perform: "))
add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b

i="{:.2f}"
for x in operation:
    if x=="+":
        print("Addition is:",i.format(add))
    elif x=="-":
        print("Subtraction is:",i.format(sub))
    elif x=="*":
        print("Multiplication is:",i.format(mul))
    elif x=="/":
        print("Division is:",i.format(div))
    elif x=="%":
        print("Modulus is:",i.format(mod))
    else:
        print("Invalid Operator")
