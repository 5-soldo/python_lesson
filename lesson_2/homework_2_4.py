word = input('Ваше предложение: ').split()
print(word)
item = 1
# не могу придумать, как сюда вписать {word[:10]}
for x in word:

    print(f'{item} {x[:10]}')
    item += 1