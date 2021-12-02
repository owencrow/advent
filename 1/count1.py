#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read()

last = 10000
count = 0
for l in lines.splitlines():
    l = int(l)
    if l > last:
        count += 1
    last = l

print(count)
