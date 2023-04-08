def is_pasha_wins(n: int) -> bool:
    if n < 2:
        True

    d = n - 1
    Pasha_wins = False
    print('pasha', Pasha_wins, 'd', d, 'n', n)
    while d > 0:
        if n % d != 0:
            d -= 1
        else:
            print('d', d)
            n = n - d
            d = n - 1
            Pasha_wins = not Pasha_wins
            print('pasha', Pasha_wins, 'n', n)

    return Pasha_wins

n = int(input())
if is_pasha_wins(n):
    print('Pasha')
else:
    print('Mark')