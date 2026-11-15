
rules = [
    (["fever", "cough"], "possible flu"),
    (["fever", "rash"], "possible measles"),
    (["sneezing", "runny nose"], "possible common cold"),
    (["sore throat", "cough"], "possible throat infection"),
    (["fever", "sore throat"], "possible throat infection")
]

def forward_chaining(symptoms):
    facts = set(symptoms)
    results = []

    changed = True
    while changed:
        changed = False

        for conditions, conclusion in rules:
            if all(c in facts for c in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    results.append(conclusion)
                    changed = True

    return results

def backward_chaining(goal, symptoms):
    for conditions, conclusion in rules:
        if conclusion == goal:
            if all(c in symptoms for c in conditions):
                return True
    return goal in symptoms

symptoms = input("Enter symptoms separated by commas: ")
symptoms = {s.strip().lower() for s in symptoms.split(",") if s.strip()}

results = forward_chaining(symptoms)

print("\nForward Chaining Results:")
if results:
    for result in results:
        print(result)
else:
    print("No matching condition found.")

goal = input("\nEnter condition to verify: ").strip().lower()

if backward_chaining(goal, symptoms):
    print("Backward Chaining: Condition supported by the entered symptoms.")
else:
    print("Backward Chaining: Condition not supported by the entered symptoms.")

print("\nNote: This is an educational demonstration, not a medical diagnosis.")
