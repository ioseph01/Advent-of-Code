

def checkAround(lineNum, charNum):
    for i in range(3):
        for j in range(3):
            if lines[lineNum - 1 + i][charNum - 1 + j] != '.' and lines[lineNum - 1 + i][charNum - 1 + j].isdigit() == False:
                return True
    return False
                

lines = []
with open("f.txt") as f:
    lines = ['.' + line.strip() + '.' for line in f]
    
horizontal_padding = ''.join(['.' for char in range(len(lines[1]))])
lines.append(horizontal_padding)
lines.insert(0, horizontal_padding)

result = 0

for lineNum in range(1, len(lines) - 1):
    number = ""
    isNear = False
    for charNum in range(len(lines[lineNum])):
        if lines[lineNum][charNum].isdigit():
            number += lines[lineNum][charNum]
            if checkAround(lineNum, charNum):
                isNear = True

        else:
            if number != "" and isNear == True:
                result += int(number)
                
            isNear = False
            number = ""
            

print(result)
