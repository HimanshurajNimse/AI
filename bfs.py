from collections import deque
graph={"A": ["B", "C"],
       "B": ["D", "E"],
       "C":["F"],
       "D": [],
       "E": ["G"],
       "F": ["G"],
       "G": []}

def bfs(start,goal):
    q=deque([start])
    parent={start:None}
    while q:
        u=q.popleft()
        if u==goal:
            break

        for v in graph[u]:
            if v not in parent:
                parent[v]=u
                q.append(v)

    if goal not in parent:
        return None

    path=[]
    cur=goal
    while cur is not None:
        path.append(cur)
        cur=parent[cur]
    return path[::-1]



print("Shortest path from A to B",bfs("A","G"))