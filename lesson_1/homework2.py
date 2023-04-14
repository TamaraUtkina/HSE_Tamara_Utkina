parts = []

for i in range(3):
    print("Введите данные об участнике спора: ")
    
    current = {
        "name": input("Имя: "),
        "status": input("Статус: "),
        "inn": input("ИНН: ")
    }
    
    parts.append(current)

print(parts)
