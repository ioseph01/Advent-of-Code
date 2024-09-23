

result = 0

with open("f.txt") as f:
    for line in f:
        line = [set([num for num in card.split()]) for card in line.strip().split(": ")[-1].split(" | ")]
        matches = len(line[0] & line[-1])
        if matches > 0:
            result += 2 ** (matches - 1)
        
print(result)