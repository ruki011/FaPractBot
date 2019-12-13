#Добавить JSON отдачу?
from bs4 import BeautifulSoup
import requests

#Функция формирования url на основе даты
def date2url(date):
    month_dict = {
        "01": "1",
        "02": "2",
        "03": "3",
        "04": "4",
        "05": "5",
        "06": "6",
        "07": "7",
        "08": "8",
        "09": "9",
        "10": "10",
        "11": "11",
        "12": "12",
    }

    month, year = date.split("/")  
    if month in month_dict:
        month = month_dict[month]
    
    url = "https://et-cetera.ru/poster/?month="+month+"&year="+year
    return url

#Функция с основной логикой парсинга сайта
def site2(url):

    theatre_dict = {}
    response = requests.get("https://et-cetera.ru/poster/").text
    content = BeautifulSoup(response,"lxml")

    #Баннеры в будние дни
    daily_list = []
    banners = content.find_all("td", class_="day withShow")
    for banner in banners:

        #Название выступления
        banner_titles = banner.find_all("div", class_="banner")
        theatre_list = all_banners(banner_titles)
        daily_list.extend(theatre_list)
    
    #Баннер сегодня
    today_list = []
    today_banners = content.find_all("td", class_="day today withShow")
    for banner in today_banners:
        
        #Название выступления
        banner_titles = banner.find_all("div", class_="banner")
        theatre_list = all_banners(banner_titles)
        today_list.extend(theatre_list)


    #Баннеры в выходные дни
    weekday_list = []
    weekday_banners = content.find_all("td", class_="day withShow weekday")
    for banner in weekday_banners:
        #Название театра
        banner_titles = banner.find_all("div", class_="banner")
        theatre_list = all_banners(banner_titles)
        weekday_list.extend(theatre_list)

    #Соединяем все списки 
    print(daily_list, today_list, weekday_list)
    return True

#Функция для получения всех спектаклей на текущий день
def all_banners(banner_titles):
    out_list = []
    for b_title in banner_titles:
        
        #Получение даты концерта
        check = b_title.find("p")
        concert_date = check.get("data-date")
        
        #Получение отформатированного (красивого) названия спектакля 
        value = b_title.text.replace("\t","")
        concert_name = value.replace("\n"," ")
        concert_name = concert_name[2:]
        formatted_name = concert_name[:len(concert_name)-3]
        out_list.append({"name": formatted_name,"date":concert_date})
    
    return out_list

#Функция, вызываемая из бота
def parser():
    #Введите месяц и год в формате 01/2020:
    url = date2url("01/2020")
    result = site2(url)

if __name__ == "__main__":
    parser()