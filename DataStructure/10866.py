import queue
import sys
from collections import deque


def solution():
    n = int(sys.stdin.readline())
    a = deque([])
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "push_front":
            a.appendleft(cmd[1])
        elif cmd[0] == "push_back":
            a.append(cmd[1])
        elif cmd[0] == "pop_front":
            print(a.popleft() if len(a) else -1)
        elif cmd[0] == "pop_back":
            print(a.pop() if len(a) else -1)
        elif cmd[0] == "size":
            print(len(a))
        elif cmd[0] == "empty":
            print(0 if len(a) else 1)
        elif cmd[0] == "front":
            print(a[0] if len(a) else -1)
        else:
            print(a[-1] if len(a) else -1)


if __name__ == "__main__":
    solution()
