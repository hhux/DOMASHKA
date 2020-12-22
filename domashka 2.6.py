n = [7, 2, 5, 3, 15, 23]
summa = 0
ne_summa = 1

# Ищем сумму и произведение элементов списка
for i in n:
    summa += i
    ne_summa *= i
print('Сумма =', summa, 'Произведение =', ne_summa)