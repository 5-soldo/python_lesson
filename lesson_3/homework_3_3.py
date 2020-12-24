def my_func(a, b, c):
    if a >= b and a < c:
        return a + c
    elif b > a and b <= c:
        return b + c
    else:
        return a + b

print(my_func(1, 2, 3))
print(my_func(1, 1, 1))


