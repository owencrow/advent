#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read()
lines = lines.splitlines()
digits = len(lines[0])
g = [0] * digits
count = 0

for l in lines:
    count += 1
    for i in range(digits):
        #print(l,i,l[i])
        g[i] += int(l[i])

gamma = 0
epsilon = 0
for i in range(digits):
    if g[digits - 1 - i] * 2 > count:
        gamma += 2**i
    else:
        epsilon += 2**i

print(gamma * epsilon, count, g)
