'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from collections import Counter
s = "AABCAAADA"
#s = "ABCDEFGHI"
k = 3
i = 0
st = ""
l1 = []
parts = []
u1 = []

for z in range(0,len(s),k):
    l1.append((s[z:z+k]))
'''
parts = [s[i:i+k] for i in range(0, len(s), k)]
for l in parts:
    print(l)


for z in range(0,len(s)):
    if i<k:
        #print('condition true')
        st += s[z]
        i += 1
    else:
        #print('condition false')
        l1.append(st)
        #print(st)
        st = ""
        st+= s[z]
        i = 0
'''
templist = []
sk = ""
listM = []
for k in l1:
    print(k)
    for t in range(0,len(k)):
        if k[t] not in templist:
            templist.append(k[t])
    for p in templist:
        print(p)
        sk += p
    listM.append(sk)
    templist.clear()
    sk = ""

for t in listM:
    print(t)
        
    #u1.append(list(Counter(k).keys()))
    #print(u1)

'''
for k in l1:
    print(k)
    u1.append(list(Counter(k).keys()))
    print(u1)

sf = ""
for j in u1:
    for m in sorted(j):
        sf += m
    print(sf)
    sf = ""
    

'''