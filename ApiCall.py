import json
import requests
from DBConnection import ABC

class Test(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

username = "18c03922bd545c47083ff64d77390126"
password = "dad5303abec678be0c7f517a4982119f"

pre = "https://api.intrinio.com/prices?identifier="
post = "&start_date=1900-01-01&page_number="
current_Page = 1
testUrl= "https://api.intrinio.com/prices?identifier=SNAP&start_date=2018-02-16"

ticker = "SNAP"
#request_url = pre + ticker + post + str(current_Page)
request_url = testUrl
#print(request_url)
response = requests.get(request_url,auth=(username, password))
result = response.json()
final=result['data']
#print(result['data'][0]['date'])
#print(final[0])
current_Page = int(current_Page)
#final = result['data']
currentPage = result['current_page']
total_page = result['page_size']
for index in final:
    print(index['high'], " " , index['date'])

currentPage +=1
while(currentPage <= total_page):
    newUrl = pre + ticker + post + str(currentPage)

    newResponse = requests.get(newUrl,auth=(username, password))
    newResult = newResponse.json()
    newFinal = newResult['data']

    for index in newFinal:
        print(index['high'], " " , index['date'])
    currentPage += 1


ABC.DBConnect(ticker)
