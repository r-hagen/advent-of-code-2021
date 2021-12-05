input = [int(line.strip()) for line in open('input')]

# lines = [199,
# 200,
# 208,
# 210,
# 200,
# 207,
# 240,
# 269,
# 260,
# 263]

# part 1
ans = 0
for idx in range(1, len(input)):
    if input[idx] > input[idx-1]:
        ans += 1
print(ans)

# part 2
ans = 0
for idx in range(3, len(input)):
    if sum(input[idx-2:idx+1]) > sum(input[idx-3:idx]):
        ans += 1
print(ans)