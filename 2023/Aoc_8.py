
path, table = open("f.txt").read().split("\n\n")
table = {(k := entry.strip("=").split())[0] : (k[2][1:4], k[3][:3]) for entry in table.split("\n")}

directionToIdx = {"L" : 0, "R" : 1}
current = "AAA"
result = 0

while current != "ZZZ":
    for direction in path:
        
        if current == "ZZZ":
            break
        
        else:
           current = table[current][directionToIdx[direction]]
           result += 1

print(result)
