import requests
import json
url = 'https://geocode-maps.yandex.ru/1.x/?format=json&apikey=3f355b88-81e9-4bbf-a0a4-eb687fdea256&geocode=Самара'
res = requests.get(url)
response = json.loads(res.content)
print('Долгота для центра города Самара: ', response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0])
