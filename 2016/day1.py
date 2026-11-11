# --- Day 1: No Time for a Taxicab ---
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# 
# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.
#
# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
#
# For example:
#
# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?

import os

with open(os.path.abspath(__file__) + 'input1.txt', 'r', encoding='utf-8') as file:
    instructions = file.read().strip().split(', ')


def solve_part1(instructions: list) -> int:
    facing = 0  # 0 = north, 1 = east, 2 = south, 3 = west

    x_position = 0
    y_position = 0

    for instruction in instructions:
        if instruction[0] == 'R':
            facing += 1
        else:
            facing -= 1
        facing %= 4

        distance = int(instruction[1:])
        if facing == 0:
            y_position -= distance
        elif facing == 1:
            x_position += distance
        elif facing == 2:
            y_position += distance
        elif facing == 3:
            x_position -= distance

    return abs(x_position) + abs(y_position)

print('Steps:', solve_part1(instructions)) # Solution: 271



# --- Part Two ---
# Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.
#
# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.
#
# How many blocks away is the first location you visit twice?


def solve_part2(instructions: list) -> int:
    visited = {(0, 0)}

    facing = 0  # 0 = north, 1 = east, 2 = south, 3 = west

    x_position = 0
    y_position = 0

    for instruction in instructions:
        if instruction[0] == 'R':
            facing += 1
        else:
            facing -= 1
        facing %= 4

        for _ in range(int(instruction[1:])):
            if facing == 0:
                y_position -= 1
            elif facing == 1:
                x_position += 1
            elif facing == 2:
                y_position += 1
            elif facing == 3:
                x_position -= 1

            if (x_position, y_position) in visited:
                return abs(x_position) + abs(y_position)

            visited.add((x_position, y_position))

print('Steps:', solve_part2(instructions)) # Solution: 153 
