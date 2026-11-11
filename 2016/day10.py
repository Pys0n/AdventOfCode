# --- Day 10: Balance Bots ---
# You come upon a factory in which many robots are zooming around handing small microchips to each other.
#
# Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.
#
# Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).
# 
# Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.
#
# For example, consider the following instructions:
#
# value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2
# Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
# Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
# Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
# Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
# In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.
#
# Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?

import os

class Bot:
    def __init__(self, low: tuple = (), high: tuple = ()) -> None:
        self.low = low
        self.high = high
        self.chips = []

    def get_chip(self, chip: int) -> None:
        if len(self.chips) != 0 and self.chips[0] > chip:
            self.chips.insert(0, chip)
        else:
            self.chips.append(chip)

    def is_full(self) -> bool:
        return len(self.chips) >= 2

    def give_chips(self, bots: dict, outputs: dict) -> bool:
        if len(self.chips) < 2:
            return False
        if self.low[0] == 'bot':
            if bots[self.low[1]].is_full():
                return False
        if self.high[0] == 'bot':
            if bots[self.high[1]].is_full():
                return False

        if self.low[0] == 'bot':
            bots[self.low[1]].get_chip(self.chips.pop(0))
        else:
            outputs[self.low[1]].append(self.chips.pop(0))
        if self.high[0] == 'bot':
            bots[self.high[1]].get_chip(self.chips.pop(0))
        else:
            outputs[self.high[1]].append(self.chips.pop(0))

        return True


with open(os.path.abspath(__file__) + 'input10.txt', 'r', encoding='utf-8') as file:
    instructions = file.read().strip().split('\n')


def solve(instructions: list) -> int:
    bots = {}
    outputs = {}
    
    for instruction in instructions:
        if instruction.startswith('value'):
            instruction = instruction.split(' ')
            value = int(instruction[1])
            bot = int(instruction[5])
            if bot in bots:
                bots[bot].get_chip(value)
            else:
                new_bot = Bot()
                new_bot.get_chip(value)
                bots[bot] = new_bot
        else:
            instruction = instruction.split(' ')
            bot = int(instruction[1])
            low = (instruction[5], int(instruction[6]))
            high = (instruction[10], int(instruction[11]))

            if low[0] == 'output':
                if low[1] not in outputs:
                    outputs[low[1]] = []
            if high[0] == 'output':
                if high[1] not in outputs:
                    outputs[high[1]] = []

            if bot in bots:
                bots[bot].low = low
                bots[bot].high = high
            else:
                new_bot = Bot(low, high)
                bots[bot] = new_bot

    
    result_bot = None
    found = True
    while found:
        found = False
        for bot in bots:
            if bots[bot].chips == [17, 61]:
                result_bot = bot
            
            res = bots[bot].give_chips(bots, outputs)
            if res:
                found = True

    product = 0
    for output in (0, 1, 2):
        for value in outputs[output]:
            if product != 0:
                product *= value
            else:
                product = value

    return bot, product


bot, product = solve(instructions)
print('Bot for value-61 and value-17 microchips:', bot) # Solution: 141



# --- Part Two ---
# What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?


print('Product of all values in outputs 0, 1, and 2:', product) # Solution: 1209
