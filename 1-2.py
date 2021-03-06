"""
Плакунов Иван - Python.Март2021.1урок.2задание

Оставил принты, которыми пользовался для проверки корректности работы алгоритма:
1. Выводит список кубов нечётных чисел до числа, указанного пользователем
2. Выводит каждый элемент, сумма чисел которого делится нацело на 7
3. Выводит сумму элементов из списка выше
4. Выводит изменённый список, увеличив каждый элемент на 17
5. Выводит каждый элемент изменённого списка, сумма чисел которого делится нацело на 7
6. Выводит сумму элементов изменённого списка из списка выше

"""


answer = 'y'
while True:
    my_list = []
    user_count = int(input("Введи число, до какого значения мне возвести все нечётные значения в куб? До 10/100/1000? "))
    ind = 1
    number_odd = 1
    while ind < user_count:
        if (ind % 2) != 0:
            number_odd = ind**3
            my_list.append(number_odd)
        ind += 1
    print(f"Кубы нечётных чисел до", user_count,": \n", my_list)
    ind = 0
    sum_number = 0
    el_from_my_list = 0
    while ind < len(my_list):
        el_from_my_list = my_list[ind]
        sum_number_odd = 0
        while el_from_my_list:
            sum_number_odd += el_from_my_list % 10
            el_from_my_list //= 10
        if sum_number_odd % 7 == 0:
            sum_number += my_list[ind]
            print("Сумма цифр числа делится на 7 без остатка:", my_list[ind])
        ind += 1
    if sum_number != 0:
        print("Их сумма равна:", sum_number)
    else:
        print("Я не нашёл числа, сумма цифр которых делилась бы без остатка на 7")
    for i in range(len(my_list)):
        my_list[i] += 17
    print("\nЭто всё хорошо, конечно, но теперь увеличим каждый элемент списка на 17 и попробуем ещё раз:\n", my_list)
    sum_number = 0
    ind = 0
    while ind < len(my_list):
        el_from_my_list = my_list[ind]
        sum_number_odd = 0
        while el_from_my_list:
            sum_number_odd += el_from_my_list % 10
            el_from_my_list //= 10
        if sum_number_odd % 7 == 0:
            sum_number += my_list[ind]
            print("Сумма цифр числа делится на 7 без остатка:", my_list[ind])
        ind += 1
    if sum_number != 0:
        print("Их сумма равна:", sum_number)
    else:
        print("Я не нашёл числа, сумма цифр которых делилась бы без остатка на 7")
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer !='y':
        break