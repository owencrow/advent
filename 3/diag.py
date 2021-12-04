#!/usr/bin/env python3

def diag(lines):
    digits = len(lines[0])
    sums = [0] * digits
    count = 0
    for l in lines:
        count += 1
        for i in range(digits):
            sums[i] += int(l[i])
    gamma = 0
    epsilon = 0
    for i in range(digits):
        if sums[digits - 1 - i] * 2 > count:
            gamma += 2**i
        else:
            epsilon += 2**i
    return(gamma * epsilon)

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read()
        lines = lines.splitlines()
    print(diag(lines))
