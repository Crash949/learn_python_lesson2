def hello_user():
    try:
        while True:
            user_say = input('Как дела? ')
            if user_say == 'Хорошо':
                break
            else:
                print('{}'.format(user_say))
    except KeyboardInterrupt:
            print('Пока!') break
                
        
hello_user()      