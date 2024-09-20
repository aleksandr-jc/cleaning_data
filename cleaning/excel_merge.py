import pandas as pd
import os

"""
Скрипт який отримує папку з файлами ексель та обьєднає їх в один ексель файл.
"""

# вкажіть шлях до папки з файлами Excel
folder_path = 'data/all_data'

# Створюємо список для збереження всіх DataFrame
all_data = []

# проходимо по кожному файлу в папці
for file in os.listdir(folder_path):
    if file.endswith('.xlsx') or file.endswith('.xls'): # перевірка чи це є файли Excel
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        all_data.append(df)

# Обʼєднуємо всі DataFrame в один
combined_df = pd.concat(all_data, ignore_index=True)

# Зберігаємо обʼєднаний DataFrame в новий Excel файл
combined_df.to_excel('data/cleaning_data/all_data.xlsx', index=False)

print('Файли успішно обʼєднані!')