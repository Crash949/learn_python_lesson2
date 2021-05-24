def ask_user ():
    vopros = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Что получил?": "Отлично"} 
    user_say = input("Введите свой вопрос:\n")
    for bb in vopros.keys():
        if user_say == bb:
            print(vopros.get(bb))
    #c=list(filter(lambda x: vopros[x] in user_say,vopros))
    #print(c)


ask_user()  