# Для каждого числа от 1 до 100 вывести список чисел меньше текущего и кратного 5
for j in range(100):
    print('для числа', j, end='\n')
    for i in range(j):
        if i % 5==0:
            print(i, sep=' ')