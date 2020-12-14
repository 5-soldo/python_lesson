a = int(input("some number > 0: ")) #  это задание я сделать сам не смог
max_n = 0
while a > 0:
    num1 = a % 10
    if num1 >= max_n:
        max_n = num1
    a //= 10
print(max_n)