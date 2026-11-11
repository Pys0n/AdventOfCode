# --- Day 8: Two-Factor Authentication ---
# You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.
#
# To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.
#
# Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.
#
# The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:
#
# rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
# rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
# rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
# For example, here is a simple sequence on a smaller screen:
#
# rect 3x2 creates a small rectangle in the top-left corner:
#
# ###....
# ###....
# .......
# rotate column x=1 by 1 rotates the second column down by one pixel:
#
# #.#....
# ###....
# .#.....
# rotate row y=0 by 4 rotates the top row right by four pixels:
#
# ....#.#
# ###....
# .#.....
# rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:
#
# .#..#.#
# #.#....
# .#.....
# As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.
#
# There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

import os

with open(os.path.abspath(__file__) + 'input8.txt', 'r', encoding='utf-8') as file:
    operations = file.read().strip().split('\n')


def solve(operations: list) -> int:
    display = [['.' for _ in range(50)] for _ in range(6)]

    for operation in operations:
        if 'rect' in operation:
            width, height = operation.split(' ')[1].split('x')
            width, height = int(width), int(height)

            for y in range(height):
                for x in range(width):
                    display[y][x] = '#'
        elif 'row' in operation:
            operation = operation.split(' ')
            y = int(operation[2][2:])
            modifier = int(operation[4]) % 50
            for _ in range(modifier):
                display[y].insert(0, display[y].pop(-1))
        elif 'column' in operation:
            operation = operation.split(' ')
            x = int(operation[2][2:])
            modifier = int(operation[4]) % 6
            for _ in range(modifier):
                display[0][x], display[1][x], display[2][x], display[3][x], display[4][x], display[5][x] = display[5][x], display[0][x], display[1][x], display[2][x], display[3][x], display[4][x]

    # Part 2:
    print('Display:')
    for row in display:
        print(''.join(row).replace('.', ' '))

    return sum([row.count('#') for row in display])


print('Number of Pixels lit:', solve(operations)) # Solution: 119


# --- Part Two ---
# You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.
#
# After you swipe your card, what code is the screen trying to display?


# Solution: ZFHFSFOGPO
