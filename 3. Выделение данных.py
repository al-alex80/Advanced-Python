import pandas as pd
data = pd.read_csv('https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv', delimiter=';')
data['Percent'] = data['UnemployedDisabled'] * 100 / data['UnemployedTotal']
data = data[data['Percent'] < 2]
data = data.set_index('Year').sort_index()
print(data.index[0:1])
