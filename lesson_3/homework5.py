import json
import csv
import re

def task1():
    # читаем ИНН номера из файла traders.txt в список numbers
    with open("traders.txt") as f:
        numbers = [item.strip() for item in f]
    
    # читаем содержимое файла traders.json в список traders 
    with open("traders.json") as f:
        traders = json.load(f)
    
    # помещаем организации с совпадающими ИНН в список found
    found = [trader for trader in traders if trader['inn'] in numbers]

    # записываем данные из списка found в файл traders.csv
    with open("traders.csv", "w") as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['ИНН', 'ОГРН', 'Адрес'])
        for item in found:
            writer.writerow((item['inn'], item['ogrn'], item['address']))
            

# поиск e-mail адресов в заданной строке
# возвращает список с найденными адресами или пустой список
def find_emails(string):
    pattern = re.compile(r"\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b")
    return re.findall(pattern, string)
    

def task2():
    # считываем датасет из json файла в список data
    with open("1000_efrsb_messages.json") as f:
        data = json.load(f)
    
    # создаем пустой словарь
    result = {}

    # для каждой записи в датасете (для каждого сообщения)
    for item in data:
        found = find_emails(item['msg_text'])
        if found:
            result[item['publisher_inn']] = set(found)
    
    # преобразуем множества в списки, так как
    # модуль JSON не может работать с множествами при записи json файла
    emails = {}
    for key, value in result.items():
        emails[key] = list(value)
    
        # запишем результат в файл emails.json
    with open('emails.json', 'w') as f:
        json.dump(emails, f, indent=4)
