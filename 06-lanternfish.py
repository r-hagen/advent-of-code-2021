input = [int(x) for x in open('input').readline().strip().split(',')]

# input = [3,4,3,1,2]

# part 1
fish = input
days = 80

for day in range(days):
    spawn = [8 for x in fish if x == 0]
    aged = [x-1 for x in fish]
    aged = [6 if x < 0 else x for x in aged]
    fish = [y for x in [aged, spawn] for y in x]
    # print(fish)

print(len(fish))

# part 2
fish = input
days = 256
dict = {}

for f in fish:
    dict[f] = dict.get(f, 0) + 1

for day in range(days):
    updated = {}

    if dict.get(0, 0):
        updated[8] = dict.get(0)
    
    for age in dict:
        updated[age-1] = dict[age]

    if updated.get(-1, 0):
        updated[6] = updated.get(6, 0) + updated[-1]
        updated.pop(-1)

    dict = updated

print(sum(dict.values()))