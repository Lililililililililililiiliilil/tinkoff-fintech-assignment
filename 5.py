n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.insert(0, 0)
ans = [9999 for z in range(n + 1)]
ans[-1] = 0

for i in range(len(A) - 1, -1, -1):
    for j in range(len(A), i + B[i] - 1, -1):
        if i >= j - A[j - 1]:
            ans[i + B[i]] = min(ans[i + B[i]], ans[j] + 1)

if ans[0] == 9999:
    print(-1)
else:
    print(ans[0])
