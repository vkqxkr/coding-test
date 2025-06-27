import sys
from collections import deque

def solution():
    n, k = map(int, sys.stdin.readline().split())
    a = deque(list(range(1, n + 1)))
    answer = []
    while len(a):
        for idx in range(k):
            v = a.popleft()
            if idx == k - 1:
                answer.append(v)
            else:
                a.append(v)
    print(f"<{', '.join(map(str, answer))}>")


if __name__ == "__main__":
    solution()
