import time
def func_time(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print ("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp



@func_time
def calc(x, y):
    cnt = 0 # Счетчик счастливых билетов
    for i in range(1000000):
        s = str(i).zfill(6)
        if int(s[0]) + int(s[1]) + int(s[2]) == int(s[3]) + int(s[4]) + int(s[5]): # Можно было срезом
            cnt += 1


calc(1, 2)
