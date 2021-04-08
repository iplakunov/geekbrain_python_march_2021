"""
Плакунов Иван - Python.Март2021.6урок.1задание

"""


def request_parse(line):
    remote_addr, _, _, _, _, request_type, requested_resource, *argv = line.split(' ')
    return remote_addr, request_type[1:], requested_resource


with open('nginx_logs.txt', encoding='utf-8') as f:
    result = [print(request_parse(i)) for i in f.readlines()]
