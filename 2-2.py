"""
Плакунов Иван - Python.Март2021.2урок.2задание

Это было очень жёстко. Делал часов 6, вроде работает, даже если температуру поднять или сделать минусовой

"""
answer = 'y'
while True:
    my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    print("Итак, заблаговременно я позаботился и накал некий список, покажу тебе его:", my_list)
    i = 0
    while i < len(my_list):
        if my_list[i].isdigit() or my_list[i].find('+') != -1 or my_list[i].find('-') != -1:
            my_list[i] = my_list[i].zfill(2)
            if my_list[i].find('+') != -1 or my_list[i].find('-') != -1:
                my_list[i] = my_list[i].zfill(3)
            my_list.insert(i + 1, '"')
            my_list.insert(i, '"')
            i += 2
        i += 1
    my_string = ''
    i = 0
    while i < len(my_list):
        if my_list[i].isdigit() or my_list[i].find('+') != -1 or my_list[i].find('-') != -1:
            my_string += f'{my_list[i]}'
        elif my_list[i] == '"':
            if my_list[i-1].isdigit() or my_list[i-1].find('+') != -1 or my_list[i-1].find('-') != -1:
                my_string += f'{my_list[i]} '
            else:
                my_string += f'{my_list[i]}'
        else:
            my_string += f'{my_list[i]} '
        i += 1
    print(f'После хитрых манипуляций покажу тебе наш обработанный список: \n {my_list}, type {type(my_list)}')
    print("Сформируем из него строку:", my_string)
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer != 'y':
        break
