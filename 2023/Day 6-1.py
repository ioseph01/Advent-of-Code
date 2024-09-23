

def fun(race):
    
    sum = 0
    for n in range(race[1] - 1):
        num = n * (race[0] - n)
        
        if num > race[1]:
            sum += 1
          
    return sum

time, distance = [l.split()[1:] for l in open("f.txt").read().split("\n")]


result = 1
for i in range(len(time)):
    result *= fun((int(time[i]), int(distance[i])))
    
    
print(result)
    
    


    

