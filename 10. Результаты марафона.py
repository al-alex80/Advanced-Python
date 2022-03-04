import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

sns.set_context('paper', font_scale=2)
data = pd.read_csv('https://video.ittensive.com/python-advanced/marathon-data.csv', delimiter=',')
data['split'] = data['split'].apply(lambda x: int(x.split(':')[0]) * 3600 + int(x.split(':')[1]) * 60 + int(x.split(':')[2]))
data['final'] = data['final'].apply(lambda x: int(x.split(':')[0]) * 3600 + int(x.split(':')[1]) * 60 + int(x.split(':')[2]))
sns.pairplot(data, hue='gender', height=6)
plt.show()
sns.jointplot(x=data['split'], y=data['final'])
plt.show()
print(round(stats.pearsonr(data['split'], data['final'])[0], 2))
