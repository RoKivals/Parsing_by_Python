# Импортнули модуль запросов и обработки
import requests
from bs4 import BeautifulSoup

# Указали ссылку на сайт
link = "https://browser-info.ru/"
# Взяли html-страницу сайта
responce = requests.get(link).text
# Создали объект BS, который парсит нужную нам html-страницу
soup = BeautifulSoup(responce, 'lxml')
# Ищем блок, который содержит всю необходимую нам информацию (отсюда и название переменной)
block = soup.find("div", id = "tool_padding")
js_block = block.find('div', id = "javascript_check")
js_status = js_block.find_all('span')[1].text

'''
Принцип работы примерно таков, НО это работает только для статических сайтов, где ничего не подгружается через скрипты.
В третьем примере будет показана работа lxml по назначению (со статикой).
'''