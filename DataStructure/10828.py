import sys

def solution():
    n = int(sys.stdin.readline())
    queue = []
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if len(cmd) == 1:
            if cmd[0] == "pop":
                print(queue.pop() if len(queue) else -1)
            elif cmd[0] == "size":
                print(len(queue))
            elif cmd[0] == "empty":
                print(0 if len(queue) else 1)
            else:
                print(queue[-1] if len(queue) else -1)
        else:
            queue.append(cmd[1])


if __name__ == "__main__":
    solution()
