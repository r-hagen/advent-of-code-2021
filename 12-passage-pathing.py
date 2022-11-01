lines = [line for line in open("input", "r").read().strip().split("\n")]
print(lines)

edges = {}
for line in lines:
    a, b = line.split("-")
    edges[a] = edges.get(a, []) + [b]
    edges[b] = edges.get(b, []) + [a]
print(edges)


# part 1
def count(node, visited=set()):
    if node == "end":
        return 1
    total = 0
    for next in edges[node]:
        if next in visited:
            continue
        total += count(next, visited | {node} if node == node.lower() else visited)
    return total


print(count("start"))


# part 2
def count(node, visited=set(), doubled=False):
    if node == "end":
        return 1
    total = 0
    for next in edges[node]:
        if next == "start": continue
        if next in visited and doubled: continue
        if next in visited:
            total += count(next, visited | {node} if node == node.lower() else visited, True)
        else:
            total += count(next, visited | {node} if node == node.lower() else visited, doubled)
    return total


print(count("start"))
