print('введите имя')
a = input()
print('введите фамилию')
b = input()
print('укажите возраст')
while True:
    c = input()
    if c.isalpha():
        print('Укажите возраст в числах, например, "15"')
        continue
    else:
        break
print('населенный пункт')
d = input()
print('Выберите одно из увлечений: Рыбалка/Пиво')
e = str(input())
z = e.capitalize()
if "Рыбалка" in z:
    print(f'Имя: {a.capitalize()}')
    print(f'Фамилия: {b.capitalize()} ')
    print(f'Возраст: {c}')
    print(f'Населенный пункт: {d.capitalize()}')
    print('Увлечение: рыбалка, но что за рыбалка без пива?')
else:
    if int(c) < 18:
        print(f'Уважаемый {a.capitalize()}, Вам слишком рано употреблять спиртное')
        print(f'Имя: {a.capitalize()}')
        print(f'Фамилия: {b.capitalize()} ')
        print(f'Возраст: {c}')
        print(f'Населенный пункт: {d.capitalize()}')
    else:
        print(f'Имя: {a.capitalize()}')
        print(f'Фамилия: {b.capitalize()} ')
        print(f'Возраст: {c}')
        print(f'Населенный пункт: {d.capitalize()}')
        print('Увлечение: пиво, но разве пиво не вкуснее на рыбалке? :)')



