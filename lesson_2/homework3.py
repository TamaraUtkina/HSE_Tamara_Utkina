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
