x=int(input("enter the current year:"))
y=int(input("enter the future year:"))
print("future leap years are:",)
for x in range(x,y+1):
 if(x%4==0 and x%100!=0 or x%400==0):
    print(x)

