import sys
from collections import deque

def solution():
    n = int(sys.stdin.readline())
    a = deque(list(range(1, n + 1)))
    while len(a) > 1:
        a.popleft()
        a.append(a.popleft())
    print(a[0])


if __name__ == "__main__":
    solution()
