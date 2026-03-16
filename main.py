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
price_per_croissant = 1.04
price_per_glass = 2.09
price_per_coffee_pack = 3.12

num_croissants = int(input("How many croissants do you want to buy? "))
num_glasses = int(input("How many glasses do you want to buy? "))
num_coffee_packs = int(input("How many coffee packs do you want to buy? "))

total_cost = (num_croissants * price_per_croissant) + \
             (num_glasses * price_per_glass) + \
             (num_coffee_packs * price_per_coffee_pack)

total_dollars = int (total_cost)
total_cents = int ((total_cost - total_dollars) * 100)

print (f"You need to pay {total_dollars} dollars and {total_cents} cents.")