def calc():
    start = 100000
    stop = 999999
    cnt = 0
    for i in range(start, stop+1, 1):
        a = str(i)[:3] # первая половина номера билета
        b = str(i)[3:] # вторая половина номера билета
        if int(a[0]) + int(a[1]) + int(a[2]) == int(b[0]) + int(b[1]) + int(b[2]):
            cnt += 1
    return cnt

print(calc())