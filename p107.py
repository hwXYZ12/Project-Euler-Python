import math

adjMatrix = [line.split(',') for line in open("p107_network.txt").read().split('\n')[:-1]]

findSet = {x:set([x]) for x in range(len(adjMatrix))}

sortedEdgeSet = sorted( [(int(row), int(col)) for row in range(len(adjMatrix)) for col in range(len(adjMatrix)) if adjMatrix[row][col] != "-"], key= lambda x: int(adjMatrix[x[0]][x[1]]) )

newList = []
for t in sortedEdgeSet:
    (x,y) = t
    if ((y,x) in sortedEdgeSet
        and not (y,x) in newList):
        newList.append(t)

for x in newList:
    sortedEdgeSet.remove(x)

minTree = set()
for i in xrange(len(sortedEdgeSet)):

    if (findSet[sortedEdgeSet[i][0]] != findSet[sortedEdgeSet[i][1]]
        and len(minTree) < 39):
        findSet[sortedEdgeSet[i][0]] |= findSet[sortedEdgeSet[i][1]]
        findSet[sortedEdgeSet[i][1]] |= findSet[sortedEdgeSet[i][0]]
        for x in findSet[sortedEdgeSet[i][0]]:
            findSet[x] = findSet[sortedEdgeSet[i][0]]
        minTree.add(sortedEdgeSet[i])

totalWeight = sum([int(adjMatrix[x][y]) for x in xrange(len(adjMatrix)) for y in xrange(len(adjMatrix)) if adjMatrix[x][y] != "-"])
totalWeight -= sum([int(adjMatrix[x][x]) for x in xrange(len(adjMatrix)) if adjMatrix[x][x] != "-"])
totalWeight /= 2
total = sum(int(adjMatrix[x][y]) for (x,y) in minTree)

print total
print totalWeight - total

