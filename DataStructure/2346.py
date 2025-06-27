import sys
from collections import deque

def solution():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = deque(list(map(lambda x: x, zip(a, list(range(1, n + 1))))))
    answer = []
    while len(b) > 1:
        v = b.popleft()
        answer.append(v[1])
        for _ in range(abs(v[0]) - 1):
            if v[0] > 0:
                b.append(b.popleft())
            else:
                b.appendleft(b.pop())
    print(*answer)


if __name__ == '__main__':
    solution()
