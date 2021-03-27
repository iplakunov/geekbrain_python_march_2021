"""
Плакунов Иван - Python.Март2021.5урок.1задание

"""


def num_gen(num_max):
    for num in range(1, num_max + 1, 2):
        yield num


my_max = int(input('До скольки? '))
nums = num_gen(my_max)
for _ in range(my_max):
    print(next(nums))
