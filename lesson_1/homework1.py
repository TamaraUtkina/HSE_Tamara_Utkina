### Задание 1 ###

# Присваиваем переменной coins значение 5 (целое число)
coins = 5 

# Выводим тип значения, присвоенного переменной coins
# int - integer
print(type(coins))

# Выводим id (идентификатор) объекта
print("id значения в переменной coins (5):", id(coins))
coins += 1  # coins = coins + 1
print("У меня увеличилось кол-во монет, теперь их", coins)
print("id значения в переменной coins (6):", id(coins))

# Запрашиваем строковое значение у пользователя
user = input("Введите имя: ")

# Выводим значение, введенное пользователем
print("Рад знакомству с тобой,", user)

# Запрашиваем целочисленное значение у пользователя
age = int(input("Введите возраст: "))

# Выполняем операцию умножения и вывод на экран
print("А я в два раза старше, мне", age * 2)

### Задание 2 ###
 
time = input("Введите время в секундах: ")

if time.isdigit():
    time = int(time)
    
    hours = time // 3600
    print("Часы:", hours)
    
    minutes = (time - hours * 3600) // 60
    print("Минуты:", minutes)
    
    seconds = time - hours * 3600 - minutes * 60
    print("Секунды:", seconds)
else:
    print("Введено некорректное значение!")

### Задание 3 ###

n = input("Введите число (от 1 до 9): ")

print(int(n) + int(n*2) + int(n*3))