
b=[' ']*9
w=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
p=lambda:[print('|'.join(b[i:i+3])) or (print("-----") if i<6 else None) for i in range(0,9,3)]
win=lambda x:any(b[a]==b[b1]==b[c]==x for a,b1,c in w)

def mm(m):
    if win('X'): return -1
    if win('O'): return 1
    if ' ' not in b: return 0
    r=-9 if m else 9
    for i in range(9):
        if b[i]==' ': b[i]='O' if m else 'X';v=mm(not m);b[i]=' ';r=max(r,v) if m else min(r,v)
    return r

best=lambda:max((mm(0),i) for i in range(9) if b[i]==' ')[1]

while True:
    p();m=int(input("Enter move (0-8): "));b[m]='X'
    if win('X') or ' ' not in b: break
    ai=best();print("AI plays:",ai);b[ai]='O'
    if win('O') or ' ' not in b: break
p();print("You win!" if win('X') else "You lose!" if win('O') else "Draw!")
