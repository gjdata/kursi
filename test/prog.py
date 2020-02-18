N, K = map(int, input().split())
counts = dict()
for n in range(N):
    x = int(input())
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

for (key, val) in counts.items():
    if val == 1:
        print(key)
        break


