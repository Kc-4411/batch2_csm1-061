states = ['Idle', 'Loaded']
actions = ['Pick', 'Move', 'Charge']

rewards = {
    'Idle': {'Pick': 5, 'Move': 1, 'Charge': 0},
    'Loaded': {'Pick': -1, 'Move': 4, 'Charge': 2}
}

trans = {
    'Idle': {
        'Pick': {'Loaded': 1.0},
        'Move': {'Idle': 1.0},
        'Charge': {'Idle': 1.0}
    },
    'Loaded': {
        'Pick': {'Loaded': 1.0},
        'Move': {'Idle': 1.0},
        'Charge': {'Loaded': 1.0}
    }
}

policy = {s: actions[0] for s in states}
V = {s: 0 for s in states}
gamma = 0.9

for _ in range(5):
    for _ in range(10):
        for s in states:
            a = policy[s]
            V[s] = sum(trans[s][a][ns] * (rewards[s][a] + gamma * V[ns]) for ns in trans[s][a])

    stable = True
    for s in states:
        old = policy[s]
        vals = {}
        for a in actions:
            vals[a] = sum(trans[s][a][ns] * (rewards[s][a] + gamma * V[ns]) for ns in trans[s][a])
        policy[s] = max(vals, key=vals.get)
        if old != policy[s]:
            stable = False
    if stable:
        break

print(policy)