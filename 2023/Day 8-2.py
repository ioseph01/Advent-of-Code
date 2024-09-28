import math

path, table = open("f.txt").read().split("\n\n")
table = {(k := entry.strip("=").split())[0] : (k[2][1:4], k[3][:3]) for entry in table.split("\n")}

currents = [[entry, 0] for entry in table if entry.find("A") != -1]
directionToIdx = {"L" : 0, "R" : 1}
result = []

while len(currents) > 0:
    
    for direction in path:
        
        if currents[0][0].find("Z") == -1:
            currents[0] = [table[currents[0][0]][directionToIdx[direction]], currents[0][1] + 1]
            
        else:
            result.append(currents.pop(0)[1])
            break
            
                  
print(math.lcm(*result))


