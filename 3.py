n = int(input())
A = list(map(int, input().split()))

x = [1]
while len(x) < n + 1:
    A_temp = A.copy()
    for i in range(n):
        x_i = x[i] ** 2 - min(A_temp)
        A_temp.remove(min(A_temp))
        if x_i < 0:
            temp = x[0]
            x = [temp + 1]
            break
        else:
            x.append(x_i)
print(x[0])
