import math

def orientation(ax,ay,bx,by,cx,cy):
    return (ax*by-bx*ay)+(ay*cx-ax*cy)+(bx*cy-by*cx) >= 0

# open text file
triangles = open('p102_triangles.txt', 'r')

# get coords
coords = triangles.read().split('\n')
coords = coords[:len(coords)-1]

sum = 0
# split and analyze coords
for t in coords:
    points = t.split(',')
    print points
    o1 = orientation(int(points[0]), int(points[1]), int(points[2]), int(points[3]), 0, 0)
    o2 = orientation(int(points[2]), int(points[3]), int(points[4]), int(points[5]), 0, 0)
    o3 = orientation(int(points[4]), int(points[5]), int(points[0]), int(points[1]), 0, 0)
    if ( o1
        and o2
        and o3 or(not o1 and not o2 and not o3)):
        sum += 1

print sum