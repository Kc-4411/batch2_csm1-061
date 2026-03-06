

import math

A=[-15,-10]   # attacker damage
D=[10,15]     # defender recovery

def minimax(s,d,a):
    if d==0: return s
    M=A if a else D
    f=min if a else max
    return f(minimax(s+x,d-1,not a) for x in M)

s=50
print("\n⚔️ CYBER WAR: ATTACKER vs DEFENDER ⚔️\n")
print("Initial Security:",s,"\n")

for t in range(6):
    M=A if t%2==0 else D
    f=min if t%2==0 else max
    move=f(M,key=lambda x:minimax(s+x,2,t%2^1))
    s+=move
    print(("💀 ATTACK!" if t%2==0 else "🛡 DEFENSE!"),
          f"{move:+} → Security:{s}")
