# Variable declaration and assignment
name = 'Mwikali' 
age = 16
salary = 80000.00
# print(name, age, salary)

my_name = 'Mwiks'
myName = 'Mwiks1'
MyName = 'Mwiks2'
MAX_SIZE = 15

# Working with Lists
students = ['Ingavi','Loyce','Akinyi','Ronny', 1, 2, 3, {'name':'Mwikali'},"Calvin"]
# students.insert(3, 'Winfred')
# students.append('Sharon')
students.pop()
# students.pop(2)
# students.remove('Calvin')
# print(students)
# print(len(students))
# print(students[::-1])

mentors = ['Diana', 'Asha']
mentors.pop()
# print(mentors)

new_list = students + mentors
# print(new_list)

students.extend(mentors)
staff = ['Mary','Biwott','Silas']
staff.extend(mentors)
# mentors.extend(staff)
# print(mentors)

#user input and ouput
# num1 = input('Enter first number')
# num2 = input('Enter second number')

# sum_of_2 = int(num1) + int(num2)

# print('Sum {0} and {1} is {1}'.format(num1, num2,sum_of_2))
# print(sum_of_2)

# name = input('What is your name? ')

# print('Hello, ' + name)

#while loop
# count = 0
# while count < 5:
#     print('Count is:', count)
#     count += 1

# user_input = None
# while user_input not in ['y', 'n']:
#     user_input = input('Do you want to continue? (y/n): ')
#     if user_input not in ['y', 'n']:
#         print('Invalid input. Please enter y for yes and n for no')

#break statement
# count = 0
# while count < 5:
#     print('Count is: ', count)
#     if count == 3:
#         break
#     count += 1 

# data = [27, 80,-1, 98, 23, 67]
# for d in data:
#     if d == -1:
#         print('Invalid data found')
#         break
#     print(f"Data: {d}")

# continue statement
# count = 0
# while count < 5:
#     count += 1 
#     if count == 3:
#         continue
#     print('Count is: ', count)

data = [27, 80,-1, 98, 23,-2, 67, -7]
# count = 0
# for d in data:
#     # count += 1
#     if d < 0 and d > -10:
#         continue
#     print(f"Data: {d}")

#nested loops
# colors = ['Red', 'White','Black']
 
# for first_color in colors:
#     for second_color in colors:
#         print(first_color, "+" , second_color)

# for day in range(1,3):
#     print(day)
#     for hour in range(1, 25):
#         print(hour)

#iterate independently
# list1 = [1,2,3]
# list2 = ['a','b','c']

# for number in list1:
#     for letter in list2:
#         print(f"Number: {number}, Letter:{letter}")

# zip function
# list1 = [1,2,3,4]
# list2 = ['a','b','c','d']

# for number, letter in zip(list1, list2):
#     print(f"Number: {number}, Letter:{letter}")

# students = ['Ingavi', 'Myra', 'Carol', 'William','Josephine','Sharon']
# numbers = [1,2,3,4,5,6]

# for index, student in zip(numbers, students):
#     print(f"{index}. {student}")

# enumerate function
# students = ['Ingavi', 'Myra', 'Carol', 'William','Josephine','Sharon']
# # numbers = [1,2,3,4,5,6]
# for index, student in enumerate(students, start=1):
#     print(index,student)

# creating functions
# def greet_person(name):
#     greeting = 'Hi ' + name
#     return greeting

# message = greet_person('Joan')
# print(message)

# def greet():

#     print('Hello World')
# greet()

# def sum():
#     total = 20 + 40

#     print(total)
# sum()

# def sum_user_input():
#     num1 = input('Enter first number: ')
#     num2 = input('Enter second number: ')


#     result = num1 + num2

#     return result

# print('The sum is:',sum_user_input())

# Describe why NumPy is used at times over standard Python
# Instantiate a NumPy array with specified values
# Use broadcasting to perform a math operation on an entire NumPy array


import numpy as np

# arr = np.array([1,2,3,4,5])
# # print(arr)

# print(arr * 2)

# DRY
# Use broadcasting to perform a math operation on an entire numpy array
# Perform vector and matrix operations with numpy
# Access the shape of a numpy array
# Use indexing with numpy arrays

# new_array = np.array([2,4,6,8])
# print(new_array/2)

# new_array = np.array([2,4,6,8])
new_array2 = np.array([10,12,14,16,18])

# print(new_array - new_array2)

# matrix = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6,9], [7,8,0] ,[2,4,1]])

# print(np.dot(matrix, matrix2))

# shape = matrix2.shape
# print(shape)

element = matrix2[-1]
print(element)



