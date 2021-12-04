#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read()
lines = lines.splitlines()
g = [0] * len(lines[0])
e = [0] * len(lines[0])
count = 0

for l in lines:
    count += 1
    for i in range(len(l)):
        print(l,i,l[i])
        g[i] += int(l[i])

