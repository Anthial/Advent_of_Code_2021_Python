
def part_1():
    previous = -1
    increase_counter = -1
    with open ("input.txt", "r") as f:
        for line in f:
            current = int(line)
            if current > previous:
                increase_counter += 1
            previous = current
    print(increase_counter)


def part_2():
    from collections import deque
    previous = deque()
    current = deque()
    increase_counter = 0
    with open ("input.txt", "r") as f:
        for line in f:
            current.append(int(line))
            if len(current) == len(previous):
                if sum(current) > sum(previous):
                    increase_counter += 1
                current.popleft()
                previous.popleft()
                previous.append(int(line))
            else:
                if len(current) == 3:
                    previous = current.copy()
                    current.popleft()
    print(increase_counter)

if __name__ == "__main__":
    part_1()
    part_2()