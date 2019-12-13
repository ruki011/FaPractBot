from bs4 import BeautifulSoup
import requests

def date_detector(date):
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

def site2_module():

    #theatre_dict = {}
    
    #print("https://et-cetera.ru/poster/?month=2&year=2020") - динамическая ссылка
    response = requests.get("https://et-cetera.ru/poster/").text
    content = BeautifulSoup(response,"lxml")

    #Баннеры в будние дни
    banners = content.find_all("td", class_="day withShow")
    for banner in banners:

        #Название выступления
        banner_titles = banner.find_all("div", class_="banner")
        for banner_title in banner_titles:
            check = banner_title.find("p")
            print(check.get("data-date"))
            value = banner_title.text.replace("\t","")
            value = value.replace("\n"," ")
            print(value)
    
    #Баннер сегодня
    today_banners = content.find_all("td", class_="day today withShow")
    for banner in today_banners:
        
        #Название выступления
        banner_titles = banner.find_all("div", class_="banner")
        for banner_title in banner_titles:
            check = banner_title.find("p")
            print(check.get("data-date"))
            value = banner_title.text.replace("\t","")
            value = value.replace("\n"," ")
            print(value)


    #Баннеры в выходные дни
    weekday_banners = content.find_all("td", class_="day withShow weekday")
    for banner in weekday_banners:
        #Название театра
        banner_titles = banner.find_all("div", class_="banner")
        for banner_title in banner_titles:
            check = banner_title.find("p")
            print(check.get("data-date"))
            value = banner_title.text.replace("\t","")
            value = value.replace("\n"," ")
            print(value)

def parser():
    #Введите месяц и год в формате 01/2020:
    date_detector
    pass

if __name__ == "__main__":
    parser()