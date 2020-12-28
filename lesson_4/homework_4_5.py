# Реализовать формирование списка, используя
# функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000
# (включая границы). Нужно получить результат
# вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
# from functools import reduce
# print([reduce(x + y)el for el in range(100, 1001) if el % 2 == 0])

from functools import reduce

my_list = []

for num in range(100, 1001):

    if num % 2 == 0:
         my_list.append(num)


print(my_list)

# new_list = [el for el in range(100, 1001) if el % 2 == 0]
# print(new_list)
fin_all = reduce(lambda x, y: x * y, my_list)
print(fin_all)