'Абстракция'
class Iphone:
    model_name = None   
    ios_version = None 
    color = None
    release_date = None
    brand_name =  None

    def __init__(self,model_name, ios_version ,color ,release_date ,brand_name):
        self.model_name = model_name
        self.ios_version = ios_version
        self.color = color
        self.release_date = release_date
        self.brand_name = brand_name

    def get_iphone_model_data(self):
        print(f'''Model Name: {self.model_name}
IOS Version: {self.ios_version}
Device Color: {self.color}
Date of Release: {self.release_date}
Brand Name: {self.brand_name}''')

import time
all_users_info = []
questions = ['What iphone model you have? : ',
             'What Ios version you have? : ',
             'What color is your iphone? : ',
             'what is realese data of your iphone? : ',
             'Type Brand Name : ']

while True:
    try:
        users_enter = int(input('Введите количество добавляемых пользователей: '))
        break
    except ValueError:
        print('Вводите Только целые числа: ')
        continue

for user_count in range(users_enter):
    print(f'---Загрузка Данных пользователя {user_count + 1}---')
    
    user_current = []
    
    for count_qst in questions:
        user_current.append(input((count_qst)))

    new_iphone = Iphone(*user_current)
    all_users_info.append(new_iphone)
    print('\n')

for load in range(0,101,10):
    if load != 100:
        print(f'\r---Загрузка всех данных: {load}%---', end='')
        time.sleep(0.15*users_enter)
    elif load == 100:
        print(f'\r---Загрузка всех данных: Завершенно!---')
        input("Нажмите Enter чтоб продолжить . . .")

print(f'\n---Список Всех Пользователей---')
for outcount, phone in enumerate(all_users_info, 1):
    print('\n')
    print(f'---User {outcount}---')
    phone.get_iphone_model_data()

# новые методы - для меня , enumerate позволяет получить и индекс и знечение при переборе for
# for phone, outcount in enumerate(all_users_info, 1):
#что стоит закрепить тк по кд забывал - 
# добавление списка в список и индексация списка в списке
# new_iphone = iphone(user_current[0],user_current[1],user_current[2],user_current[3],user_current[4])
#     all_users_info.append(new_iphone)
# также стоит более осмысленно называть переменные тк в них путаюсь оссобено при создании переменой для перебора for
#также сам пришел к тому что надо было использовать словари вместо списков (НУЖНО ПОВТОРИТЬ СЛОВАРИ)
# 
# code review от нейронки: 
#
# 1. Именование (Стандарт PEP 8)

# • Классы с большой буквы: Имя класса должно быть Iphone, а не iphone. Это сразу отличает класс от обычных переменных и функций.
# • Понятные переменные в циклах: Вместо абстрактных get, load, outcount используйте говорящие имена: user_index, progress, user_number, phone_object. Когда код разрастется, вы не запутаетесь.

# 2. Распаковка аргументов (Красивый финт)

# Вместо длинной строки:
# python
# new_iphone = iphone(user_current[0], user_current[1], user_current[2], ...)
# Используйте код с осторожностью.
# Использована звезда: Iphone(*user_current). Звездочка * автоматически берет элементы списка по порядку и подставляет их в __init__. Это избавляет от ручного прописывания индексов.

# 3. Удаление лишнего "мусора" из класса

# Убраны строки model_name = None перед __init__. В Python свойства создаются внутри __init__ через self.название = значение.

# 4. Исправление enumerate

# python
# for user_number, phone_object in enumerate(all_users_info, 1):
# Используйте код с осторожностью.
# Теперь user_number — это число (1, 2, 3...), а phone_object — сам экземпляр класса, у которого мы успешно вызываем метод.