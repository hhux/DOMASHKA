def cash(deposit, persent, years):
    itogo = deposit * (persent * 0.01) * years
    return itogo + deposit

deposit = 10000
persent = 10
years = 20
print(cash(deposit, persent, years))