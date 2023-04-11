def blocks(file):
    block = []
    for line in lines(file):
        if line:
            block.append(line)
        else:
            yield ''.join(block)
            block = []


def lines(file):
    for line in file:
        yield line.strip()
    yield '\n'


def test():
    file = open('test_input.txt')

    a = blocks(file)
    x = 0
    for i in a:
        print(x, i)
        x += 1
