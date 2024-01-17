import requests
from requests.auth import HTTPBasicAuth
import json
from web_admin_telebot.settings import DJANGO_USERNAME, DJANGO_PASSWORD


# Замените ContNum на нужный номер контейнера

def req_cont(number):
    cont_num = number
    url = f"http://94.73.216.81:65533/alfatos/hs/API/Check/CheckCont?ContNum={cont_num}"

    # Аутентификационные данные
    username = DJANGO_USERNAME
    password = DJANGO_PASSWORD

    # Отправка GET-запроса с базовой аутентификацией
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    # Проверка ответа от сервера
    if response.status_code == 200:
        return response.json()
    else:
        return f"Ошибка выполнения запроса. Код состояния: {response.status_code}"


if __name__ == '__main__':
    print(req_cont('NEPU4571987'))