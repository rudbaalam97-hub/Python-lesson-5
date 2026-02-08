# program make a simple calculator

# This function adda two numbers
def add(x, y):
    return x + y

#This function substracts two numbers
def substract(x, y):
    return x - y

#This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function devides two numbers
def devide(x, y):
    return x / y

num1 = int(input("Enter Number 1"))
num2 = int(input("Enter number 2"))

print("sum :", add(num1, num2))
print("difference :", substract(num1, num2))
print("Product :", multiply(num1, num2))
print("Quotinent :", devide(num1, num2))