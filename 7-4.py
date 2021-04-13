"""
Плакунов Иван - Python.Март2021.7урок.4задание

"""

import os

lot_hundred = 0
lot_thousand = 0
lot_ten_thousand = 0

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if os.path.getsize(f'{dirpath}/{filename}') <= 100:
            lot_hundred += 1
        elif 100 < os.path.getsize(f'{dirpath}/{filename}') <= 1000:
            lot_thousand += 1
        elif 1000 < os.path.getsize(f'{dirpath}/{filename}') <= 10000:
            lot_ten_thousand += 1

my_dict = {'100': lot_hundred, '1 000': lot_thousand, '10 000': lot_ten_thousand}
print(my_dict)
