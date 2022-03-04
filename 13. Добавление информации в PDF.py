from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfFileMerger, PdfFileReader
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# функция выявления районов из данных
def extract_district(x):
    return list(map(lambda a: a['District'], x))[0]

# выборка данных и построение графика
r = requests.get('https://video.ittensive.com/python-advanced/data-7361-2019-11-28.utf.json')
data = pd.DataFrame(json.loads(r.content)).fillna(value=0)
data['District'] = data['ObjectAddress'].apply(extract_district)
data_sum = data.groupby('District').sum().sort_values('NumOfVisitors', ascending=False)
fig = plt.figure(figsize=(11,6))
area = fig.add_subplot(1, 1, 1)
data_sum[0:20]['NumOfVisitors'].plot.pie(ax=area, labels=['']*20, label='Посещаемость', cmap='tab20')
plt.legend(data_sum[0:20].index, bbox_to_anchor=(1.5,1,0.1,0))
plt.savefig('libraries.png')

#создание pdf с диаграммой
pdfmetrics.registerFont(TTFont('Trebuchet', 'Trebuchet.ttf'))
PDF = canvas.Canvas('readers.pdf', pagesize=pagesizes.A4)
PDF.drawImage(ImageReader('libraries.png'), -200, 150)
PDF.setfont('Trebuchet', 24)
PDF.drawString(50, 600, 'Круговая диаграмма посещаемости библиотек по районам Москвы')
PDF.drawString(50, 100, 'Самый популярный район Москвы: ' + data_sum.index.get_values()[0])
PDF.drawString(100, 100, 'Посетило ' + data_sum['NumOfVisitors'].values[0] + ' человек')
PDF.save()

#соединение титульного и листа с диаграммой
files = ['https://video.ittensive.com/python-advanced/title.pdf', 'readers.pdf']
merger = PdfFileMerger()
for file in files:
    merger.append(PdfFileReader(open(file, 'rb')))
merger.write('report.pdf')
