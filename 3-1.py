"""
Плакунов Иван - Python.Март2021.3урок.1задание
Делал через словарь, занёс его в функцию, тк делал сразу после занятия, не мог вспомнить где лучше объявить:
до функции или внутри, сделал внутри.

"""
answer = 'y'
while True:
    def num_translate_adv(num):
        my_dict = {'one': 'один',
                   'One': 'Один',
                   'two': 'два',
                   'Two': 'Два',
                   'three': 'три',
                   'Three': 'Три',
                   'four': 'четыре',
                   'Four': 'Четыре',
                   'five': 'пять',
                   'Five': 'Пять',
                   'six': 'шесть',
                   'Six': 'Шесть',
                   'seven': 'семь',
                   'Seven': 'Семь',
                   'eight': 'восемь',
                   'Eight': 'Восемь',
                   'nine': 'девять',
                   'Nine': 'Девять',
                   'ten': 'десять',
                   'Ten': 'Десять'}
        print(f'{my_dict.get(num)}')
    num_translate_adv(input("Write english num: "))
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer != 'y':
        break
