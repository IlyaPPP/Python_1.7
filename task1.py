# Задача N°49. Решение в группах
# Создать телефонный справочник c возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например
# имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.

import csv


def show_menu():
    print("1 - Просмотреть телефонную книгу")
    print("2 - Поиск по имени")
    print("3 - Поиск по номеру телефона")
    print("4 - Добавить пользовтеля в первый список 'Phonebook.csv'")
    print("5 - Добавить'")
    return int(input("Введите цифру: "))


def print_result(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)


def get_search_name():
    x = input("Введите имя или фамилию: ")
    return x


def find_by_name(filename: str, x):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if x in line:
                return line


def get_search_number():
    x = input("Введите номер телефона: ")
    return x


def find_by_number(filename, x):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if x in line:
                return line


def get_new_user(filename):
    return


def add_user(filename, data):
    fields = ["Фамилию", "Имя", "Телефон", "Описание"]
    data = ''
    for i in range(4):
        data += (input(f"Введите {fields[i]}: ")) + ", "
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(data)
    return data


def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line))
            data.append(record)
    return data


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            s = ''
            i = i
            data1 = dict(data[i])
            for v in data1.values():
                s += v + ', '
            file.write(f'{s[:-1]}\n')


def get_file_name(b):
    return b


def write_txt(phone_book, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ', '
        file.write(f'{s[:-1]}\n')


def work_with_phonebook():
    choice = show_menu()
    phonebook = read_csv('phonebook.csv')
    phone_book = 'phone_book.txt'

    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user(phone_book)
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phonebook,)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()


work_with_phonebook()
