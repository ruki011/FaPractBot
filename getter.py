from bs4 import BeautifulSoup
import requests

def site1_module():
    response = requests.get("https://www.bolshoi.ru/timetable/").text
    content = BeautifulSoup(response,"lxml")
    
    #Секции с распределением по датам
    sections = content.find_all("div", class_="DATE timetable_content")
    for section in sections:

        #Работа с датой
        date = section.find("div", class_="timetable_content__date")
        date_first = date.find("b", class_="timetable_content__date_date").text
        date_second = date.find("i", class_="timetable_content__date_weekday").text
        #print(date_first, date_second)

        #Находим все представления/выступления в секции (на текущую дату)
        theatres = section.find_all("tr", class_="past_q")
        for theatre in theatres:
            
            #Название выступления
            theatre_name = theatre.find("a", class_="timetable_content__performance_title")
            if theatre_name != None:
                #Если нет названия выступления, то никакую другую информацию уже о нём не получаем
                print("Название:", theatre_name.text)
            
            #Описание выступления
            theatre_description = theatre.find("p", class_="timetable_content__performance_description")
            if theatre_description != None and theatre_description.text != "":
                print("Описание:", theatre_description.text)
            
            #Место и время выступления
            theatre_place_time = theatre.find("td", class_="timetable_content__place")
            if theatre_place_time != None:
                value = theatre_place_time.text.replace("\t","")
                value = value.replace("\n"," ")
                print("Место/время:", value[1:])
            

def site2_module():
    response = requests.get("https://et-cetera.ru/poster/").text

if __name__ == "__main__":
    site1_module()