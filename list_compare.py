# Enter your code here. Read input from STDIN. Print output to STDOUT
h = 0
n,m = input().split()
listD = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
lA = 0
lB = 0
'''
intAD = ()
intBD = ()
intADBD = ()
intAD = A.intersection(listD)
intBD = B.intersection(listD)
h = len(A.intersection(listD))

print(intAD)
print(intBD)
#intADBD = intAD.intersection(intBD)
#print(intADBD)
h = h - len(intBD)
#h = lA - lB
'''
for i in range(0,int(m)):
    if listD[i] in A:
        h += 1
    if listD[i] in B:
        h -= 1



'''
for i in listD:
    if i in A:
        h += 1
    if i in B:
        h -= 1
'''

'''
for i in A:
    cA = listD.count(i)
for j in B:
    cB = listD.count(j)
print(cA - cB)

'''
print(h)
