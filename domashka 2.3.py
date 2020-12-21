n = int(input())
if n % 2 == 0:
    for i in range(0, n, 2):
        print(n * (n - i)* (n - i) )
