print("Hello world")
print("I am Mahnoor Akhtar")

print("I am learning Python programming language", "Its fun and interesting")

print (23)

print (3.14 + 2)


# Variables in python 

name = "Mahnoor Akhtar"
age=21
print("My name is", name)
print("My age is " + str(age))


# To find type of variable

print(type(name))
print(type(age))

success = True
print(type(success))
print("Success status is", success)

fail = None
print(type(fail))
print("Fail status is", fail)


# Print sum of two numbers
a = 10 
b = 20 

sum = a+b
print("Sum of", a, "and", b, "is", sum)


# Comments in python 
# This is a single line comment 


# Operators in python 
a = 10 
b = 5

print(a+b)      # Addition
print(a-b)      # Subtraction
print(a*b)      # Multiplication
print(a/b)      # Division
print(a%b)      # Modulus
print(a**b)     # Exponentiation
print(a//b)     # Floor Division
print(a>b)      # Greater than
print(a<b)      # Less than
print(a==b)     # Equal to
print(a!=b)     # Not equal to
print(a>=b)     # Greater than or equal to
print(a<=b)     # Less than or equal to
print(a and b)  # Logical AND
print(a or b)   # Logical OR
print(not(a>b)) # Logical NOT


# Type conversion in python by python interpreter

a=100
b=3.14
print(a+b)

# Type casting Manually conversion 
a = "100"
b = 5
print(int(a)+b)
print(a+ " "+ str(b))


# Input from user
name = input("Enter your name: ") #Result of input is always string
print("Hello " + name + ", Welcome to Python programming!")


age = int(input("Enter your age: ")) #Type casting input to integer
print("You are " + str(age) + " years old.")



