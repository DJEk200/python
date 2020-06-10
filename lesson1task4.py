x = int(input())
m = x % 10
x = x // 10
while x > 0:
    if x % 10 > m:
        m = x % 10
    x = x // 10
print(m)
