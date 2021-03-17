"""
Плакунов Иван - Python.Март2021.3урок.3задание

Добавил Анна в конце списка для проверки правильности сортировки
Решил оставить вывод словаря для наглядности формата: ключ : значение \n
15 строка выведет обычный словарь
16 строка выведет словарь, отсортированный по ключам

"""
answer = 'y'
while True:
    def thesaurus(name):
        my_dict = {}
        for i in name:
            if i[0] in my_dict:
                my_dict[i[0]].append(i)
            else:
                my_dict[i[0]] = [i]
        # print(my_dict)
        # print(sorted(my_dict.items(), reverse=False))
        for i in sorted(my_dict.keys()):
            print(i, ':', my_dict[i])


    names = ['Иван', 'Мария', 'Петр', 'Илья', 'Анна']
    thesaurus(names)
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer != 'y':
        break
