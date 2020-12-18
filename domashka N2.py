#сложите цифры целого числа
n = input()
x = str(n)
c = 0
for i in x:
    c = int(i) + c
print(c)
