from collections import deque

CUP_A,CUP_B,Target=4,3,2
def next_state(x,y):
    states=[]
    states+=[((CUP_A, y), "Fill A"), ((x, CUP_B), "Fill B")]
    states+=[((0,y),"Empty B"),((x,0),"Empty A")]
    t=min(x,CUP_B-y)
    states.append(((x-t,y+t),"POUR A--->B"))
    t=min(CUP_A-x,y)
    states.append(((x+t,y-t),"POUR B--->A"))

    return states

stack=[((0,0),[])]
visted={(0,0)}
solution=[]

while stack:
    state,path=stack.pop()
    x,y=state
    if x==Target or y==Target:
        solution=path+[state]
        break

    for nxt,act in next_state(x,y):
        if nxt not in visted:
            visted.add(nxt)
            stack.append((nxt,path+[act]))


print("DFS solution:",solution)