#result_list.insert(pos, el)
#Разместить на позиции pos (индекс элемента списка) элемент el



my_list = [7, 5, 3, 3, 2]
num = int(input('number: '))
result_list = my_list

result_list.insert(2, num)
print(result_list)
