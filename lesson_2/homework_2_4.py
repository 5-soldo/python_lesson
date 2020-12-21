word = input('Ваше предложение: ').split()
print(word)
item = 1
for x in word:

print(f'{item} {x[:10]}')
item += 1


# another
simple = ('когда уже проэллюстрируем').split()
for index, number in enumerate(simple):
    print(index, number[:10])


