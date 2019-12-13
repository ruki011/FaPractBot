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
        print(date_first, date_second)
        #print(section)

        #Находим все представления/выступления в секции (на текущую дату)
        theatres = section.find_all("tr", class_="past_q")
        for theatre in theatres:
            
            print(theatre.text)
            
            

