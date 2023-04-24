# Проверка ИНН для организаций ###

def valid_org_inn(inn):
    numbers = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    
    total = 0
    
    for i in range(len(numbers)):
        total += int(inn[i]) * numbers[i]
    
    control = total % 11
    
    if control > 9:
        control = control % 10
    
    if control == int(inn[-1]):
        return True
    else:
        return False
    

result = valid_org_inn("7812014560")

### Проверка ИНН для физического лица и ИП ###

my_inn = '770804312540'

def valid_person_inn(inn: str):
    numbers_1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    numbers_2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
  
  sum_1 = 0
  sum_2 = 0
  
    for i, c in enumerate(inn):
     if i > 9:
        break
    sum_1 +=(numbers_1[i] * (int(c)
    sum_1 = sum_1 % 11
    if sum_1 > 9:
         sum_1 = sum_1 % 10
    for i, c in enumerate(inn):
      if sum_1 > 10:
         break
     sum_2 += (int(c) * k_2[i])
    sum_2 = sum_2 % 11
    if sum_2 > 9:
        sum_2 = sum_2 % 10
    pass
    
  def is_valid_inn(inn: str):
    if inn.isdigit() and len(inn) == 12:
        return is_person_inn(inn)
    elif inn.isdigit() and len(inn) == 10:
        return is_org_inn(inn)
    else:
        raise TypeError


def task_3():

    print(is_valid_inn(my_inn))


def main():
    # task_1()
    # task_2()
    task_3()
