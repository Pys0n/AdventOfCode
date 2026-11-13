# --- Day 3: Squares With Three Sides ---
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.
#
# Or are they?
#
# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.
# 
# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?

import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r', encoding='utf-8') as file:
    triangles = file.read().strip().split('\n')

for i, triangle in enumerate(triangles):
    triangle = triangle.strip()
    while '  ' in triangle:
        triangle = triangle.replace('  ', ' ')
    triangle = (int(x) for x in triangle.split(' '))
    triangles[i] = triangle


def solve(triangles: list) -> int:
    count = 0

    for triangle in triangles:
        a, b, c = triangle
        if a + b <= c or a + c <= b or b + c <= a:
            continue

        count += 1

    return count

print('Possible Triangles:', solve(triangles)) # Solution: 982



# --- Part Two ---
# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
# 
# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
#
# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?


with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    triangles = [[] for _ in range(len(lines))]
    for i, line in enumerate(lines):
        line = line.strip()
        while '  ' in line:
            line = line.replace('  ', ' ')

        line = line.split(' ')

        triangles[i//3*3].append(int(line[0]))
        triangles[i//3*3+1].append(int(line[1]))
        triangles[i//3*3+2].append(int(line[2]))

print(triangles)

print('Possible Triangles:', solve(triangles)) # Solution: 1826 
