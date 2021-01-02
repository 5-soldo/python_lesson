# Создать (программно) текстовый файл, записать
# в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и
# выводить её на экран.

def sum():
    try:
        with open('hm_file_5_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
        # "34 90 76 7 15" получим ["34" "90" "76" "7" "15"]
        my_numb = line.split()
        # map(fun, ["34" "90" "76" "7" "15"]) map из str("34") сделает int(34)
        print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


sum()