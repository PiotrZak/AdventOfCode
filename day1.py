numbers = [int(x) for x in open('day1.txt', 'r').readlines()]

# part 1, with zip
pairs = zip(numbers, numbers[1:])
increases = [b - a for a,b in pairs if b - a > 0]
print('part 1:', len(increases))

# part 2, with zip
windows = [sum(w) for w in zip(numbers, numbers[1:], numbers[2:])]
print(windows)
pairs = zip(windows, windows[1:])
increases = [b - a for a,b in pairs if b - a > 0]
print('part 2:', len(increases))