

sum = 0

with open("f.txt") as f:
    for line in f:
        d1 = 0
        d2 = 0
        for char in line:
            if char.isdigit():
                d1 = char
                break
        for char in reversed(line):
            if char.isdigit():
                d2 = char
                break
        
        sum += int(d1 + d2)
        

print(sum)
            
        
