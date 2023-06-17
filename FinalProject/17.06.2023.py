# импортируем модули
import json
import os
from datetime import datetime
# реквест - это запросы
import requests
# bs4 пакет, а класс BS делает парсинг
from bs4 import BeautifulSoup


class ParserCBRF:

    def __init__(self, date):
        date_format = '%d.%m.%Y'

        try:
            datetime.strptime(date, date_format)
        except ValueError:
            raise RuntimeError("Дата некорректна!")

        self.date = date
        # создаем список для хранения словарей
        self.collected_data = []
        print("Парсер создан! Вызов метода .start() сформирует отчет")

        # два нижних подчеркивания - значит скрыто

    def __get_data(self):
        parameters = {
            # UniDbQuery.Posted самой взять из URL
            "UniDbQuery.Posted": True,
            "UniDbQuery.To": self.date,
        }
        # квинтессенция - params= - менять нельзя
        result = requests.get(
            "https://www.cbr.ru/currency_base/daily/",
            params=parameters
        )
        # soup это полный текст страницы + обработка строк
        soup = BeautifulSoup(result.text, "html.parser")
        # table это тег таблицы
        data = soup.find('table', {"class": "data"})
        # если дата будет пустая

        if not data:
            return
        
        rows = data.find_all('tr')

        for row in rows:
            data = tuple(cell.text for cell in row.find_all('td'))
            # print(data)

            current = {}

            if data:
                current["digit_code"] = int(data[0])
                current["letter_code"] = data[1]
                current["units"] = int(data[2])
                current["title"] = data[3]
                current["rate"] = float(data[4].replace(',', '.'))

                self.collected_data.append(current)

    
    def __to_json(self, filename='rates.json'):
        # os.getcwd() - получить путь к текущей папке
        # os.path.join() - добавить к пути текущего каталога подкаталог parsed_data
        target_path = os.path.join(os.getcwd(), "parsed_data")

        # если целевой путь не существует, создать его
        if not os.path.exists(target_path):
            os.mkdir(target_path)

        # сохранить json файл в целевой каталог
        with open(os.path.join(target_path, filename), 'w') as f:
            json.dump(self.collected_data, f, ensure_ascii=False, indent=4)

    
    def start(self):
        self.__get_data()

        if not self.collected_data:
            print("Данных на указанную дату нет!")
            return

        self.__to_json()
        print("Данные сохранены в JSON файл!")


date = input("Введите дату для получения курсов валют: ")

parser = ParserCBRF(date)

print("Вызываем метод .start()...")

parser.start()
