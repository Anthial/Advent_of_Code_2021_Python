#Do I need regex for this? No, am I lazy enough to use it anyway? Yes. (I think I should specify that this is actually just prep for future AoC days, in case I need to remember how to do basic regex)
import re

def part_1():
    vertical = 0
    horizontal = 0
    with open ("input.txt", "r") as f:
        for line in f:
            forward_match = re.search (r"\bf\w+", line)
            if forward_match is not None:
                horizontal += int(line.split(' ')[1])
            down_match = re.search (r"\bd\w+", line)
            if down_match is not None:
                vertical += int(line.split(' ')[1])
            up_match = re.search (r"\bu\w+", line)
            if up_match is not None:
                vertical -= int(line.split(' ')[1])
    print(vertical*horizontal)

def part_2():
    horizontal = 0
    aim = 0
    depth = 0
    with open ("input.txt", "r") as f:
        for line in f:
            forward_match = re.search (r"\bf\w+", line)
            if forward_match is not None:
                h_temp = int(line.split(' ')[1])
                horizontal += h_temp
                depth += aim*h_temp
            down_match = re.search (r"\bd\w+", line)
            if down_match is not None:
                aim += int(line.split(' ')[1])
            up_match = re.search (r"\bu\w+", line)
            if up_match is not None:
                aim -= int(line.split(' ')[1])
    print(depth*horizontal)


if __name__ == "__main__":
    part_1()
    part_2()

            
