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

def valid_org_inn(inn):
    numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_2 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

sum_1 = 0

 for i in range(numbers)):
    sum_1 += numbers_1[i] * numbers_2[i]

    control = sum_1 % 11
    
    if control > 9:
        control = control % 10
    
    if control == (inn[-1]):
        return True
    else:
        return False

def valid_org_inn(inn):
    numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    numbers_4 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

sum_2 = 0

for i in range(len(numbers)):
    sum_2 += numbers_3[i] * numbers_4[i]

 if control > 9:
        control = control % 11
    
    if sum_1 == (inn[-1]):
    if sum_2 == (inn[-2]):
     
      return True
    else:
        return False
