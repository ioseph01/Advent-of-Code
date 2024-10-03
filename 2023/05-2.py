


with open("f.txt") as f:
    maps = [[r.split(" ") for r in ranges.split("\n")] for ranges in f.read().split("\n\n")]
    
seeds = [(int(maps[0][0][seed]), int(maps[0][0][seed + 1]) + int(maps[0][0][seed])) for seed in range(1, len(maps[0][0]), 2)]


for block in range(1, len(maps)):
    maps[block] = maps[block][1:]
    new = []
    #print(maps[block])
    
    while len(seeds) > 0:
        start, end = seeds.pop()
        
        
        for dest, begin, r in maps[block]:
            start, end, dest, begin, r = int(start), int(end), int(dest), int(begin), int (r)
            os = max(int(start), int(begin))
            oe = min (int(end), int(begin + r))
            if oe > os:
                new.append((os - begin + dest, oe  - begin + dest))
                if os > start:
                    seeds.append((start, os))
                if oe < end:
                    seeds.append((oe, end))
                break
        else:
            new.append((start, end))
    seeds = new

print(min(seeds)[0])
