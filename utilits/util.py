import requests
from requests.auth import HTTPBasicAuth


url = "http://94.73.216.81:6003/sigir_work/hs/API/Check/CheckCont?ContNum=HNKU6137310"
response = requests.get(url, auth=HTTPBasicAuth('web_api', 'Fcn9KhC85hXnut12'))

print(response.status_code)
print(response.text)