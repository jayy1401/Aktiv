string = 'Hello good morming how are you doing'

string1 = string.split(" ")

print(string1)

b = []

for i in string1:
	a = i[0:2]
	b.append(a)

print(b)

