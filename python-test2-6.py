# задание №2-6
# Напишите программу, которая запрашивает натуральное число N и выводит на экран все автоморфные числа, не превосходящие N.
# Автоморфным называется натуральное число, если оно равно последним цифрам своего квадрата. Например, 252 = 625.

# запросим число
rightBound = int(input())

for number in range(rightBound + 1):
    numberSquare = number ** 2
    numberSquareAsString = str(numberSquare)
    numberAsString = str(number)


    if (numberSquareAsString.endswith(numberAsString)):
        print(number)
        #print(numberSquare)

input("Нажмите любую клавишу, чтобы закрыть")