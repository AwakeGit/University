def min_breaks(a, b, memo=None):
    if memo is None:
        memo = {}
    if a == 1 and b == 1:
        return 0
    if a == 1:
        return b - 1
    if b == 1:
        return a - 1
    if (a, b) in memo:
        return memo[(a, b)]
    horizontal_breaks = min_breaks(a // 2, b, memo) + min_breaks(a - a // 2, b, memo) + 1
    vertical_breaks = min_breaks(a, b // 2, memo) + min_breaks(a, b - b // 2, memo) + 1

    result = min(horizontal_breaks, vertical_breaks)
    memo[(a, b)] = result

    return result


if __name__ == '__main__':
    n = 2
    m = 2
    print(f"Минимальное количество разломов для шоколадки {n}x{m}: {min_breaks(n, m)}")