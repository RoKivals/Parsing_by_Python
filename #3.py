# Импортнули модуль запросов и обработки
import requests
from bs4 import BeautifulSoup

# Указали ссылку на сайт
link = "https://gijoe.fandom.com/wiki/Snake-Eyes_(Movie)#Snake_Eyes:_G.I._Joe_Origins_.282021_Movie.29"
# Взяли html-страницу сайта
responce = requests.get(link).text
# Создали объект BS, который парсит нужную нам html-страницу
soup = BeautifulSoup(responce, 'lxml')
# Ищем блок, который содержит всю необходимую нам информацию (отсюда и название переменной)
block = soup.find("div", class_="page-content")
info_block = block.find("aside", role="region")
name = info_block.find("h2", attrs={"data-source": "name"}).text
personal_info = info_block.find_all("section")[0]
gender_block = personal_info.find("div", attrs={"data-source": "gender"})
gender = gender_block.find("div").text

print(f"Gender type of {name} is {gender}")
