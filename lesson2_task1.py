def vozrast(age):
    if 0<=age<=2:
        return 'Вы недавно родились'
    elif 3<=age<=6:
        return 'Вы в садике'
    elif 7<=age<=18:
        return 'Вы школьник'
    elif 19<=age<=22:
        return 'Вы студент'
    elif 23<=age<=65:
        return 'Вы работяга'
    else:
        return 'Вы пенсионер'

c = int(input('Введите ваш возраст\n'))
print(vozrast(c))