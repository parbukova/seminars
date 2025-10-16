# #sem2 ex4
# raw = '0' + input()
# new = ''
# for i in range(0, len(raw)+1, 4):
#    new += (raw[i+3:i:-1]+' ')
# print(new)
    
# # sem2 ex5
# raw = list(input().split())
# raw[1:-1] = raw[0:-1]
# raw[0] = raw[-1]
# raw.pop()
# print(' '.join(raw))


# sem2 ex6
# raw = list(input().split())
# l = len(raw)
# for i in range(0, l):
#     n = raw.count(raw[i])
#     if n == 1:
#        print(raw[i], end=' ')


# # sem2 ex7
# raw = list(input().split())
# l = len(raw)
# n = raw.count(raw[0])
# fin =raw[0]
# for i in range(0, l):
#     n1 = raw.count(raw[i])
#     if n1 > n:
#        n = n1
#        fin = raw[i]
# print(fin)


# sem2 ex8
N = int(input())
raw = list(map(int, input().split()))
if sum(raw)/N - sum(raw)//N > 0.5:
    print((sum(raw)//N)+1)
else: 
    print(sum(raw)//N)