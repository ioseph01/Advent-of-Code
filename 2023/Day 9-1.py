
table = [line.split(" ") for line in open("f.txt").read().split("\n")]
result = 0

for x in table:
    differences = [x]
    while 1 != len(set(differences[-1])):
        differences.append([int(differences[-1][n + 1]) - int(differences[-1][n]) for n in range(len(differences[-1]) - 1)])


    difference = differences[-1][-1]
    for l in reversed(range(len(differences) - 1)):
        difference = int(differences[l][-1]) + difference
    
    result += difference

print(result)
