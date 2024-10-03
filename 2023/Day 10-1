

pipe_types = {
    "north_pipes" : (("|", "S", "L", "J"), -1, 0, "south_pipes"),
    "east_pipes"  : (("-", "L", "F", "S"), 0,  1, "west_pipes"),
    "south_pipes" : (("|", "7", "S", "F"), 1,  0, "north_pipes"),
    "west_pipes"  : (("-", "J", "7", "S"), 0, -1, "east_pipes"),
    }
maze = []

with open("f.txt") as f:
    counter = 1
    for line in f:
        if (idx := line.find("S")) != -1:
            start = (counter, idx + 1, -1)
        
        maze.append(["."] + [char for char in line.strip()] + ["."])
        counter += 1

maze.append((horizontal_padding := ["." for i in range(len(maze[0]))]))
maze.insert(0, horizontal_padding)

toCheck = [start]
result = -1

while len(toCheck) > 0:
    current = toCheck.pop(0)
    value = maze[current[0]][current[1]]
    
    if isinstance(value, int):
        result = max(result, value)
    else:
        
        for direction in pipe_types:
            if value in (pipe_info := pipe_types[direction])[0]:
                coord = (current[0] + pipe_info[1], current[1] + pipe_info[2], current[2] + 1)
                if maze[coord[0]][coord[1]] in pipe_types[pipe_info[3]][0]:
                    
                    toCheck.append((current[0] + pipe_info[1], current[1] + pipe_info[2], current[2] + 1))
        
        maze[current[0]][current[1]] = (current[2] + 1)
        

print(result)


        
