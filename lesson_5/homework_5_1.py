# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая
# строка.

with open("data.txt", "w", encoding="utf-8") as f:
    data = []
    while True:
        string = input()
        if not string:
            break
        data.append(string)
    f.writelines(string)
