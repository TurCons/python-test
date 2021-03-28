# задание №2-1

print("Введите несколько целых чисел, или 0 для окончания ввода.")

sumPositive = 0  # сумма положительных чисел 
sumNegative = 0  # сумма отрицательных чисел

while True:
    inputDigit = int(input())
    
    # условие выхода из цикла:
    if inputDigit == 0:
        break

    if(inputDigit > 0):
        sumPositive += inputDigit
    else:
        sumNegative += inputDigit


print('Сумма положительных чисел: ' + str(sumPositive))
print('Сумма отрицательных чисел: ' + str(sumNegative))

input("Нажмите любую клавишу, чтобы закрыть")