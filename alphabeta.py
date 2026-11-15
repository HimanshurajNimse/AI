def alphabeta(node,depth,alpha,beta,maximizing):
    if not isinstance(node,dict):
        return node, None

    if maximizing:
        value,best=float("-inf"),None
        for move, child in node.items():
            score, _=alphabeta(child,depth+1,alpha,beta,False)

            if score>value:
                value,best=score, move
                alpha=max(alpha,value)

                if alpha>=beta:
                    break
        return value,best

    else:
        value,best=float("inf"),None

        for move,child in node.items():
            score,_=alphabeta(child,depth+1,alpha,beta,True)

            if score<value:
                value,best=score,move
                beta=min(beta,value)

                if alpha>=beta:
                    break
        return value,best

tree={
    "A":{"A1":3,"A2":5},
    "B":{"B1":2,"B2":9},
    "C":{"C1":4,"C2":5}

}

value,move=alphabeta(tree,0,float("-inf"),float("inf"),True )

print(f"Best move: {move} with value: {value}")