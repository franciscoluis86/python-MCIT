print("Hola Nicaragua")
if 5 > 2:
    print("Five is greater than two!")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

def howmuchmoneydoihave(money):
    return f"Hello, you have CAD {money} in your account"
print(howmuchmoneydoihave(1))

x, y, z = "Orage", "Banada", "Cherry"
print(x)
print(y)
print(z)

fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x)
print(y)
print(z)

def calculate_sum(numbers):
  return sum(numbers)

#1st step
input_numbers = input("Enter numbers separated by spaces: ")
#2nd step
aftersplit=input_numbers.split()
aftermap=map(int,aftersplit)
afterlist=list(aftermap)
print(aftersplit)
print(aftermap)
print(afterlist)
numbers_list = list(map(int, input_numbers.split()))
print(numbers_list)
total_sum = calculate_sum(numbers_list)
print("The sum of the numbers is:", total_sum)

#1. sum function
#2. substraction function
#3. multiplicaton function

#request the user for two inputs
#the user puts the two inputd
##put this in a variable --> Enter First number:
#put this in a variable --> Enter second number:
#first number + second number 

numberA=int(input("Please enter a number: "))
numberB=int(input("Please enter a second number: "))

def sum_numbers(numberA, numberB):
    return f"The sum of both numbers are {numberA + numberB}"
print(sum_numbers(numberA, numberB))

def substract_numbers(numberA, numberB):
    if numberA < numberB:
        return "Sorry first number is smaller than second number"
    else:
        return f"The substraction of both numbers are {numberA - numberB}"
print(substract_numbers(numberA, numberB))

def multiplication_numbers(numberA, numberB):
    return f"The multiplication of both numbers are {numberA * numberB}"
print(multiplication_numbers(numberA, numberB))