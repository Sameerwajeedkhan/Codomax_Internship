def greet():
    print("Hello! Welcome to Python.")

greet()

def greet(name):
    print("Hello", name)

greet("Suraksha")


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))

result = check_even_odd(number)

print("The number is", result)