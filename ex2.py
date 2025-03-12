def somatorio(n: int) -> int:
    if n == 1:
        return n
    return n + somatorio(n-1)

print(somatorio(5))