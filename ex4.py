def somatorio_entre(j: int, k: int) -> int:
    if(j>k):
        return 0;
    return j + somatorio_entre(j+1, k)

print(somatorio_entre(3, 6))