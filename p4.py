n=int (input("enter the no. of elements in the list:"))
num_list=[]
for i in  range(n):
    x=int(input("enter the element:"))
    if x < 100:
        num_list.append(x)
    else:
        num_list.append('over')
print(num_list)