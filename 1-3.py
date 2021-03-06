"""
Плакунов Иван - Python.Март2021.1урок.3задание

"""

answer = 'y'
while True:
    word =['процент','процента','процентов']
    user_number = int(input("Я умею склонять слово 'процент', введи любую цифру до 20 и я покажу как это: "))
    if user_number == 1:
        print(f"Ты ввёл(а)", user_number, word[0], "\n А вот все склонения, которые я знаю: ", word)
    elif user_number == 2 or user_number == 3 or user_number == 4 or user_number == 5:
        print(f"Ты ввёл(а)", user_number, word[1], "\n А вот все склонения, которые я знаю: ", word)
    elif 0 <= user_number <= 20:
        print(f"Ты ввёл(а)", user_number, word[2], "\n А вот все склонения, которые я знаю: ", word)
    answer = input("Повторим? Если не против, жми 'y' \n")
    if answer !='y':
        break