import numpy as np

# input = [16,1,2,0,4,2,7,1,2,14]
input = [int(x) for x in open('input').readline().strip().split(',')]

# part 1
fuel_cost = lambda x,p : abs(x-p)
total_cost = lambda p : sum([fuel_cost(x,p) for x in input])
ans = min([total_cost(x) for x in input])
print(ans)

# part 2
fuel_cost = lambda x,p : abs(x-p)*(abs(x-p) + 1)//2
total_cost = lambda p : sum([fuel_cost(x,p) for x in input])
ans = min([total_cost(x) for x in input])
print(ans)