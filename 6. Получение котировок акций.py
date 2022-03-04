import requests
import pandas as pd
from bs4 import BeautifulSoup
r = requests.get("mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019")
html = BeautifulSoup(r.content)
table = html.find('table', {'id' : 'marketDataList'})
rows = []
trs = table.find_all('tr')
for tr in trs:
    tr = [td.get_text(strip=True) for td in tr.fond_all('td')]
    if len(tr) > 0:
        rows.append(tr)
data = pd.DataFrame(rows, columns=['Тикер','Дата', 'Сделки', 'С/рост', 'С/%', 'Закрытие', 'Открытие', 'min', 'max', 'avg', 'шт.', 'руб.', 'Всего'])
data = data[data['Сделки'] != 'N/A']
data['С/%'] = data['С/%'].str.replace('–','-').astype(float)
data = data.set_index('С/%').sort_index(ascending=False)
print(data['Тикер'].head(1))
