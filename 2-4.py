"""
Плакунов Иван - Python.Март2021.2урок.4задание

"""
answer = 'y'
while True:
    my_staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                'директор аэлита']
    print(f'В общем, есть рандомный набор должностей и имён, вот он:{my_staff},\n А теперь поздороваемся '
          f'с каждым по имени:')
    my_staff_two = ''
    ind = 0
    while ind < len(my_staff):
        for i in my_staff[ind]:
            my_staff_two = my_staff[ind].split(' ')
        print(f'Привет, {my_staff_two[-1].capitalize()}!')
        ind += 1
    print("Ну и выведем список в конце, чтобы убедиться, что с ним всё ок:\n", my_staff)
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer != 'y':
        break
