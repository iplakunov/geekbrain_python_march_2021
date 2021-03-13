"""
Плакунов Иван - Python.Март2021.2урок.5задание

Вывод делал через строки, поэтому дублировалась часть кода, в дальнейшем можно вынести в функцию, а пока не знаю как.
На мой взгляд вывод получился перегруженным и не информативным, в чате рекомендовали отформатировать, чтобы
были <NN> руб <NN> коп, поэтому так.

"""
answer = 'y'
while True:
    my_product_price = [32, 44.65, 54, 7, 64.3, 12, 23.59, 3, 45.0, 84]
    my_string = ''
    for i in my_product_price:
        my_string += f'Цена: {int(i // 1):02} руб. {int(i*100%100):02} коп. '
    print(f'Для начала покажу список, который красиво отформатировал: \n{my_string}\n')
    my_string_sort = ''
    for i in sorted(my_product_price):
        my_string_sort += f'Цена: {int(i // 1):02} руб. {int(i * 100 % 100):02} коп. '
    print(f'Список, который форматнул по возрастанию: \n{my_string_sort}\n')
    print(f'Докажем, что список остался прежним: {my_product_price}\n')
    my_change_product_price = my_product_price
    my_change_product_price.sort(reverse = True)
    my_string_sort_new_list = ''
    for i in my_change_product_price:
        my_string_sort_new_list += f'Цена: {int(i // 1):02} руб. {int(i * 100 % 100):02} коп. '
    print(f'Выведем новый список, отсортированный по убыванию: \n{my_string_sort_new_list}\n')
    print(f'А теперь выведем 5 самых дорогих товаров с минимум кода '
          f'(не форматировал, чтобы использовать минимум кода): {my_change_product_price[:5]}')
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer != 'y':
        break
