n=int(input("enter the number of elements"))
numlist=[]
for i in range(n):
    a=int(input("enter the numbers"))
    numlist.append(a)
print("entered numbers are:",numlist)
sqr_list=[x**2 for x in numlist]
print("squered list are:",sqr_list)
