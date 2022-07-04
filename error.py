def divide(a, b):
    try:
        return a / b
    except:
        return "division by zero"


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print(divide(a, b))

print("==============================")
print("This should print")  # even with zero division
