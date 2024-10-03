

DISTANCE = int(input("Enter expansion rate: ")) - 1
stars = []

f = open("f.txt").read().split("\n")
clear_cols = [] # x's
clear_rows = [] # y's


for line in range(len(f)):
    current = f[line]
    if len(set(current)) != 1:
        for i in range(len(current)):
            if current[i] == "#":
                stars.append((i, line))
                clear_cols.append(i)
        
    else:
        clear_rows.append(line)
             

clear_cols = [i for i in range(len(f[0])) if i not in clear_cols]
        
result = 0
for star in range(len(stars)):
    x1, y1 = stars[star]
    for other in range(star + 1, len(stars)):
        x2, y2 = stars[other]
        r = 0
        for x in clear_cols:
            if min(x1, x2) < x < max(x1, x2):
                result += DISTANCE
       
            elif x > max(x1, x2):
                break
        
        for y in clear_rows:
            if min(y1, y2) < y < max(y1, y2):
                result += DISTANCE
                                
            elif y > max(y1, y2):
                break
        
        result += abs(x2 - x1) + abs(y2 - y1)

        
print(result)