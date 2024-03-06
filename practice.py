# 1. Find the Prime Numbers: Write a program that uses a loop to find and print all the prime numbers between 2 and a given number n. 
# Use a for loop for iteration and a break statement to skip non-prime numbers.

# n = int(input())
# for num in range(2, n + 1):
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print(num)

# 2.Temperature Converter: Implement a loop that continuously prompts the user to enter a temperature in Celsius until they enter a specific 
# sentinel value (e.g., -999). For each input, the program should print the equivalent temperature in Fahrenheit. Use a while loop for this task.

# degrees = 100
# user_input = None
# while user_input != degrees:
#     user_input = int(input('Please enter degress: '))
#     print(f'Temperature entered {user_input *33.8} Farenheit')
#     if user_input != degrees:
#         print('Incorrect value!Please input temperature again')
#     else:
#         print('Temperature entered is accurate')

# 3 . Guess the Number Game: Create a simple number guessing game. The program selects a random number between 1 and 100, and the user has to 
# guess the number. The program provides hints ("too high" or "too low") after each guess. Use a while loop to keep the game running until 
# the user guesses correctly, and allow the user to exit the game by typing 0.
# import random

# guess_number = random.randint(1,100)
# while True:
#     user_input = int(input('Enter any number or 0 to exit the game: '))
#     if user_input == guess_number or user_input == 0:
#         print('Game over!')
#         break
#     elif user_input > guess_number:
#         print('Too High')
#     elif user_input < guess_number:
#         print('Too low')
#     else:
#         print('Not a valid number')

# 4. Skip Negative Numbers: Given a list of numbers, write a loop that prints all the numbers in the list except for negative numbers. 
# Use a continue statement to skip the negative numbers
# data = [0,-9,24,10,16,-1,20,56,98]
# for x in data:
#     if x < 0:
#         continue
#     print(x)

# 5.Multiplication Table Printer: Write a program that prints the multiplication table (from 1 to 10) for a number entered by the user. 
# However, use a break statement to end the loop early if the product exceeds 50.
# user_input = int(input('Enter number to print table for: '))
# for number in range(1,11):
#     product = user_input * number
#     if product > 50:
#         break
#     print(f"{number} x {user_input} = {product}")

# 6. FizzBuzz with a Twist: Implement the classic FizzBuzz problem but with a twist. 
# Print the numbers from 1 to n, but for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five, print “FizzBuzz”. However, skip printing anything for numbers that are prime. 
# Use a loop for iteration, a continue statement for primes, and a nested loop or function to check for prime numbers.
# user_input = int(input('Enter your stop number'))
# for i in range(1,user_input+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % i == 0 and i % :
#         continue
#     else:
#         pass

# 6. Collatz Conjecture: Implement a program that takes a positive integer from the user and then applies the Collatz conjecture algorithm to it.
#  The algorithm is: if the number is even, divide it by 2; if it's odd, multiply it by 3 and add 1. Continue applying the algorithm to the result 
# until you reach the number 1. Use a while loop for this task
# user_input = int(input('Enter a number: '))
# while user_input != 1:
#     print(user_input, end=' ')
#     if user_input % 2 == 0:
#         user_input = user_input // 2
#     else:
#         user_input = (user_input * 3) + 1
# print(user_input)

# 7. Character Occurrences Counter: Ask the user to input a string and a specific character. Use a loop to count how many times the specified character
#  appears in the string. Print the count after the loop ends. 

# user_input = str(input('Enter a string: '))
# user_input1 = (input('Enter a character: '))
# count = 0
# for char in user_input:
#     if char == user_input1:
#         count +=1
# print(f"Number of occurences of {char} = {count}")

# 1. Reverse Number: Write a program that takes a positive integer input from the user and prints its digits in reverse order. 
# Use a while loop to extract each digit and construct the reversed number
# user_input = int(input('Enter a positive integer: '))
# reversed_number = 0
# while user_input > 0:
#     digit = user_input % 10
#     reversed_number = reversed_number * 10 + digit
#     user_input //= 10
# print(f"Reversed number: {reversed_number}")

# 2. Odd Number Sum: Write a program using a for or while loop that calculates the sum of all odd numbers between 1 and a given number n (inclusive). 
# Use a continue statement to skip even numbers.

# user_input = int(input('Enter a number: '))
# total = 0
# for i in range(1, user_input+1):
#     if i % 2 == 0:
#         continue
#     total += i
# print(total)
    
# 6. Sum of Digits Until Single Digit: Write a program that takes a non-negative integer and repeatedly adds its digits until the 
# result is a single digit. For example, given the number 38, the process would be 3 + 8 = 11, 1 + 1 = 2. Print the resulting single digit. 
# Use a while loop to perform the digit addition until the number is less than 10
# user_input = int(input('Enter a number: '))
# while user_input > 9:
#     sum_of = sum([int(digit) for digit in str(user_input)])
#     if sum_of < 10:
#         print(sum_of)
#         break
#     else:
#         sum_of = sum([int(digit) for digit in str(sum_of)])
#         print(sum_of)
#         break

# 7. Custom Sequence Generator: Given two integers start and end, write a program that prints a sequence of numbers starting from start to end. 
# However, for numbers divisible by 4, print "Linked", for numbers divisible by 6, print "In", and for numbers divisible by both 4 and 6, print "LinkedIn".
# Use a for loop to iterate through the range and continue statements to manage the custom printing logic.
