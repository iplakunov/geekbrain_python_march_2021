"""
Плакунов Иван - Python.Март2021.5урок.5задание
Может не так понял задание, сделал так. Хотел замерить время, но операции слишком быстро выполняются,
значение везде было 0.0, поэтому затёр строчки, чтобы не нагружали

"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_for = []
for number in src:
    if src.count(number) <= 1:
        if number not in result_for:
            result_for.append(number)
print(result_for)

# Тут как бы оптимизировал код :)
result_lc = []
[result_lc.append(number) for number in src if src.count(number) <= 1 if number not in result_lc]
print(result_lc)
