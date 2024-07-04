N = input().strip()

A = list(map(int, input().strip().split()))

result = 0
for i in range(0, len(A) - 2):
    if A[i] == A[i + 2]:
        result += 1

print(result)
