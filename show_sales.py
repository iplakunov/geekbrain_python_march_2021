"""
Плакунов Иван - Python.Март2021.6урок.6задание

"""
import sys


def my_func(my_args=0):
    len_args = 1

    with open('bakery.csv', encoding='utf-8') as f:
        if len(my_args) == 1:
            for line in f:
                print(line.strip())
        elif len(my_args) == 2:
            for line in f:
                if len_args < (int(my_args[1])):
                    line.strip()
                    len_args += 1
                else:
                    print(line.strip())
        else:
            for line in f:
                if (int(my_args[1])-1) < len_args <= (int(my_args[2])):
                    print(line.strip())
                    len_args += 1
                else:
                    line.strip()
                    len_args += 1


my_func(sys.argv)
