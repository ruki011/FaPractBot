import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from random import randint

import parser1
import parser2

import formater1
import formater2

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id,  'random_id': get_random_id(), 'message': message})

# API-ключ созданный ранее
token = "5d6230782449ccdafbdff21b22f0c1ca764a568e9de7ce63aff604f693ed5fedbedfad732d9455516ea2a"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

universal_dict = {}
# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа
            if request == "/start":
                
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('bolshoi ru', color=VkKeyboardColor.DEFAULT)
                keyboard.add_button('et-cetera ru', color=VkKeyboardColor.DEFAULT)
                message_str = "Привет, я подскажу тебе график спектаклей\nДля начала выбери источник, который хочешь использовать:"
                vk.method('messages.send', {'user_id': event.user_id,  'random_id': get_random_id(), "keyboard" : keyboard.get_keyboard(), 'message': message_str})

            elif request == "bolshoi ru":
                write_msg(event.user_id, "Получаем данные..")
                result = parser1.parser()
                send_list = formater1.format(result)
                for s in send_list:
                    write_msg(event.user_id, s)

            elif request == "et-cetera ru":
                universal_dict[event.user_id] = True
                write_msg(event.user_id, "Введите месяц и год в формате 01/2020 для отображения расписания на конкретный период:")
            else:
                if event.user_id in universal_dict:
                    if len(request) == 7 and "/" in request:
                        write_msg(event.user_id, "Получаем данные..")
                        result = parser2.parser(request)
                        send_list = formater2.format(result)
                        for s in send_list:
                            print(s)
                        universal_dict.pop(event.user_id, None)
                    else:
                        write_msg(event.user_id, "Некорректный ввод даты!")
