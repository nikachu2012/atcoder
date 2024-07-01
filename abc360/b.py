# S, T = input().strip().split()

import sys

S, T = ("atcoder", "toe")


def splitStr2(str, num):
    l = []
    for i in range(num):
        l.append(str[i::num])
    l = ["".join(i) for i in zip(*l)]
    rem = len(str) % num  # zip で捨てられた余り
    if rem:
        l.append(str[-rem:])
    return l


for i in range(1, len(S)):

    t = splitStr2(S, i)

    for k in range(i):
        target = ""

        for j in t:
            if len(j) <= k:
                break

            target += j[k]

        if target == T:
            print("Yes")
            sys.exit(0)

print("No")
