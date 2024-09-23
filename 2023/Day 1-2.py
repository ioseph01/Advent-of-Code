

import re

textToNum = {
    "one" : "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
}
# p = re.compile("(nine|eight|seven|six|five|four|three|two|one|[0-9])")
sum = 0

with open("f.txt") as f:
    for line in f:
        matches = re.finditer(r"(?=(nine|eight|seven|six|five|four|three|two|one|[1-9]))", line)
        numbers = [match.group(1) for match in matches]
        
        sum += int(textToNum[numbers[0]] + textToNum[numbers[-1]]) 
        
        

print(sum)
            

