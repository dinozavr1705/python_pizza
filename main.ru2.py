import json

file_path = 'lol.json'
library = []

x = input('Введите имя автора: ')
y = input('Введите год выпуска: ')
a = input('Введите имя книги: ')
b = input('Введите количество страниц: ')

new_book = {
    "title": a,
    "year": y,
    "pages": b,
    "author": x
}

try:
    with open(file_path, 'r') as file:
        library = json.load(file)
except FileNotFoundError:
    print("Файл не найден.")
library.append(new_book)

with open(file_path, 'w') as file:
    json.dump(library, file, indent=4)

print("Данные о новой книге успешно добавлены!")