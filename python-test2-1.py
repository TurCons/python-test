# задание №2

sumPositive = 0  # сумма положительных чисел 
sumNegative = 0  # сумма отрицательных чисел

while True:
    inputDigit = int(input())
    
    if(inputDigit > 0):
        sumPositive += inputDigit
    else:
        sumNegative += inputDigit

    # условие выхода из цикла:
    if inputDigit == 0:
        break

print('Сумма положительных чисел: ' + str(sumPositive))
print('Сумма отрицательных чисел: ' + str(sumNegative))
