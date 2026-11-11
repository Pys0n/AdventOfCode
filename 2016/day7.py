# --- Day 7: Internet Protocol Version 7 ---
# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).
#
# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.
#
# For example:
#
# abba[mnop]qrst supports TLS (abba outside square brackets).
# abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
# aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
# ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
# How many IPs in your puzzle input support TLS?

with open('input7.txt', 'r', encoding='utf-8') as file:
    ips = file.read().strip().split('\n')


def solve_part1(ips: list) -> int:
    count = 0
    for ip in ips:
        outside = []
        inside = []
        data = ip.split('[')
        for entry in data:
            if ']' in entry:
                p1, p2 = entry.split(']')
                outside.append(p2)
                inside.append(p1)
            else:
                outside.append(entry)

        found = False
        for entry in outside:
            for i in range(len(entry)-3):
                if entry[i] == entry[i+3] and entry[i+1] == entry[i+2] and entry[i] != entry[i+1]:
                    found = True
                    break
            if found:
                break

        if not found:
            continue

        found = False
        for entry in inside:
            for i in range(len(entry)-3):
                if entry[i] == entry[i+3] and entry[i+1] == entry[i+2] and entry[i] != entry[i+1]:
                    found = True
                    break
            if found:
                break

        if found:
            continue

        count += 1

    return count


print('Number of TLS supporting IPs:', solve_part1(ips)) # Solution: 115


# --- Part Two ---
# You would also like to know which IPs support SSL (super-secret listening).
#
# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.
#
# For example:
#
# aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
# xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
# aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
# zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
# How many IPs in your puzzle input support SSL?



def solve_part2(ips: list) -> int:
    count = 0
    for ip in ips:
        outside = []
        inside = []
        data = ip.split('[')
        for entry in data:
            if ']' in entry:
                p1, p2 = entry.split(']')
                outside.append(p2)
                inside.append(p1)
            else:
                outside.append(entry)

        found = False
        needed_bab = []
        for entry in outside:
            for i in range(len(entry)-2):
                if entry[i] == entry[i+2] and entry[i] != entry[i+1]:
                    found = True
                    needed_bab.append(entry[i+1] + entry[i] + entry[i+1])
            
        if not found:
            continue

        found = False
        for entry in inside:
            for i in range(len(entry)-2):
                if entry[i:i+3] in needed_bab:
                    found = True
                    break
            if found:
                break

        if not found:
            continue

        count += 1

    return count


print('Number of SSL supporting IPs:', solve_part2(ips)) # Solution: 231


