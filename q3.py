letter=str(input("Enter a letter: "))
l=letter.split()
text,letter= map(str,l)
k=0
for i in text:
    if i==letter:
        k+=1

length=len(text)
frequency=(k/length)*100
print(int(frequency))
