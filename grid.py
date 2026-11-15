grid =[["S",".",".","#","."],
       [".",".",".","#","."],
       ["#",".",".",".","."],
       [".","#",".",".","G"]]

pos=(0,0)
goal=(3,4)
visited=set()

def neighbors(r,c):
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
            yield (nr,nc)

path=[pos]
while pos!=goal:
    visited.add(pos)
    candidates=[x for x in neighbors(*pos)
                if x not in visited and grid[x[0]][x[1]]!="#"]

    if not candidates:
        print("No path found")
        break

    pos=min(candidates,key=lambda x: abs(x[0]-goal[0]) + abs(x[1]-goal[1]))
    path.append(pos)
    print("Internal visited state:",sorted(visited))
    print("Current path:",path)
    print("goal:",pos==goal)

if pos == goal:
    print("\nGoal reached!")
    print("Final path:", path)