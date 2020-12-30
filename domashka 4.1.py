from datetime import datetime, timedelta

d = '2012.12.12'
n = -5
my_date = datetime.strptime(d, '%Y.%m.%d')


if my_date.month == 12 and n > 0: #Проверяю, нужно ли добавить +1 к году
    change_month = my_date.replace(month=n, year=my_date.year+1)
elif n <0: #Проверяю, нужно ли вычитать месяц
    change_month = my_date.replace(month=my_date.month - (abs(n)))
else: #Во всех остальный случаях просто прибавляю месяц
    change_month = my_date.replace(month=n)

print(change_month)