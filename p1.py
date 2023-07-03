my_list = [1, 2, 3, 4, 5]

# original list
print("Original list:", my_list)


for i in range(len(my_list)):
    value = my_list[i] + 1  
    my_list[i] = value


print("Updated list:", my_list)


