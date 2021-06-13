data={"123-08":24,"67-03":35,"45-05":15,"50-09":13,"121-08":40}
age=int(input())
young=0
old=0

for i in data.values():
    if i<18:
        old+=5
    else:
        old+=20

for j in data.values():
    if j<18:
        young+=5
    else:
        young+=20

print(young)
print(old)
if age<18:
    print(int((new-old)/old*100))
else:
    print(0)

        
