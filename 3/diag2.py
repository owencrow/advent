#!/usr/bin/env python3

def diag(lines):
    digits = len(lines[0])
    for l in range(len(lines)):
        lines[l] = int(f'0b{lines[l]}',2)
        print(lines[l])

if __name__ == "__main__":
    with open("test-input.txt") as f:
        lines = f.read()
        lines = lines.splitlines()
    print(diag(lines))
