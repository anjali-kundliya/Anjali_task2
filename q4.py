number=int(input("Enter a number: "))
i=number
j=0
while number>0:
    num=number%10
    j=j*10+num
    number=number//10
if i==j:
    print("Number is palindrome")
else:
        print("Number is not palindrome")
