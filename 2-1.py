"""
Плакунов Иван - Python.Март2021.2урок.1задание

Задание было либо очень простым, либо я не понял

"""
answer = 'y'
while True:
    one = 15 * 3
    two = 15 / 3
    three = 15 // 2
    four = 15 ** 2
    print(f'Значение вычисления 1: {one}. Тип первого вычисления:{type(one)}\n'
          f'Значение вычисления 2: {two}. Тип второго вычисления:{type(two)}\n'
          f'Значение вычисления 3: {three}. Тип третьего вычисления:{type(three)}\n'
          f'Значение вычисления 4: {four}. Тип четвертого вычисления:{type(four)}\n')
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer != 'y':
        break
