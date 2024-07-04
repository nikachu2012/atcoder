N = int(input().strip())

result = 0
for _ in range(N):
    p = input().strip()
    if p == "Takahashi":
        result += 1
    else:
        continue

print(result)
