n = int(input())
intervals = []

for _ in range(n):
  start, end = map(int, input().split())
  intervals.append([start, end])

intervals.sort()
result = []

for start, end in intervals:
  if not result or start > result[-1][1]:
    result.append([start, end])
  else:
    result[-1][1] = max(result[-1][1], end)

for start, end in result:
  print(start, end)