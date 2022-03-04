import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import descartes

data = pd.read_csv('https://video.ittensive.com/python-advanced/data-44-structure-4.csv.gz', usecols=['Объект', 'Регион'])
data['Регион'] =data['Регион'].str.upper()
data = data.groupby('Регион').count()
data_geo = gpd.read_file('https://video.ittensive.com/python-advanced/russia.json')
data_geo = data_geo.to_crs({'init': 'epsg:3857'})
data_geo['NL_NAME_1'] = data['NL_NAME_1'].str.upper()
data_geo = data_geo.replace({
    "ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ": "ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ - ЮГРА",
    "РЕСПУБЛИКА АДЫГЕЯ": "РЕСПУБЛИКА АДЫГЕЯ (АДЫГЕЯ)",
    "ЧУВАШСКАЯ РЕСПУБЛИКА": "ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ",
    "РЕСПУБЛИКА МАРИЙ-ЭЛ": "РЕСПУБЛИКА МАРИЙ ЭЛ",
    "РЕСПУБЛИКА СЕВЕРНАЯ ОСЕТИЯ": "РЕСПУБЛИКА СЕВЕРНАЯ ОСЕТИЯ - АЛАНИЯ",
    "РЕСПУБЛИКА ТАТАРСТАН": "РЕСПУБЛИКА ТАТАРСТАН (ТАТАРСТАН)"
})
data_geo = pd.merge(left=data_geo, right=data, left_on='NL_NAME_1',right_on ='Регион', how='left')
fig = plt.figure(figsize=(16,9))
area = plt.subplot(1, 1, 1)
data_geo.plot(ax=area, legend=True, column="Объект", cmap="Reds")
area.set_xlim(2e6, 2e7)
for _, region in data_geo.iterrows():
    area.annotate(region['Объект'], xy=(region.geometry.centroid.x, region.geometry.centroid.y), fontsize=8)
plt.show()
print(data_geo[data_geo['NL_NAME_1'] == 'АЛТАЙСКИЙ КРАЙ']['Объект'])
