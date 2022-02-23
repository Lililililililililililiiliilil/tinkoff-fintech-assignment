A, B, n = map(int, input().split())
X = (A + B) / 2
if not X.is_integer() or A < X:
    print("NO")
else:
    if n == 1:
        if A - X == X - B:
            print("YES")
        else:
            print("NO")
    else:
        if n > A - X:
            print("NO")
        else:
            print("YES")
