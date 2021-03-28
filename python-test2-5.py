# задание №2-5
# Найдите все трёхзначные и четырёхзначные числа Армстронга.
# Число Армстронга. Числом Армстронга считается натуральное число, сумма цифр которого, возведенных в N-ную степень (N – количество цифр в числе) равна самому числу.

def armstrongSumV1(number):
    """ Функция определения суммы цифр, возведенных в степень количества цифр числа. (используются возможности представления числа как строки) """
    numberAsString = str(number)
    length = len(numberAsString) 
    sum = 0
    for digit in range(length):
        sum += int(numberAsString[digit]) ** length 

    return sum

def armstrongSumV2(number):
    """ Функция определения суммы цифр, возведенных в степень количества цифр числа. (используются разложение числа на разряды) """
    num = number
    length = len(str(number)) 
    sum = 0
    while num >= 1:
        digit = num % 10
        num = num // 10
        sum += digit ** length

    return sum

# левая граница диапазона
leftBound = 100
# правая граница диапазона
rightBound = 10000

for number in range(leftBound, rightBound):
    if (number == armstrongSumV1(number)):
        print(number)

    if (number == armstrongSumV2(number)):
        print(number)


input("Нажмите любую клавишу, чтобы закрыть")