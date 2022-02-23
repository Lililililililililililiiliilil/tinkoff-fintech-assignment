def painter(n, m, i):
    if n == m:
        return 1 + i
    if n > m:
        return painter(n - m, m, i + 1)
    if m > n:
        return painter(n, m - n, i + 1)


n, m = map(int, input().split())
print(painter(n, m, 0))
