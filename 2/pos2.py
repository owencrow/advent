#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read()

x = 0
y = 0
a = 0

for l in lines.splitlines():
    (verb, count) = l.split()
    count = int(count)
    if verb == 'forward':
        x += count
        y += count * a
    elif verb == 'up':
        a -= count
    elif verb == 'down':
        a += count
    print(verb, count, x, y, a)

print(x, y, x * y)
