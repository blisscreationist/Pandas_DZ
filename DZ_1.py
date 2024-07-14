import pandas as pd

df = pd.read_csv('Electric_Vehicle_Population_Data.csv')

print("Выводим первые 5 строк данных:")
print(df.head())

print("\nВыводим информацию о данных:")
print(df.info())

print("\nВыводим статистическое описание данных:")
print(df.describe())