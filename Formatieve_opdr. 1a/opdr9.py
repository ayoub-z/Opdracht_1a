def verschuiven(ch, n):
    return ch[n::1] + ch[:n:1]

print(verschuiven('1', 3))