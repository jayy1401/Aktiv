string = input("enter your string:")

print("your string is: ", string)


count = 0

for i in string:
    if i.isalpha():
        count += 1


print("number of character in your string: ", count)