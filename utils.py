"""
Плакунов Иван - Python.Март2021.4урок.1задание

"""
from requests import get
from decimal import Decimal
import datetime as dt


def currency_rates(char_code, value = 0):
    my_request = get('http://www.cbr.ru/scripts/XML_daily.asp')
    result_list = my_request.text.split('Valute ID')
    my_func_char_code = 0
    day_temp = result_list[0]
    day = day_temp[60:70].replace('.', '-')
    my_day = dt.datetime.strptime(day, '%d-%m-%Y').date()
    for i in result_list:
        result_list_part = i.split('>')
        el = 0
        while el < len(result_list_part):
            if result_list_part[el] == '<CharCode':
                char_code_in_my_request = result_list_part[el + 1]
                value_in_my_request = result_list_part[el + 7]
                if char_code_in_my_request[:3] == char_code.upper():
                    my_func_char_code = char_code_in_my_request[:3]
                    value = Decimal(value_in_my_request[:5].replace(',', '.'))
            el += 1

    return my_func_char_code, value, my_day
