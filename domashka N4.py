#В строке удалить все буквы "а" и подсчитать количество удаленных символов
a = str(input())
cnt = a.replace('a', '')
print(cnt, 'Количество удаленных символов -', (len(a)-len(cnt)))

