# Выввести на экран циклом N строк из "*", причем каждая строка должна быть пронумерована и длина строки равна номеру
n = int(input())
for i in range(1, n+1, 1):
    print(i, '*' * i)