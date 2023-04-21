### Задание № 1 ###
# подпункт 1 #
def get_factorial(number):
    if number < 0:
        print("Факториал не существует!")
    elif number == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, number+1):
            factorial = factorial * i
        return factorial
    
# подпункт 2 #
def get_maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

# подпункт 3№
def calc_area(side1, side2):
    return side1 * side2 / 2
# импортируем переменные repondents и courts из файла lesson_2_data.py
from lesson_2_data import repondents, courts

# Функция для генерации "шапки"
# Добавлен дополнительный параметр courts - в него при вызове передается список судов (для заполнения названия и адреса суда по коду из номера дела)
def generate_header(respondent, courts):

    court_code = respondent["case_number"].split("-")[0]

    for court in courts:
        if court["court_code"] == court_code:
            court_name = court["court_name"]
            court_address = court["court_address"]
    
    text = f'''
В {court_name}
Адрес: {court_address}
    
Истец: Пупкин Василий Геннадьевич
ИНН 1236182357 ОГРНИП 218431927812733
Адрес: 123534, г. Москва, ул. Водников, 13
    
Ответчик: {respondent["short_name"]}
ИНН {respondent["inn"]} ОГРН {respondent["ogrn"]}
Адрес: {respondent["address"]}
    
Номер дела {respondent["case_number"]}
'''
    return text


# Функция для генерации "шапок" из списка ответчиков
# respondents - список словарей с данными ответчиков
# courts - список словарей с данными судов
def all_headers(respondents, courts):
    for respondent in respondents:
        if "case_number" in respondent:
            print(generate_header(respondent, courts))
