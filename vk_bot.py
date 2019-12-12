#Не терять
# https://vk.com/dev/methods

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

def get_random_id():
    return randint(100000,999999)

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id,  'random_id': get_random_id(), 'message': message})

# API-ключ созданный ранее
token = "5d6230782449ccdafbdff21b22f0c1ca764a568e9de7ce63aff604f693ed5fedbedfad732d9455516ea2a"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            
            print(event)
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")