
f = open('input.txt')
numbers = f.readline()
sign = f.readline()
base = f.readline()
f.close()
N = list(map(int, numbers.split()))
b = int(base)
if b != 10:
    power1 = 0
    power2 = 0
    dec1 = 0
    dec2 = 0
    n1 = N[0]
    n2 = N[1]
    while n1 > 0:   
        rem1 = n1%10
        dec1 += rem1*(b**power1)
        n1 = n1//10
        power1 += 1
    while n2 > 0:   
            rem2 = n2%10
            dec2 += rem2*(b**power2)
            n2 = n2//10
            power2 += 1    

    # арифметика в десятичной
    plus = '+'
    minus = '-'
    comp = '*'

    if sign == plus:
       res = dec1 + dec2
    elif sign == minus:
       res = dec1 - dec2
    else:
       res = dec1*dec2
    # перевод из десятичной в исходную
    list = []
    while res > 0:
        rem3 = res % b
        list.append(rem3)
        res = res//b
    listt = map(str, list[::-1])
    result = ''.join(listt)


else:
    plus = '+'
    minus = '-'
    comp = '*'

    if sign == plus:
       res = N[0] + N[1]
    elif sign == minus:
       res = N[0] - N[1]
    else:
       res = N[0]*N[1]
    result = res

g = open('output.txt', 'w')
g.write(str(result))
g.close()