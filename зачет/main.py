n = int(input())
a = []
for u in range(n):
    a.append(list(map(int, input().split())))
b = []
for i in range(n):
    b.append([0] * n)

for u in range(n):
    for j in range(n):
        b[u][j] = a[n-1-j][u]
s1 = 0
s2 = 0
for u in range(n):
    s1 += b[u][u]
    s2 += b[u][n-1-u]

for u in range(n):
    for j in range(n):
        print(b[u][j], end=' ')
    print()
print(s1,s2)
