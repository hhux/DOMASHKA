spisok = [0, 2, 5, 75, 11, 7]
# Нахожу минимальное и максимальное число
maximum = max(spisok)
minimum = min(spisok)
# Нахожу их айди
max_id = spisok.index(maximum)
min_id = spisok.index(minimum)
# Прикручиваю к айди значение минимума и максимума
spisok[min_id] = maximum
spisok[max_id] = minimum

print(spisok)