#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = sum(int(x) for x in sys.argv[1:])
    print(total)
