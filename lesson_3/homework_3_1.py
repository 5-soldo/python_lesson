
def number():
    val_1 = int(input('enter number: '))
    val_2 = int(input('enter number: '))
    if val_2 == 0:
        return('enter number > 0')
    else:
        num_del = val_1 // val_2

    return num_del

num_del = number()
print(num_del)