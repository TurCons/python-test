# задание №2-3
# Задание Python 2_3: Запрашиваются 10 чисел (целые значения от 0 до 1000).     
# Опишите алгоритм, позволяющий найти и вывести минимальное значение среди введенных чисел, которые имеют чётное значение и не делятся на три.

# левая граница диапазона
leftBound = 0
# правая граница диапазона
rightBound = 1000

numbersCount = 0
minNumber = rightBound + 1

while numbersCount < 10:
    number = int(input())
    
    if (number >= leftBound and number <= rightBound):
        numbersCount += 1
        if (number < minNumber and number % 2 == 0 and number % 3 != 0):
            minNumber = number
    else:
        print('Введенное число не попадает в диапазон [' + str(leftBound) + ', ' + str(rightBound) + ']')


if minNumber < rightBound + 1:
    print('Минимальное четное число, не делящееся на 3: ' + str(minNumber))
else:
    print('Минимального четного числа, не делящегося на 3, среди введенных чисел нет')