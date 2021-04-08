"""
Плакунов Иван - Python.Март2021.6урок.6задание

"""
import sys


def my_func(my_args=0):
    if len(my_args) == 1:
        print('Вы не ввели сумму продаж')
    else:
        with open('bakery.csv', 'a+', encoding='utf-8') as f:
            f.write(f'{my_args[1]}\n')


my_func(sys.argv)
