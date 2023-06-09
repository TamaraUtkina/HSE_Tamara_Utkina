from datetime import datetime

import requests
from bs4 import BeautifulSoup


class ParserCBRF:
    def __init__(self, start_date, end_date): 
        date_format = '%d.%m.%Y'
        
        try:
            datetime.strptime(start_date, date_format)
            datetime.strptime(end_date, date_format)
        except ValueError:
            raise RuntimeError("Дата начала или окончания периода отчета некорректна! Парсер не создан")
        
        self.start_date = start_date
        self.end_date = end_date
        self.collected_data = {}
        self.key_rates = self.collected_data.values()
        print("Парсер создан! Вызов метода .start() сформирует отчет")

    def __get_data(self):
        parameters = {
            "UniDbQuery.Posted": True,
            "UniDbQuery.From": self.start_date,
            "UniDbQuery.To": self.end_date
        }

        result = requests.get("https://www.cbr.ru/statistics/ddkp/infl/", params=parameters)

        soup = BeautifulSoup(result.text, "html.parser")

        data = soup.find('table', {"class": "data"})

        if data:
            values = data.find_all("td")
            for i in range(0, len(values), 4):
                key_rate = float(values[i+1].text.replace(',', '.'))
                self.collected_data[values[i].text] = key_rate

    def __get_average(self):
        return sum(self.key_rates) / len(self.key_rates)

    def __get_min(self):
        return min(self.key_rates)

    def __get_max(self):
        return max(self.key_rates)

    def start(self):
        self.__get_data()

        if not self.collected_data:
            print("Данных за указанный период нет!")
            return
        
        print(f"Ключевая ставка с {self.start_date} по {self.end_date}")
        for key in self.collected_data:
            print(key + ":", self.collected_data[key])
        
        print()

        print("Минимальная:", self.__get_min())
        print("Максимальная:", self.__get_max())
        print("Средняя:", self.__get_average())


print("Необходимо ввести даты в формате ДД.ММ.ГГГГ")
print("Пример: 15.12.2020")
start = input("Введите дату начала периода: ")
stop = input("Введите дату окончания периода: ")

parser = ParserCBRF(start, stop)

print("Вызываем метод .start()...")

parser.start()
