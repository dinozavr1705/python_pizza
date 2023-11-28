
m = 'да'
c = 0

import json


def remove_item_from_cart(item_name):
    file_path = 'pizzeria.JSON'

    try:
        with open(file_path, 'r') as file:
            pizzeria = json.load(file)
    except FileNotFoundError:
        print("Файл не найден.")
        return

    total_price = 0

    for item in pizzeria:
        if item["name"] == item_name:
            price = item["price"]
            total_price += price
            pizzeria.remove(item)

    with open(file_path, "w") as file:
        json.dump(pizzeria, file, indent=4)

    print(f"Товар удален из корзины! Вычитано {total_price} фазкоинов.")

    print("Товар удален из корзины!")
while m!='нет':
 file_path = 'корзина.JSON'
 library = []
 print('Hi nigger')
 print("Какое блюдо хотите добавить в корзину?:"
           "1)Пицца 4 сыра"
           "2)Пицца Пепперони"
          "3)Шаурма Deluxe")
 n = int(input('нажмите на цифру соответсвующую товару'))
 y = "without"
 a = 0
 b = 0
 x ="no"
 if n == 1:
     print('это будет стоить 500 фазкоинов ')
     x ="Pizza 4 cheese"
     b = 500
 elif n == 2:
     print('это будет стоить 600 фазкоинов')
     x = "Pizza Pepperoni"
     b = 600
 elif n == 3:
     "это будет стоить 400 фазкоинов"
     b = 400
 a = str(input("Вы будете добавлять приправы?"))
 if a =="да":
         print('какую приправу добавлять?'
               '1)перец'
               '2)кетчуп'
               '3)горчица'
               '4)кетчунез')
         l = int(input('укажите номер приприправы'))
         if l == 1:
             y ="paper"
             b = b + 100
         elif l == 2:
             y ="ketchup"
             b = b + 150
         elif l == 3:
             y ="mustar"
             b = b + 200
         elif l == 4:
             y ="ketchunez"
             b = b + 120
 else:
     y ="without"
 new_pizza = {
    "name": x,
    "cost": b,
    "spices":y
 }

 try:
    with open(file_path, 'r') as file:
        pizzeria = json.load(file)
 except FileNotFoundError:
    print("Файл не найден.")
 pizzeria.append(new_pizza)

 with open(file_path, 'w') as file:
    json.dump(pizzeria, file, indent=4)

 print("Пицца добавлена в корзину!")
 c = c + b
 m = str(input('Подолжать покупку?'))
k = str(input('вы хотите удалить какие - нибудь товары?'))
if k =='нет':
    print(f'это будет стоить {c}')
    v = str(input('оплата наличными или картой?'))
    if v == 'картой':
        print('все было успешно оплачено')
    elif v == 'наличными':
        g = int(input('сколько вы хотите заплатить?'))
        if g > c:
            print(f'ваша сдача составляет {g - c}')
        elif g == c:
            print('покупка оплачена успешно')
        else:
            print('здесь не хватает')
else:
    n = str(input('что вы хотите удалить?'))
    remove_item_from_cart(n)
    print(f'это будет стоить {c}')
    v = str(input('оплата наличными или картой?'))
    if v == 'картой':
        print('все было успешно оплачено')
    elif v == 'наличными':
        g = int(input('сколько вы хотите заплатить?'))
        if g > c:
            print(f'ваша сдача составляет {g - c}')
        elif g == c:
            print('покупка оплачена успешно')
        else:
            print('здесь не хватает')


