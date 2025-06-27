import sys
from collections import deque


def solution():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = deque(" ".join(sys.stdin.readline().strip()).split())
        tmp = deque([])
        while len(s):
            if len(tmp) == 0:
                tmp.append(s.popleft())
            else:
                if s[0] == ")" and tmp[0] == "(":
                    s.popleft()
                    tmp.popleft()
                else:
                    tmp.append(s.popleft())
        if len(tmp):
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    solution()
