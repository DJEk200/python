#a = int(input('Введите первое число: '))
#b = int(input('Введите второе число: '))
#c = int(input('Введите третье число: '))

def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a >= b and c >= b:
        return a + c
    else:
        return b + c

print(my_func(a=3, b=1, c=2))