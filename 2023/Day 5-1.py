

seeds = []
with open("f.txt") as f:
    maps = [[r.split(" ") for r in ranges.split("\n")] for ranges in f.read().split("\n\n")]

for seed in range(1, len(maps[0][0])):
    
    for m in range(1, len(maps)):
        # print(maps[0][0][seed])   
        passed = False
        for r in range(1, len(maps[m])):
     
            if passed == True:
                break
            if int(maps[0][0][seed]) in range(int(maps[m][r][1]), int(maps[m][r][1]) + int(maps[m][r][2])):
         
                maps[0][0][seed] = int(maps[m][r][0]) + int(maps[0][0][seed]) - int(maps[m][r][1])
                passed = True
        
    seeds.append(maps[0][0][seed])

print(min(seeds))