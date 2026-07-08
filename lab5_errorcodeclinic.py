#  Sasha Peterson | Lab 5 | Error Code Clinic

# Snippet 1

# PREDICT: the error type is zero division error because the code is trying to divide by zero.

x = 10
y = 0 
if y == 0: 
    print("you cant divide by zero")
else: 
    result = x / y
    print("The result is:", result)

# Snippet 2 

# PREDICT: the error type is an index error because the code is trying to access an index that does not exist in the list yet 

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):  #change print(numbers [i+1] to print numbers[i] to fix the error
    print(numbers[i]) 

# Snippet 3

# PREDICT: umm to be honest im not too sure what the error type is but i know it has something to do with the def line, maybe something to do with the function definiton.. idk

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area 

radius = 5
print(calculate_area(radius)) 

# Snippet 4

# PREDICT: the error type is an syntax error i'm pretty sure, because of the if statement, its missing a colon

def is_even(number): 
    if number % 2 == 0: 
        return True 
    else:   #else statement was missing a colon at the end of the line which i now noticed, so i added it to fix the error
        return False
    
print(is_even(4))
print(is_even(7))

# Snippet 5

# PREDICT: another syntax error because the for loop statment is also missing a colon 

for i in range(5):
    print(i)

# Snippet 6

# PREDICT: i have no clue so i'm going to write the code and ask google how i can problem solve

def greet(name):
    return "Hello," + name #comma changed to plus sign to fix the error

print(greet("Sasha"))

# Snippet 7

# PREDICT: syntax error because the print statement is indented and doesnt need to be

numbers = [1,2,3,4,5]
total = 0
for number in numbers:
    total += number 
print("Sum of numbers:", total) 

# Snippet 8

# PREDICT: i dont think this is a syntax error because the code is written correctly, but i think the error type has something to do with infinite loop? 

def factorial(n):
    if n == 0: 
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

# Snippet 9 

# PREDICT: the error type is a name error i think but idk because im pretty sure its not but im just guessing 

name = input("Enter your name: ")
if name == "Sasha" or name == "Tiny":
    print("Hello," + name)
else:
    print("Hello, stranger!")


# Snippet 10

# PREDICT: zero division erros beacause u cant divide by zero

def divide_numbers(x,y):
    if y == 0:
        return "Error: cant divide by zero."
    else:
        result = x/y
        return result

    num1 = 10
    num2 = 0
    print(divide_numbers(num1, num2))