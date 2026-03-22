# print ("Hello, World!")
# name = input("What is your name ?")
# print ("Hello, " + name + "!")

# name2 = input("What is your name ?")
# age = input("What is your age?")
# print ("Hello, " + name2 + "! You are " + age + " years old.")

# Variables 
# a= 12 + 5
# print (a)


# DECIMAL NUMBERS
# from decimal import Decimal
# a = Decimal('0.1') + Decimal('0.2')
# print (a)
# -------------------------------------------
#  F-STRINGS
# s1 = 'Hello'
# s2 = 'World'
# joined = f'{s1} {s2}'
# print (joined)
# ------------------------------------------

# ** operator

# sidea = 23
# sideb = 34
# hypotenuse = (sidea**2 + sideb**2) ** 0.5
# print (hypotenuse)


# --------------------------------
# n = 5000

# hours = n // (60 * 60)
# minutes = (n - hours * 60 * 60) // 60
# seconds = n - hours * 60 * 60 - minutes * 60
# print(hours)
# print(minutes)
# print(seconds)
# -----------------------------------------

# a%b

# a = 23
# b = 12
# print (a % b)

# number = 10
# print (number % 2)

# if 10 % 2 == 0:
#     print ("Even")

# -------------------------------

# ratio = 10
# result = 8* ratio + 12 * ratio **2
# print (result)

# distance evklid
# x1= 12
# y1= 12
# x2=11
# y2= 54
# distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
# print (distance)

# -------------------------------
#  changing a variable
# a = float(input("Enter a number: "))
# b = 4*a
# print (b)

# --------------------------------
# Task 1 
# price_per_croissant = 1.04
# price_per_glass = 2.09
# price_per_coffee_pack = 3.12

# num_croissants = int(input("How many croissants do you want to buy? "))
# num_glasses = int(input("How many glasses do you want to buy? "))
# num_coffee_packs = int(input("How many coffee packs do you want to buy? "))

# total_cost = (num_croissants * price_per_croissant) + \
#              (num_glasses * price_per_glass) + \
#              (num_coffee_packs * price_per_coffee_pack)

# total_dollars = int (total_cost)
# total_cents = int ((total_cost - total_dollars) * 100)

# print (f"You need to pay {total_dollars} dollars and {total_cents} cents.")


#Collections
# LISTS
# my_list = [1, 2, 3, 4, 5]
# print (my_list)

# # Tuples
# my_tuple = (1,2,3,4,5)
# print (my_tuple)

# # Sets
# my_set = {1,2,3,4,5}
# print (my_set)

# Dicts 
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print (my_dict)

# append()
# my_list = []
# my_list.append("первый")
# my_list.append("второй")
# my_list.append("третий")
# print(my_list)

# remove()
# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)
# print(my_list)

# indexing
# my_list_q = [10, 20, 30, 40, 50]
# first_number = my_list_q[0]
# print(first_number)
# last_number = my_list_q[-1]
# print(last_number)

# changing values in a list
# my_list = [1, 2, 3, 4, 5]
# my_list[2] = 99
# print(my_list)

# pop()
# my_list = [1, 2, 3, 4, 5]
# popped_value = my_list.pop(2)
# print(popped_value)
# print(my_list)

# insert()
# my_list = [1, 2, 4, 5]
# my_list.insert(2, 3)
# print(my_list)

# count()
# my_list =[1,2,3,2,3,4,1]
# print(my_list.count(2))
# print (my_list.count(3))

# index()
# my_list = [10, 20, 30, 40, 50]
# print(my_list.index(30))

# clear()
# my_list = [1, 2, 3, 4, 5]
# my_list.clear()
# print(my_list)
