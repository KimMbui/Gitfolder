#                                   Variables
# #different types of variables (left side of the (=) is the variable, the right side is the value)
#
#                           #list is donated using square brackets []
# fruits = ["Banana", "oranges", "apples"]
#
# #left side uses lower case
# integers = 23
#
#
# decimals = 23.90
# full_name = "The Richie"
# dcm = 65.90
#
#                          #This is a string (cover with a quotation mark)
# name = "Richie"
# age = 19
#
# name, age = "Richie", 19
# #upper () makes value upper case
# print(name.upper())
#
#                                         lower () makes value lower case
# print(name.lower())
#
#
# #This is an integer (a whole number)
# num = 87
#
#                                  #A list (Store a list in square brackets)
#
# fruits = ["Banana", "oranges", "apples"]
# commodities = ["soap",15,37.90,"juice"]
# print(fruits,commodities)
#

#                            #If-Elif-Else statement( else can be combined with an if)
# num = 100
# if num:
#     print(num)
#
#                                 #Else statement is an optional statement
# num = 89,100
# var = 23
# if num:
#     print("This is a true expression value")
#     print(num)
# else:
#     print("not a number")
#     print(num)
#     print(var)
# print("That was awesome!")
#
# #Elif used to check multiple expressions (happens when there is an if statement)(use IF as the first expression)
# # (else used as the last statement
# num = 200
# if num == 300:
#     print("This is False")
#     print(num)
# elif num == 150:
#     print("This is False")
#     print(num)
# elif num == 1000:
#     print("This is False")
#     print(num)
# elif num == 900:
#     print(num)
# else:
#     print('This is not the number')

#                                         Loop & For Loop
# A loop statement used to execute a statement and a group of statements multiple times looping through
# different signs  meanings in python
# + : concatenate
# % : modulator divisibility
# * : multiplication

#                                            The FOR loop
# movies = ["Avengers", "Spiderman", "Thor"]
# for movie in movies:
#     print(movie)
#
# for letter in 'marvel':
#     print(letter)

#                                    Using else statement with a FOR loop
# num = []
# for num in range(10, 20):
#     for i in range(2, num):
#         if num%i == 0:
#             x = num/i
#             print(num, i, x)
#             break
#         else:
#             print(num)

#                                            indexing & Slicing

# Indexing is used to obtain individual elements. (used to get the position)
movies = ["cars", "frozen", "ice age", "rio"]
print(movies.index('cars'))

#                       Slicing: Slicing is used to obtain a sequence of elements using its position
# Indexing and Slicing can be done in Python Sequences types like list, string, tuple, range objects

# movies = ["cars", "frozen", "ice age", "rio"]
# print(movies[0])  # slicing an item from its position
#
# # Quiz:
# # identify the item in position 1.
#
# print(movies[1])
#
# # Quiz:
# # identify the item in position -1. (negative position starts from the right to left, 0 position starts from left)
# print(movies[-1])

# # Quiz:
# # Find the index value(position value) of frozen
print(movies.index('ice age'))
