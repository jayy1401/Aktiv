my_dict = {3: 'Heli', 1: 'jay', 2: 'Aayush'}

sorted_list = sorted(my_dict.items())

sorted_dict = {}
for key, value in sorted_list:
    sorted_dict[key] = value

print("Sorted by key-value using for loop:", sorted_dict)
