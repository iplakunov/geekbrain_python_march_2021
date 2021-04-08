"""
Плакунов Иван - Python.Март2021.6урок.3задание

"""
len_users = 0
len_hobby = 0
with open('users.csv', encoding='utf-8') as f:
    for line in f:
        len_users += 1
with open('hobby.csv', encoding='utf-8') as f:
    for line in f:
        len_hobby += 1
file_1 = open('users.csv', encoding='utf-8')
file_2 = open('hobby.csv', encoding='utf-8')
with open('users_hobby.txt', 'a+', encoding='utf-8') as f:
    if len_users > len_hobby:
        for line in file_1:
            f.writelines(f'\n{line.strip()}: ')
            tempo = file_2.readline().strip()
            if tempo == '':
                f.write('None')
            else:
                f.write(tempo)
    else:
        for line in file_1:
            f.writelines(f'{line.strip()}: ')
            f.write(file_2.readline())
file_1.close()
file_2.close()
