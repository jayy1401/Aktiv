n = int(input("Length of list : " ))
list1 = []
for i in range(n):
	element = int(input("enter the element: "))
	list1.append(element)

print("your list: ",list1)

sum1 = 0
for i in list1:

	sum1 = sum1 + i

print("sum of all elements: ",sum1)


count = 1
for i in list1:

	count = count * i

print("Multiplication of all elements: ",count)



