#Tasks1:
users_math = ["add_two_numbers", "subtract_two_numbers", "multiply_numbers", "divide_numbers", "get_modolus" ]

a = 12
b = 23

def add_two_numbers():
    return a + b
print(add_two_numbers()) 

def subtract_two_numbers():
    return a - b
print(subtract_two_numbers())

def multiply_numbers():
    return a * b
print(multiply_numbers())

def divide_numbers():
    return a / b
print(divide_numbers())

def get_modolus():
    return a % b
print(get_modolus())



users_input = input("What is the number: ")
users_input2 = input("What's your choice?")
if users_input == users_input2:
    print(f" {users_input} , which is great!")
else:
    print("Wrong answer!")