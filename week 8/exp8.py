states = ['Low', 'Medium', 'High']
actions = ['Short', 'Long']

rewards = {
    'Low': 5,
    'Medium': 2,
    'High': -5
}

trans = {
    'Low': {'Short': {'Low': 0.7, 'Medium': 0.3},
            'Long': {'Low': 0.9, 'Medium': 0.1}},
    'Medium': {'Short': {'Low': 0.4, 'High': 0.6},
               'Long': {'Low': 0.6, 'Medium': 0.4}},
    'High': {'Short': {'Medium': 0.5, 'High': 0.5},
             'Long': {'Medium': 0.8, 'High': 0.2}}
}

V = {s: 0 for s in states}
gamma = 0.9

for _ in range(10):
    newV = {}
    for s in states:
        vals = []
        for a in actions:
            val = 0
            for ns in trans[s][a]:
                val += trans[s][a][ns] * (rewards[s] + gamma * V[ns])
            vals.append(val)
        newV[s] = max(vals)
    V = newV

print(V)