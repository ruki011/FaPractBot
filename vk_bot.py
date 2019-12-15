from random import randint

import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

import formater1
import formater2
import parser1
import parser2


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'random_id': get_random_id(), 'message': message})


# API-ключ созданный ранее
token = "7040812eb75fc3fa0e95c31f47557a16980d3c5f4975a2edc364b1de72c073fb5fff7306e242b653ffa96"

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

                universal_dict[event.user_id] = {}
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('bolshoi ru', color=VkKeyboardColor.DEFAULT)
                keyboard.add_button('et-cetera ru', color=VkKeyboardColor.DEFAULT)
                message_str = "Здравствуйте, я подскажу Вам график спектаклей\nДля начала выберите источник, который хотите использовать:"
                vk.method('messages.send',
                          {'user_id': event.user_id, 'random_id': get_random_id(), "keyboard": keyboard.get_keyboard(),
                           'message': message_str})

            elif request == "bolshoi ru" and event.user_id in universal_dict:
                universal_dict[event.user_id]["source"] = 1
                write_msg(event.user_id, "Введите месяц и год в формате 01/2020 для отображения расписания на конкретный месяц или день месяц и год в формате 01/01/2020 для отображения расписания на конкретный день")

            elif request == "et-cetera ru" and event.user_id in universal_dict:
                universal_dict[event.user_id]["source"] = 2
                write_msg(event.user_id, "Введите месяц и год в формате 01/2020 для отображения расписания на конкретный месяц или день месяц и год в формате 01/01/2020 для отображения расписания на конкретный день")
            else:
                if event.user_id in universal_dict:
                    
                    #Если введенная дата является корректной
                    if (len(request) == 7 and "/" in request) or (len(request) == 10 and "/" in request):
                        
                        write_msg(event.user_id, "Получаем данные..")
                        #Если был выбран источник №1
                        if universal_dict[event.user_id]["source"] == 1:
                            result = parser1.parser(request)
                            send_list = formater1.format(result)
                            for s in send_list:
                                write_msg(event.user_id, s)
                        
                        #Иначе если был выбран источник №2
                        elif universal_dict[event.user_id]["source"] == 2:
                            result = parser2.parser(request)
                            send_list = formater2.format(result)
                            for s in send_list:
                                write_msg(event.user_id, s)
                    else:
                        write_msg(event.user_id, "Некорректный ввод даты!")

                    universal_dict.pop(event.user_id, None)
