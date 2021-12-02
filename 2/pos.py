#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read()

x = 0
y = 0

for l in lines.splitlines():
    (verb, count) = l.split()
    count = int(count)
    if verb == 'forward':
        x += count
    elif verb == 'up':
        y -= count
    elif verb == 'down':
        y += count

print(x, y, x * y)
