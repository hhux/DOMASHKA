from datetime import datetime, timedelta
import calendar

d = '2012.01.31'
n = 1
my_date = datetime.strptime(d, '%Y.%m.%d')

# Сколько дней в месяце
all_days = calendar.monthrange(my_date.year, my_date.month)[1]

# Проверяю, нужно ли добавить год
if my_date.month + n > 12:
    change_month = my_date.replace(month=n, year=my_date.year + 1)

# Проверяю на январь
elif my_date.month == 1:
    change_month = my_date + timedelta(days=all_days)

# Проверяю, нужно ли вычитать месяц
elif n < 0:
    change_month = my_date.replace(month=my_date.month - (abs(n)))

# Во всех остальный случаях просто прибавляю месяц
else:
    change_month = my_date.replace(month=n)

print(change_month)
