a = int(input("Length of list : " ))

mylist = []

for i in range(a):
	element = int(input("enter the element: "))
	mylist.append(element)

print("your list: ",mylist)

max1 = mylist[0]

for i in mylist:
	if i > max1:
		max1 = i 

print("Maximum number from list is: ",max1)