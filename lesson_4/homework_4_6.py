from itertools import count


for i in count(3):
    #print(i)
    if i >= 10:
        #print()
        break
    print(i)

from itertools import cycle
num = 0
for el in cycle('Конец фильма'):
    if num > 36:
        break
    print(el)
    num += 1