

def checkAround(lineNum, charNum):
    for i in range(3):
        for j in range(3):
            if lines[lineNum - 1 + i][charNum - 1 + j] == '*':
                return (lineNum - 1 + i ,charNum - 1 + j)
    return (-1, -1)
                

lines = []
with open("f.txt") as f:
    lines = ['.' + line.strip() + '.' for line in f]
    
horizontal_padding = ''.join(['.' for char in range(len(lines[1]))])
lines.append(horizontal_padding)
lines.insert(0, horizontal_padding)

result = 0
numbers = {}

for lineNum in range(1, len(lines) - 1):
    number = ""
    isNear = False
    gearCoord = (-1, -1)
    for charNum in range(len(lines[lineNum])):
        if lines[lineNum][charNum].isdigit():
            number += lines[lineNum][charNum]
            if checkAround(lineNum, charNum) != (-1, -1):
                gearCoord = checkAround(lineNum, charNum)
                isNear = True

        else:
            if number != "" and isNear == True:
                if gearCoord in numbers:
                    numbers[gearCoord].append(int(number))
                else:
                    numbers[gearCoord] = [int(number)]
                
            isNear = False
            number = ""
            
print(sum(nums[0] * nums[1] for nums in numbers.values() if len(nums) == 2))
