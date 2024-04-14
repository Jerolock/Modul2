def test(*params):
    print(*params)


test(1, 2, 3, 4, 'str', True)


def rekurs(n):
    if n == 1:
        return 1
    else:
        return n * rekurs(n - 1)


print(rekurs(14))
