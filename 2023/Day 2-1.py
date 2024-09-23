

colorToAmount = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
}

sum = 0 

with open("f.txt") as f:
    id = 1
  
    for line in f:
        possible = True
        line = line.strip().split(":")[-1].split(";")
        games = []
        
        for section in line:
           games += [r.strip().split(" ") for r in section[1:].split(", ")]
        
        for game in games:
            if int(game[0]) > colorToAmount[game[1]]:
                possible = False
                break
            
        
        if possible == True:
            sum += id
        
        id += 1
        
print(sum)