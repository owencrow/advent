#!/usr/bin/env python3

def read_file(filename):
    numbers = []
    with open(filename) as f:
        for index, line in enumerate(f):
            digits = len(line.strip())
            numbers.append(int(f'0b{line}',2))
            print("Line {}: {} {} {}".format(index, line.strip(), numbers[index], digits))
    return digits, numbers

def diag2(filename):
    (digits, numbers) = read_file(filename)
    return digits, numbers

if __name__ == "__main__":
    print(diag2('test-input.txt'))
