"""
Плакунов Иван - Python.Март2021.3урок.5задание
Видимо я уже торможу, собрал такие кастыли, но, вроде, работает) документрировать оказалось труднее, чем казалось

"""
from random import choice
answer = 'y'
while True:
    def get_jokes(count, my_if):
        """
        Функция, которая забирает по одному слову из списка, формируя "шутку" из 3 случайных слов 3 разных листов.
        В зависимости от передаваемых значений либо повторяет слова в выводе, либо нет
        nouns, adverbs, adjectives - листы с набором слов, откуда забирает значения
        :param count: принимает интовое число, которое определяет количество "шуток"
        :param my_if: принимает строку, которая если состоит из символа "y", то разрешает повтор слов в "шутках",
            если любой другой - слова не повторяются
        :return: возвращает лист из наборов слов, случайно набранных в списках ниже
        """
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs  = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        if my_if in 'y':
            jok_full = []
            for i in range(count):
                jok = []
                full_data = ''
                jok.append(choice(nouns))
                jok.append(choice(adverbs))
                jok.append(choice(adjectives))
                full_data = ' '.join(jok)
                jok_full.append(full_data)
        else:
            jok_full = []
            for i in range(count):
                jok = []
                full_data = ''
                jok.append(choice(nouns))
                nouns.remove(jok[0])
                jok.append(choice(adverbs))
                adverbs.remove(jok[1])
                jok.append(choice(adjectives))
                adjectives.remove(jok[2])
                full_data = ' '.join(jok)
                jok_full.append(full_data)
        return jok_full


    count_jok = int(input("Привет, я могу рассказывать шутки из набора 3 случайных слов 3 разных списков. "
                          "Сколько тебе рассказать шуток? Введи цифру от 1 до 5: "))
    flag = input("Хорошо, а теперь напиши 'y', если мне можно повторять слова или введи любой символ и тогда "
                 "я не буду повторять слова: ")
    print(f'Вот такие шутки получились:\n {get_jokes(count_jok, flag)}')
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer != 'y':
        break
