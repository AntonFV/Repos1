import json
import os
import csv
(os.mkdir('/Users/Антон/Desktop/python/pythonTaskjson'))
dir = '/Users/Антон/Desktop/python/pythonTaskjson/country.json'
data ={'Страна':'Франция','Город':'Париж'}
with open('dir', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
with open('dir', 'r', encoding='utf-8') as file:
    data = json.load(file)
data['Язык'] = 'Французский'
with open(dir, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
print("Файл обновлен")

test_json = '/Users/Антон/Desktop/python/pythonTaskjson/test_json.json'
data2 ={'Имя': 'Роман', 'Возраст': 19, 'Город': 'Москва'}

with open('test_json', 'w', encoding='utf-8') as file:
    json.dump(data2, file, indent=2, ensure_ascii=False)
with open('test_json', 'r', encoding='utf-8') as json_file:
    data3 = json.load(json_file)

# Подготавливаем данные для CSV
row_data = {
    'Имя': data3.get('Имя', ''),
    'Возраст': data3.get('Возраст', ''),
    'Город': data3.get('Город', ''),
    'Должность': 'Стажёр',
    'Зарплата': 50000
}

# Определяем заголовки
headers = ['Имя', 'Возраст', 'Город', 'Должность', 'Зарплата']

# Проверяем существование файла
file_exists = os.path.exists('employees_with_salary.csv')

# Открываем CSV-файл для добавления данных
with open('employees_with_salary.csv', 'a', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    
    if not file_exists:
        writer.writeheader()
    
    # Записываем строку с данными
    writer.writerow(row_data)

print("Данные добавлены в файл")