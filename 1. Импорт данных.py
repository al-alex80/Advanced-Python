import pandas as pd
data = pd.read_csv('https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv', delimiter=';')
print(int(data['Calls'].mean()))
