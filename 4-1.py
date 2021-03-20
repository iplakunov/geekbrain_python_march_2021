"""
Плакунов Иван - Python.Март2021.4урок.1задание


"""
import utils
import sys


a = utils.currency_rates(sys.argv[1])
if a[1] == 0:
    print('Запрашиваемую валюту не нашёл')
else:
    print(f'На {a[2]} стоимость валюты {a[0]} равна {a[1]}')
