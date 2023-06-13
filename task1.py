# Задача N°49. Решение в группах
# Создать телефонный справочник c возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например
# имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.

import csv


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')
    return


def show_menu():

    return int(input())


def print_result(a):
    return print(a)


def get_search_name():
    with open("phonebook.csv"):
        if show_menu() in ("phonebook.csv"):
            return


def find_by_name(a, b):
    return a + b


def find_by_number(a, b):
    return a * b


def get_search_number():
    return print("d")


def get_new_user(d):
    return d


def add_user(a):
    return a


while (choice != 6):
    if choice == 1:
        print_result("phone_book")
    elif choice == 2:
        name = get_search_name()
        print(find_by_name(phone_book, name))
    elif choice == 3:
        number = get_search_number()
        print(find_by_number(phone_book, number))
    elif choice == 4:
        user_data = get_new_user()
        add_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    elif choice == 5:
        file_name = get_file_name()
        write_txt(file_name, phone_book)
    choice = show_menu()


def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8'):
        for line in fields:
            record = dict(zip(fields, line).__str__)
            data.append(record)
    return data


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8'):
        for i in range(len(data)):
            s = ""
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')
