n = list(input().split())
size = int(n[0])
symb = n[1]
def func(size, symb):
    for i in range(0, ((size//2)+1)):
        print(symb*i)
    for i in range(((size//2)+1), 0, -1):
        print(symb*i)
    return ''

print(func(size, symb))
