a = str(input())
x = a.replace(',', ' ').replace('.', ' ').replace('-', '').split()
z = 0
for i in x:
    if i.isalpha():
        z = z+1
print(z)
