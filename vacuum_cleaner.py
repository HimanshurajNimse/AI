rooms={"A":"Dirty", "B":"Dirty"}
loc="A"

def reflex_agent(loc,status):
    if status=="Dirty":
        return "Suck"
    return "RIGHT" if loc=="A" else "LEFT"

for steps in range(6):
    status=rooms[loc]
    act=reflex_agent(loc,status)
    print(f"Step {steps+1}: Location:{loc}, Status: {status}, Action: {act}")

    if act=="Suck":
        rooms[loc]="Clean"
    elif act=="RIGHT":
        loc="B"
    elif act=="LEFT":
        loc="A"

print(f"Final Room Status: {rooms}")
