import requests
from requests.auth import HTTPBasicAuth


# Замените ContNum на нужный номер контейнера
cont_num = "HNKU6137310"
url = f"http://94.73.216.81:6003/sigir_work/hs/API/Check/CheckCont?ContNum={cont_num}"

# Аутентификационные данные
username = "web_api"
password = "Fcn9KhC85hXnut12"

# Отправка GET-запроса с базовой аутентификацией
response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=10)

# Проверка ответа от сервера
if response.status_code == 200:
    print("Запрос выполнен успешно. Ответ сервера:")
    print(response.text)
else:
    print(f"Ошибка выполнения запроса. Код состояния: {response.status_code}")