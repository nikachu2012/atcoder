def fibonacchi(cnt: int) -> int:
    fa = 0
    fb = 1

    for _ in range(cnt):
        tmp = fa
        fa = fb
        fb = tmp + fb

    return fa


print(fibonacchi(22))
