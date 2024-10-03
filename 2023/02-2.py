
    
sum = 0 
with open("f.txt") as f:
    
    for line in f:
        
        line = line.strip().split(":")[-1].split(";")
        games = []
        colorAmount = {
            "red" : 0,
            "green" : 0,
            "blue" : 0,
        }
        
        for section in line:
           games += [r.strip().split(" ") for r in section[1:].split(", ")]
        
        for game in games:
            if int(game[0]) > colorAmount[game[1]]:
                colorAmount[game[1]] = int(game[0])
            
        sum += colorAmount["blue"] * colorAmount["green"] * colorAmount["red"]        
       
       
        
       
print(sum)
