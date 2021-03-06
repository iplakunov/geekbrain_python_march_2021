"""
Плакунов Иван - Python.Март2021.1урок.1задание

PyCharm выдавал предупреждения, что слишком длинные строчки кода и предлагал перенести, я перенёс, но не знаю как лучше,
поэтому просьба на это не смотреть, буду ждать обратную связь с рекомендацией.

p.S. Так же добавил цикл на подобии do while в С, чтобы при проверке не нужно было перезапускать (может пригодится,
не знаю как вы будете проверять, мне было удобнее)

"""
answer = 'y'
while True:
    user_duration = int(input(
        "Привет, ты можешь ввести любое количество секунд, а я посчитаю сколько это в минутах/часах/днях/месяцах "
        "или даже годах: "))
    minutes_whole = user_duration // 60
    minutes_remainder = user_duration % 60
    hour_whole = minutes_whole // 60
    hour_remainder = minutes_whole % 60
    days_whole = hour_whole // 24
    days_remainder = hour_whole % 24
    month_whole = days_whole // 30
    month_remainder = days_whole % 30
    year_whole = month_whole // 12
    year_remainder = month_whole % 12

    if year_whole != 0:
        print(f"Введёного числа хватило на", year_whole, "г.", year_remainder, "мес.", month_remainder, "дн.",
              days_remainder, "час.", hour_remainder, "мин. и", minutes_remainder, "сек.")
    elif month_whole != 0:
        print(f"Введёного числа хватило на", month_whole, "мес.", month_remainder, "дн.", days_remainder, "час.",
              hour_remainder, "мин. и", minutes_remainder, "сек.")
    elif days_whole != 0:
        print(f"Введёного числа хватило на", days_whole, "дн.", days_remainder, "час.", hour_remainder, "мин. и",
              minutes_remainder, "сек.")
    elif hour_whole != 0:
        print(f"Введёного числа хватило на", hour_whole, "часов", hour_remainder, "минут и", minutes_remainder,
              "секунд")
    elif minutes_whole == 0:
        print(f'Введёного числа хватило на', user_duration, "секунд")
    else:
        print(f"Введёного числа хватило на", minutes_whole, "минут и", minutes_remainder, "секунд")
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer !='y':
        break