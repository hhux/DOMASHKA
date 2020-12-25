for i in range(1, 1001): # Бегу от 1 до 1000
    for j in range(2, i):
        if (i % j) == 0: # Делю i на все значения от 2 до i
            break
    else:
        print(i, end =' ')
