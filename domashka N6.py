def f(a):
    z = a.replace('-', '').replace('+', '').replace(' ', '')
    if z.isdigit():
        return "Номер телефона состоит из цифр"
    else:
        return "Номер телефона введен некорректно"
    return
a = str(input())
print(f(a))