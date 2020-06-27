HW = input().split()

H = int(HW[0])

W = int(HW[1])

A = []

for _ in range(H):
    A.append(list(map(int, input().rstrip().split())))


a = [[0] * (len(A[0]) + 2)]
for row in A:
    a.append([0] + row + [0])
a.append([0] * (len(A[0]) + 2))

ans = len(A) * len(A[0]) * 2

for i in range(1, len(a)):
    for j in range(1, len(a[i])):
        ans += abs(a[i][j] - a[i-1][j])
        ans += abs(a[i][j] - a[i][j-1])
print(ans)
