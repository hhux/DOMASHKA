def f(a):
    z = a.replace('-', '').replace('+', '').replace(' ', '')
    for i in z:
        if i.isdigit():
            continue
        else:
            return 'Некорректный номер телефона'
    return "Номер телефона состоит из цифр"
a = str(input())
print(f(a))