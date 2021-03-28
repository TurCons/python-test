# задание №2-4
# Задание Python 2_4: Исправить предыдущее задание (2_3) для работы со случайными числами.

# Задание Python 2_3: Запрашиваются 10 чисел (целые значения от 0 до 1000).     
# Опишите алгоритм, позволяющий найти и вывести минимальное значение среди введенных чисел, которые имеют чётное значение и не делятся на три.

from random import randint

# левая граница диапазона
leftBound = 0
# правая граница диапазона
rightBound = 1000

numbersCount = 0
minNumber = rightBound + 1

while numbersCount < 10:
    # генерируем случайное целое число в диапазоне [leftBound, rightBound]
    number = randint(leftBound, rightBound)

    print(number)
    numbersCount += 1

    if (number < minNumber and number % 2 == 0 and number % 3 != 0):
        minNumber = number


if minNumber < rightBound + 1:
    print('Минимальное четное число, не делящееся на 3: ' + str(minNumber))
else:
    print('Минимального четного числа, не делящегося на 3, среди введенных чисел нет')

input("Нажмите любую клавишу, чтобы закрыть")