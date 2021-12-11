#!/usr/bin/env python3

from pprint import pprint

def read_file(filename):
    numbers = []
    with open(filename) as f:
        for index, line in enumerate(f):
            digits = len(line.strip())
            numbers.append(int(f'0b{line}',2))
            print("Line {}: {} {} {}".format(index, line.strip(), numbers[index], digits))
    return digits, numbers

def split_on_bit(numbers, bit):
    c = int('0b1' + '0' * (bit - 1),2)
    split = [[],[]]
    for num in numbers:
        if num & c == c:
            split[1].append(num)
        else:
            split[0].append(num)
    return split

def diag2(filename):
    (digits, numbers) = read_file(filename)
    split = [numbers, numbers]
    split = split_on_bit(split, 0)
    return digits, numbers, split

if __name__ == "__main__":
    pprint(diag2('test-input.txt'))

# zeros == least
# 00100
# 01111
# 00111
# 00010
# 01010
# 
# ones == most
# 11110
# 10110
# 10111
# 10101
# 11100
# 10000
# 11001
# 
# zeros == least
# 0100
# 1111
# 0111
# 0010
# 1010
# 
# ones == most
# 1110
# 0110
# 0111
# 0101
# 1100
# 0000
# 1001
# 
