#Write a function to add two numbers
def add_numbers():
    a=int(input("Enter Your 1st number:"))
    b=int(input("Enter your 2nd Number:"))
    print(a+b)
add_numbers()    
#----------------

#Write a function to find the maximum of two numbers
def max_numbers():
    a=10
    b=30
    print(max(a,b))
max_numbers()    
#----------------------------

#Write a function to check whether a number is even or odd
def check_number():
    num1 = int(input("Enter Your 1st Number: "))
    num2 = int(input("Enter Your 2nd Number: "))

    if num1 % 2 == 0:
        print(f"{num1} is even.")
    else:
        print(f"{num1} is odd.")

    if num2 % 2 == 0:
        print(f"{num2} is even.")
    else:
        print(f"{num2} is odd.")

check_number()
#------------------------------

#Write a function to find the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
#-----------------------------------

#Write a function to check whether a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
#-------------------------------

#Write a function to print the multiplication table of a number
def print_table():
    num=int(input("Enter Your Number:"))
    print(num)
    for a in range (1,11):
       print(f"{num} x {a} ={num*a}")
print_table()        
#------------------------

#Write a function to calculate the power of a number (base^exponent)
def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

print(f"{b}^{e} = {calculate_power(b, e)}")
#-------------------------------

#Write a function to check whether a number is a palindrome
def is_palindrome(number):
    original = str(number)            # number ko string banaya
    reversed_num = original[::-1]     # string ko ulta kiya

    if original == reversed_num:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
#----------------------------

#Write a function to generate the first n numbers of the Fibonacci series.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
num = int(input("Enter how many Fibonacci numbers you want: "))
fibonacci(num)
#------------------------

#Write a function to find the sum of digits of a number
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10       # last digit nikalna
        total += digit            # total mein add karna
        number = number // 10     # last digit hata dena
    return total
num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum_of_digits(num)}")
