word = input('Ваше предложение: ').split()
print(word)
for i in range(1, len(word)+1):
    print(i, '-', word[i-1])
# не могу придумать, как сюда вписать {word[:10]}
