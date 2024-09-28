import math

path, table = open("f.txt").read().split("\n\n")
table = {(k := entry.strip("=").split())[0] : (k[2][1:4], k[3][:3]) for entry in table.split("\n")}

currents = [[entry, 0] for entry in table if entry.find("A") != -1]
directionToIdx = {"L" : 0, "R" : 1}
allZ = False


while not allZ:
    
    for direction in path:
        if allZ:
            break
        
        allZ = True

        for current in range(len(currents)):
            if currents[current][0].find("Z") == -1:
                
                currents[current] = [table[currents[current][0] ][directionToIdx[direction]], currents[current][1] + 1]
            
            if currents[current][0].find("Z") == -1:
                allZ = False
                  

result = 1

for current in currents:
    result = math.lcm(result, current[1])
print(result)


