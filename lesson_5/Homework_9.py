
from random import randint

# Пункт 1

step = randint(3, 5)
stop = 250000000

nums = list(range(10, stop+1, step))

# print(nums)

# Пункт 2

rand_nums = [randint(1, 100) for i in range(10)]

# print(rand_nums)

# Пункт 3

# объявляем функцию линейного поиска
def linear_search(num_list, num):
    for i in range(len(num_list)):
        if num_list[i] == num:
            print("Число найдено на индексе:")
            print(i)
            return i
   
    print("Искомое число не найдено!")     

# вызываем функцию линейного поиска для ранее созданного упорядоченного списка
linear_search(nums, 13)

# Пункт 4

def binary_search(num_list, num):
    start = 0
    stop = len(num_list) - 1
    middle = 0

    while start <= stop:
        middle = (stop + start) // 2
        if num_list[middle] < num:
            start = middle + 1
        elif num_list[middle] > num:
            stop = middle - 1
        else:
            print("Искомое число найдено на индексе", middle)
            return middle

    print("Искомое число не найдено!")
    
