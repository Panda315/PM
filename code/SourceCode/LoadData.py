import pandas as pd

# file = pd.read_csv('code/DataSets/Bhaisipati.csv',delimiter=',')
file = pd.read_csv('../DataSets/dhm-pkr.csv',delimiter=',')
print(file.head())
print(file.info())