
numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = []
for el in range(1, len(numbers)):
    if numbers[el] > numbers[el - 1]:
        result_list.append(numbers[el])

print(result_list)



sourse = [numbers[item] for item in range(1, len(numbers)) if numbers[item] > numbers[item - 1]]
print(sourse)