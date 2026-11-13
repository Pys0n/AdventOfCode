# --- Day 6: Signals and Noise ---
# Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.
#
# In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.
#
# All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:
#
# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
# The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.
#
# Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r', encoding='utf-8') as file:
    messages = file.read().strip().split('\n')


def solve_part1(messages: list) -> str:
    appearences = [{} for _ in range(len(messages[0]))]
    for message in messages:
        for i, letter in enumerate(message):
            appearences[i][letter] = appearences[i].get(letter, 0) + 1

    message = ''
    for counts in appearences:
        most_common = (0, '')
        for key in counts:
            if counts[key] > most_common[0]:
                most_common = (counts[key], key)
        message += most_common[1]

    return message


print('Message:', solve_part1(messages)) # Solution: tzstqsua


# --- Part Two ---
# Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.
#
# In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.
#
# In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.
#
# Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?


def solve_part2(messages: list) -> str:
    appearences = [{} for _ in range(len(messages[0]))]
    for message in messages:
        for i, letter in enumerate(message):
            appearences[i][letter] = appearences[i].get(letter, 0) + 1

    message = ''
    for counts in appearences:
        least_common = (tuple(counts.values())[0]+1, '')
        for key in counts:
            if counts[key] < least_common[0]:
                least_common = (counts[key], key)
            if least_common[0] == 1:
                break
        message += least_common[1]

    return message


print('Message:', solve_part2(messages)) # Solution: myregdnr


