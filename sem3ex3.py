ab = input()
ab = ab.split(' ')
a = int(ab[0])
b = int(ab[1])
def func(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, d = func(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return x, y, d
print(func(a,b))
