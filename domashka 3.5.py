n = 'Мело, мело по всей земле Во все пределы. Свеча горела на столе, Свеча горела. \'' \
    'Метель лепила на стекле Кружки и стрелы. Свеча горела на столе, Свеча горела.'
x = n.replace(',', '').replace('.', '').lower().split()
z = dict()
for i in x:
    z[i] = x.count(i)
print(z)