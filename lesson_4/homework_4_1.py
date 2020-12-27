def cash(hour, money, bonus):
    # hour = int(input('Выработка в часах: '))
    # money = int(input('Ставка в час: '))
    # bonus = int(input('Премия: '))
    result = hour * money + bonus
    return result

result = cash
print(cash(4, 56, 200))