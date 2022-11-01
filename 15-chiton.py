import heapq

lines = open("input", "r").read().strip().split("\n")

risk = [list(map(int, line)) for line in lines]
# print(risk)


# part 1
paths = [(0, 0, 0)]

vis = [[0] * len(row) for row in risk]

while True:
    rf, x, y = heapq.heappop(paths)
    if vis[x][y]: continue
    if (x, y) == (len(risk) - 1, len(risk[x]) - 1):
        print("ans1", rf)
        break
    vis[x][y] = 1
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not len(risk) > nx >= 0 <= ny < len(risk[0]): continue
        if vis[nx][ny]: continue
        heapq.heappush(paths, (rf + risk[nx][ny], nx, ny))


# part 2
paths = [(0, 0, 0)]

vis = [[0] * len(row) * 5 for row in risk * 5]

while True:
    rf, x, y = heapq.heappop(paths)
    if vis[x][y]: continue
    if (x, y) == (len(risk) * 5 - 1, len(risk[0]) * 5 - 1):
        print("ans2", rf)
        break
    vis[x][y] = 1
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not len(risk) * 5 > nx >= 0 <= ny < len(risk[0]) * 5: continue
        if vis[nx][ny]: continue

        ox = nx // len(risk)
        oy = ny // len(risk[0])

        ix = 0 if nx == 0 else nx % len(risk)
        iy = 0 if ny == 0 else ny % len(risk[0])

        r = risk[ix][iy] + ox + oy
        r = r if r <= 9 else r - 9

        heapq.heappush(paths, (rf + r, nx, ny))

