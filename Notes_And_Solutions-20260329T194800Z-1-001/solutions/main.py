#!/bin/python3
import math
#ismlar = ["Ali", "Vali", "Gani", "Asad", "Begi"]
#for name in ismlar:
#    print(f"Salom: {name}")

#print(f"It repeated: {len(ismlar)}")

#for i in range(10, 100, 2):
#   print(i**3)
#movies_list = []

#for i in range(1, 5):
#    i = input("Enter favourite movie!  ")
#    movies_list.append(i)
#
#print(movies_list)

#len_of_list = int(input("Enter amount of people you see today:  "))
#friends_list = []
#for i in range(len_of_list):
#    i = input("Enter friend's name ")
#    friends_list.append(i)

#print(friends_list)



#cars_list = ['toyota', 'bmw', 'audi', 'gm', 'alphine', 'maserati']

#for car_name in cars_list:
#    if len(car_name) >= 4:
#       print(car_name.title())
#    elif len(car_name) <= 3:
#       print(car_name.upper())

#for car_name in cars_list:
#    if car_name != 'gm' and car_name != 'bmw':
#        print(car_name.title())
#    else:
#        print(car_name.upper())



#user_name = input("enter name: ")

#if user_name == 'admin':
#   print("good morning administrator")
#else:
#  print(f"good morning {user_name}!")



#numb_f = int(input("Enter two numbs:"))
#numb_s = int(input("Enter two numbs:"))

#if numb_f == numb_s:
#   print("they are equal")
#else:
#    print("they are not equal")

#numb = int(input("Enter any numb  "))

#if numb % 2 == 0:
#   print("numb is even! " )
#else:
#   print("numb is odd! ")


#numb = int(input("Enter number"))

#print(round(numb**(1/2), 2)) if numb>0 else print("Enter positive numb!")

#numb = int(input("Enter numb!"))

#print("Numb is positive!") if numb >=0 else print("Numb is negative!")

#age = int(input("Enter your age:  "))

#if age < 4 or age > 60:
#   print("entrance is free")
#elif age > 4 and age < 18:
#  print("entrance cost: 10.000")
#elif age > 18 and age < 60:
#     print("entrance cost: 20.000")

#numb_f = float(input("enter numb 1: "))
#numb_s = float(input("enter numb 2: "))

#if numb_f == numb_s:
#   print("numbs equal")
#elif numb_f > numb_s:
#   print(f"{numb_f} more than {numb_s}")
#else:
#   print(f"{numb_s} more than {numb_f}")

# products = ['apple', 'water', 'dishes', 'paper', 'sigarets', 'lighter', 'potatoes', 'carrots', 'milk', 'cacao']
# basket = []

# for product in range(5):
#     product = input("Enter name of product: ")
#     basket.append(product)
    
# for product in basket:
#     if product in products:
#        print(f"Product {product} available!")
#     else:
#        print(f"Product {product} is not available!")


    
# products = ['apple', 'water', 'dishes', 'paper', 'sigarets', 'lighter', 'potatoes', 'carrots', 'milk', 'cacao']

# available_prod = []
# non_available_prod = []

# for product in range(5):
#     product = input("Enter product name: ")
#     if product in products:
#         available_prod.append(product)
#     else:
#         non_available_prod.append(product)

# if non_available_prod:
#     print(non_available_prod)
# else:
#     print("All products are available")


# user_names = ['admin', 'king', 'queen', 'darkmaster', 'limon']

# nw_name = input("Enter new name: ")

# if nw_name in user_names:
#     print("This name is not avaible!")
# else:
#     print(f"Welcome {nw_name}!")



# u_numb = int(input("Enter number: "))
# nw_list = []
# for i in range(2, 11):
#     if u_numb % i == 0:
#         nw_list.append(i)
#     else:
#         continue

# print(nw_list)


# car_0 = {'model':'bmw', 'color':'red', 'year':1998}
# car_1 = {'model':'alphine', 'color':'white', 'year':2008}
# car_2 = {'model':'cobalt', 'color':'black', 'year':2019}
# car_3 = {'model':'jeep', 'color':'blue', 'year':2022}

# cars_list = [car_0, car_1, car_2, car_3]

# for car in cars_list:
#     for key, value in car.items():
#         print(f"{car}")



# favourite_food = {
#     'user_1':'pizza',
#     'user_2':'sushi',
#     'user_3':'kfc',
#     'user_4':'fri',
#     'user_5':'icecream',
#     'user_6':'soup',
#     'user_7':'salat'
# }

# for key, item in favourite_food.items():
#     print(f"{key} favourite food: {item}")



# word_descrpt = {
#     'apple': 'fruit for eat',
#     'cooffee': 'energetic drink for being active',
#     'tea': 'medium taste drink for being relaxed',
#     'vscode': 'universal code editor for creating projects',
#     'mouse':'device for managing and using laptop or pc '
# }

# word = input("Enter word: ")

# if word in word_descrpt.keys():
#     print(word_descrpt.get(word))
# else:
#     print("there is no description!")



# word_descrpt = {
#     'apple': 'fruit for eat',
#     'cooffee': 'energetic drink for being active',
#     'tea': 'medium taste drink for being relaxed',
#     'vscode': 'universal code editor for creating projects',
#     'mouse':'device for managing and using laptop or pc '
# }
# for i in word_descrpt:
#     print(sorted(i))



# books = []
# while True:
#     book_name = input("Enter book name: ")
#     books.append(book_name)
#     if book_name == 'exit':
#         break
# print(books)

# flag = True
# price=0
# age = ''
# while flag:
#     age=(input("Enter your age:  "))
    
#     if age == 'exit' or age == 'quit':
#        flag = False
#     else:
#         price = int(age)
#         if price <= 7:
#             price=2.000
#         elif price > 7 and price <= 18:
#             price=3.000
#         elif price > 18 and price <= 65:
#             price=10.000
#         else:
#             price=0
#         print(f"Narh: {price}")

    
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
   
#     if qiymat.capitalize()=='Exit':
#         break
#     else:
#         son = int(qiymat)
#         if son<0:
#             continue
#         ildiz = float(son)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")



# products = []
# while True:
#     new_product = input("Enter product name:")
#     if new_product == 'exit':
#        break
#     else:
#         products.append(new_product)

# print(products)


# price_prodct = {}

# while True:
#     product = input("Enter product name: ")
#     if product == 'exit':
#         break
#     else:
#         price = float(input(f"Enter price of {product}: "))
#         price_prodct[product] = price
# print(price_prodct)            


# m_products = {'apple':10.000, 'banana':21.000, 'carrot':12.000}
# c_products = ['apple', 'coke', 'banana']
# while c_products:
#     for prodct in c_products:
#         if prodct in m_products.keys():
#             print(f"{prodct.capitalize()}: {m_products[prodct]}")
#             c_products.remove(prodct)
#         else:
#             print(f"{prodct.capitalize()} does not exist!")
#             c_products.remove(prodct)

    
# m_products = {'apple':10.000, 'banana':21.000, 'carrot':12.000}
# c_products = ['apple', 'coke', 'banana']
# while c_products:
#         prodct = c_products.pop()
#         if prodct in m_products.keys():
#             print(f"{prodct.capitalize()}: {m_products[prodct]}")
#         else:
#             print(f"{prodct.capitalize()} does not exist!")



# def counter(name, age, current_year=2026):
#     y_of_born=current_year-age
#     print(f"{name.title()}: Age:{age}, Year of born:{y_of_born}")


# name = input("What's your name?")
# age = int(input("How old are you?"))

# counter(name, age)


# def calc(number):
#     print(f"{number**2}, {number**3}")

# number=int(input("Enter any number: "))
# calc(number)


# def analitic(number):
#     if number >=0:
#        print(f"{number} Positive")
#     else:
#         print(f"{number} Negative")

# number=int(input("Enter numb: "))
# analitic(number)


# def odd_even(number):
#     if number%2==0:
#         print(f"{number} is even!")
#     else:
#         print(f"{number} is odd!")

# number=int(inpu t("Enter numb: "))

# odd_even(number)


# def max_min(f_num, s_num):
#     if f_num>s_num:
#         print(f"{f_num} is max")
#     elif f_num<s_num:
#         print(f"{s_num} is max")
#     else:
#         print("They are equal!")

# f_number=int(input("Enter numb: "))
# s_number=int(input("Enter numb: "))

# max_min(f_number, s_number)


# def delitel(number):
#     for x in range(2, 11):
#         if number%x==0:
#             print(x)
#         else:
#             continue

# number=int(input("Enter numb: "))

# delitel(number)



# def personal_i(ismi, familiyasi, tugilgan_yili, tugilgan_joyi, email_manzili=None,  telefon_raqamini=None, current_year = 2026):
#     age = int(current_year-tugilgan_yili)
    
#     data = {
        
#         'ism':ismi,
#         'familiya':familiyasi,
#         'year_b':tugilgan_yili,
#         'place_b':tugilgan_joyi,
#         'email':email_manzili,
#         'phone':telefon_raqamini,
#         'age':age
#     }
#     if  data['email'] and data['phone']:
#         f_data = f"{data['ism']} {data['familiya']} {data['year_b']} {data['place_b']} {data['email']} {data['phone']} {data['age']}"
#     else:
#         f_data = f"{data['ism']} {data['familiya']} {data['year_b']} {data['place_b']} {data['age']}"
    

#     return f_data
# personal_info_list=[]
# while True:
#         flag = input("Do you want to continue or not: ")
#         if flag=='y':
#             name = input("Enter name: ")
#             surname = input("Enter surname: ")
#             year_of_bith = int(input("Enter yearth of birth:  "))
#             place_of_birth = input("Enter place of birth: ")
#             email = input("Enter email:  ")
#             phone_number = input("Enter phone number: ")
#             final = personal_i(name, surname, year_of_bith, place_of_birth, email, phone_number)
#             personal_info_list.append(final)
#         else:
#             break

# print(personal_info_list)


# def find_m(numbers):
#     max_ = max(numbers)
#     return max_

# numbers = []
# for i in range(3):
#     i = int(input("Enter number: "))
#     numbers.append(i)

# result =  find_m(numbers)
# print(result)


# def round(radius, pi=3.14):
#     diametr = radius * 2
#     lenth = 2 * pi * radius
#     square = pi * (radius**2)

#     return diametr, lenth, square, radius


# while True:
#      radius = input("Enter radius: ")
#      if radius!='stop':
#           radius = float(radius)
#           result = round(radius)
#           print(result)
#      else:
#           break


# def period(start, end):
#     numbers_list=[]
#     for i in range(start, end):
#        if i > 0 and i%2!=0:
#            numbers_list.append(i)
#        else:
#            continue
#     return numbers_list

# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))

# result = period(start, end)
# print(result)



# def fibonachi(lenth):
#     f_list = []
#     for i in range(lenth):
#         if i == 0 or i == 1:
#             f_list.append(i)
#         else:
#             f_list.append(f_list[i-1]+f_list[i-2])    
#     return f_list

# result = fibonachi(30)
# print(result)


# def first_letter(matn):
#     new_list = []
#     for i in matn:
#         new_list.append(i.capitalize())
#     return new_list     

# matn = ["text one", "text  two", "text three"]

# result = first_letter(matn)
# print(matn)
# print(result)


def first_letter_v2(matn):
    while matn:
        text = matn.pop()
        matn.append(text.title())
    return matn

matn = ["text one", "text  two", "text three"]

result = first_letter_v2(matn[:])
print(matn)
print(result)