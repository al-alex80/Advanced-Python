import pandas as pd
data_1 = pd.read_csv('https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv', delimiter=';')
data_1 = data_1.set_index(['Year', 'Period'])
data_1.index.names = ['Year', 'Month']
data_2 = pd.read_csv('https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv', delimiter=';')
data_2 = data_2.set_index(['AdmArea', 'Year', 'Month'])
data_2 = data_2.loc['Центральный административный округ']
data_2.index.names = ['Year', 'Period']
data = pd.merge(data_1, data_2, left_index=True, right_index=True)
data = data.reset_index().set_index('Calls')
print(data.sort_index()['UnemployedMen'][0:1])
