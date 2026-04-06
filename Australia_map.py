states = ['WA','NT','Q','SA','NSW','V','T']

neighbors = {
    'WA':['NT','SA'],
    'NT':['WA','SA','Q'],
    'SA':['WA','NT','Q','NSW','V'],
    'Q':['NT','SA','NSW'],
    'NSW':['Q','SA','V'],
    'V':['SA','NSW'],
    'T':[]
}

colors = ['Red','Green','Blue']

def is_valid(state, color, assignment):
    for n in neighbors[state]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def backtrack(assignment={}):
    if len(assignment) == len(states):
        return assignment

    state = [s for s in states if s not in assignment][0]

    for color in colors:
        if is_valid(state, color, assignment):
            assignment[state] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[state]

    return None

print("Australia Map Coloring:")
print(backtrack())
