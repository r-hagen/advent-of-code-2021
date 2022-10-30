def read_example():
    example = """
    [({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]
    """
    return [line.strip() for line in example.split("\n") if line.strip()]


def read_file(filename):
    with open(filename, "r") as file:
        return [line for line in file.read().strip().split("\n") if line]


opening_chars = ["{", "(", "[", "<"]
closing_chars = ["}", ")", "]", ">"]
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def get_illegal_character(line="{([(<{}[<>[]}>{[]{[(<()>"):
    stack = []
    for num, char in enumerate(line):
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            last = stack.pop()
            idx = closing_chars.index(char)
            if last != opening_chars[idx]:
                return (char, num)
    return (0, 0)


# input = read_example()
input = read_file("input")
# print(input)

(illegal, pos) = get_illegal_character()
assert illegal == "}" and pos == 12


# part 1
sum = 0
valid_lines = []
for line in input:
    (illegal, pos) = get_illegal_character(line)
    if illegal:
        sum += points[illegal]
    else: 
        valid_lines.append(line)
print(sum)


# part 2
class Node:
    def __init__(self, value: str, parent = None):
        self.value = value
        self.closed = False
        self.parent = parent
        self.children = []

    def __str__(self):
        values = [str(child) for child in self.children]
        return ''.join([self.value, *values])

    def print(self):
        node = self
        while node.parent != None:
            node = node.parent
        print(node)

    def add(self, value: str):
        if value in opening_chars:
            node = Node(value, self)
            self.children.append(node)
            return node
        elif value in closing_chars and opening_chars[closing_chars.index(value)] == self.value:
            self.closed = True
            if self.parent == None:
                return self
            else:
                return self.parent
        else: 
            return self

    def complete(self):
        if self.closed == False:
            return closing_chars[opening_chars.index(self.value)]
        else:
            return None

    def completeAll(self):
        completion = []
        completion.append(self.complete())

        node = self
        while node.parent != None:
            node = node.parent
            completion.append(node.complete())

        return [c for c in completion if c]


# verify against example
node = None
for char in "[({(<(())[]>[[{[]{<()<>>":
    if node == None: node = Node(char)
    else: node = node.add(char)
completion = node.completeAll()
print(completion)
assert completion == list("}}]])})]")
        

nodes = []
for line in valid_lines:
    node = None
    for char in line:
        if node == None: node = Node(char)
        else: node = node.add(char)
    nodes.append(node)

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

sums = []
for node in nodes:
    completion = node.completeAll()
    sum = 0
    for char in completion:
        sum = sum*5 + points[char]
    sums.append(sum)

sums = sorted(sums)
import math
idx = math.floor(len(sums)/2)
print(len(sums), idx)
print(sums[idx])
