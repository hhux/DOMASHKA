# Найти ТОП-2 самых дорогих товаров в списке словарей и вывести в том же формате
spisok = [{'Наименование': 'Лук', 'Цена': 24}, {'Наименование':'Чеснок', 'Цена': 15}, \
          {'Наименование': 'Колбаса', 'Цена': 300}, {'Наименование':'Рыба', 'Цена': 290}, \
          {'Наименование': 'Салат', 'Цена': 80}]

x = sorted(spisok, key=lambda x: x['Цена'])
print(x[-1], x[-2])