from bs4 import BeautifulSoup
import requests

def site1_module():

    theatre_dict = {}
    response = requests.get("https://www.bolshoi.ru/timetable/").text
    content = BeautifulSoup(response,"lxml")
    
    #Секции с распределением по датам
    sections = content.find_all("div", class_="DATE timetable_content")
    for section in sections:

        #Работа с датой
        date = section.find("div", class_="timetable_content__date")
        date_first = date.find("b", class_="timetable_content__date_date").text
        date_second = date.find("i", class_="timetable_content__date_weekday").text
        date_string = date_first+", "+date_second
        theatre_dict[date_string] = {}

        #Словарь для временного хранения данных
        locale_list = []

        #Находим все представления/выступления в секции (на текущую дату)
        theatres = section.find_all("tr", class_="past_q")
        for theatre in theatres:
            
            locale_dict = {"name": None, "description" : None, "place&time" : None}
            processing_flag = False
            #Название выступления
            theatre_name = theatre.find("a", class_="timetable_content__performance_title")
            if theatre_name != None:
                locale_dict["name"] = theatre_name.text
                processing_flag = True

            #Если есть название выступления, то продолжаем работу
            if processing_flag == True:
                #Описание выступления
                theatre_description = theatre.find("p", class_="timetable_content__performance_description")
                if theatre_description != None and theatre_description.text != "":
                    locale_dict["description"] = theatre_description.text
                
                #Место и время выступления
                theatre_place_time = theatre.find("td", class_="timetable_content__place")
                if theatre_place_time != None:
                    value = theatre_place_time.text.replace("\t","")
                    value = value.replace("\n"," ")
                    locale_dict["place&time"] = value[1:]
                locale_list.append(locale_dict)

        theatre_dict[date_string] = {"names": locale_list}
    print(theatre_dict)


            
def site2_module():

    #theatre_dict = {}
    
    #print("https://et-cetera.ru/poster/?month=2&year=2020") - динамическая ссылка
    response = requests.get("https://et-cetera.ru/poster/").text
    content = BeautifulSoup(response,"lxml")
    banners = content.find_all("td", class_="day withShow")
    for banner in banners:

        #Название театра
        banner_title = content.find("div", class_="banner")
        check = banner_title.find("p")
        print(check)
        #for c in check:
        #    print(c)
        value = banner_title.text.replace("\t","")
        value = value.replace("\n"," ")
        #print(value)


if __name__ == "__main__":
    site2_module()