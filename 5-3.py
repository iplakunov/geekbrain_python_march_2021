"""
Плакунов Иван - Python.Март2021.5урок.3задание
Перебор элементов в списке делал через расширенную версию зип, для этого импортировал из библиотеки интертулс
Для проверки выводил с типом и до истощения генератора

"""
from itertools import zip_longest

def my_gen(tut, klas):
    if len(tut) <= len(klas):
        my_tutor = zip(tut, klas)
    else:
        my_tutor = zip_longest(tut, klas, fillvalue=None)
    for el in my_tutor:
        yield el


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Petr'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]
result = my_gen(tutors, klasses)
my_print = [print(type(result), next(result)) for _ in range(len(tutors) + 1)]
