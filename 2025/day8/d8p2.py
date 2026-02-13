from math import sqrt

def dist(A, B):
    return sqrt(sum([(x-y)**2 for x,y in zip(A,B)]))

positions = []
while True:
    try:
        positions.append(tuple(int(x) for x in input().split(',')))
    except EOFError:
        break

distances = []
for i in range(len(positions)-1):
    for j in range(i+1, len(positions)):
        distances.append((dist(positions[i], positions[j]), [positions[i], positions[j]]))
distances.sort(key=lambda x: x[0])

circuits = []
for d in distances:
    c1, c2 = None, None
    for c in circuits:
        if d[1][0] in c:
            c1 = c
        if d[1][1] in c:
            c2 = c
    
    if c1 == None and c2 == None:
        circuits.append(set([d[1][0], d[1][1]]))
    elif c1 == None:
        c2.add(d[1][0])
    elif c2 == None:
        c1.add(d[1][1])
    elif c1 == c2:
        continue
    else:
        c1 |= c2
        circuits.remove(c2)
    
    if len(circuits[0]) == len(positions):
        print(d[1][0][0] * d[1][1][0])