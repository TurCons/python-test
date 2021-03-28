# задание №2-2

# количество чисел для вывода
numbersCount = int(input())

n1 = 1  # первое число
n2 = 1  # второе число
print(n1)
print(n2)
nn = 0  # n-тое число

for number in range(numbersCount-2):
    nn = n1 + n2
    n1 = n2
    n2 = nn
    print(nn)

input("Нажмите любую клавишу, чтобы закрыть")