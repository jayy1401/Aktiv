user_input = input("Enter a value: ")

try:
    integer_value = int(user_input)
    print("Input is an integer.")
except ValueError:
    print("Input is not an integer.")

