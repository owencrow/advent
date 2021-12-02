#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read()

new = []
old = []
count = 0

for l in lines.splitlines():
    l = int(l)
    new.insert(0,l)
    if len(old) == 3:
        new.pop(3)
        if sum(new) > sum(old):
            count += 1
    old = [*new]

print(count)

# 159 a 159 b [] -> a [ 159 ], b [ 159 ]
# 158 a [ 158, 159 ], b [ 159 ] -> a [ 158, 159 ], b[ 158, 159 ]
# 174 a [ 174, 158, 159 ], b [158, 159] -> a [ 174, 158, 159 ], b[174, 158, 159]
# 196 a [ 196, 174, 158 ], b [174, 158, 159] -> a(same), b=a
# 197 a [ 197, 196, 174 ], b [196, 174, 158] -> a(same), b=a
# 194
# 209
# 213
# 214
# 222
