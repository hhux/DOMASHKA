#При заданном целом трехзначном числе n посчитайте n+nn+nnn
n = input()
x = str(n)
a1 = x[0]
a2 = x[0] + x[1]
a3 = x[0] + x[1] + x[2]
print(int(a1) + int(a2) + int(a3))