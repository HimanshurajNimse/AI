import heapq

start = (8, 3, 1,
         5, 0, 4,
         6, 7, 2)

goal = (0, 1, 2,
        3, 4, 5,
        6, 7, 8)


def manhattan(state):
    dist = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        gi = goal.index(tile)

        dist += abs(i // 3 - gi // 3) + abs(i % 3 - gi % 3)

    return dist


def successor(state):
    z = state.index(0)
    r, c = divmod(z, 3)

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr * 3 + nc

            s = list(state)
            s[z], s[nz] = s[nz], s[z]

            yield tuple(s)


pq = [(manhattan(start), 0, start)]
parent = {start: None}
gscore = {start: 0}
found = False

while pq:
    f, g, state = heapq.heappop(pq)

    if state == goal:
        found = True
        break

    if g > gscore[state]:
        continue

    for nxt in successor(state):
        ng = g + 1

        if ng < gscore.get(nxt, float("inf")):
            gscore[nxt] = ng
            parent[nxt] = state

            heapq.heappush(
                pq, (ng + manhattan(nxt), ng, nxt)
            )

if found:
    path = []
    cur = goal

    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    print("Solution Path:")

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

    print("Cost:", len(path) - 1)

else:
    print("No solution found")