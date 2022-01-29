# Импортнули модуль запросов и обработки
import requests
from bs4 import BeautifulSoup
import fake_useragent

# Время запрещённых приёмов (создание фейкового user-agent'а)
# На каждом вызове он разный
user = fake_useragent.UserAgent().random
header = {"user-agent": user}
# Мы создали переменную, которая хранит в себе заголовки запроса
# Ей мы передали кастомное значение user-agent

# Указали ссылку на сайт
link = "https://browser-info.ru/"
# Взяли html-страницу сайта !(передав заголовки запроса)!
response = requests.get(link, headers=header).text
# Создали объект BS, который парсит нужную нам html-страницу
soup = BeautifulSoup(response, 'lxml')
# Ищем блок, который содержит всю необходимую нам информацию (отсюда и название переменной)
block = soup.find("div", id="tool_padding")
ua_block = block.find('div', id="user_agent")
ua_status = ua_block.text


print(ua_status)
'''
Принцип работы примерно таков, НО это работает только для статических сайтов, где ничего не подгружается через скрипты.
В третьем примере будет показана работа lxml по назначению (со статикой).
'''
