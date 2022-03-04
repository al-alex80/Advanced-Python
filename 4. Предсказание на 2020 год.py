import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
data = pd.read_csv('https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv', delimiter=';')
data['Percent'] = data['UnemployedDisabled'] * 100 / data['UnemployedTotal']
data = data.groupby('Year').filter(lambda x: x['Year'].count() > 5)
data_avg = data.groupby('Year').mean()
x = np.array(data_avg.index).reshape(len(data_avg), 1)
y = np.array(data_avg['Percent']).reshape(len(data_avg), 1)
model = LinearRegression()
model.fit(x, y)
print(model.predict(np.array(2020).reshape(1, 1)).round(2))
