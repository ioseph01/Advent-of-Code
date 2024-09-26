
from collections import Counter, defaultdict


def cardValues(char):
    if char.isdigit():
        return int(char)
    cardMap = {"T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    return cardMap[char]


def collectBuckets(hands, buckets):
    idx = 0
    for bucket in reversed(buckets):
        while len(bucket) > 0:
            current = bucket[0]
            bucket.pop(0)
            hands[idx] = current
            idx += 1


def radixSort(hands):
    buckets = [[] for l in range(13)]
    
    for digit in reversed(range(5)):
        
        for hand in hands:
            card = hand[0]
            buckets[cardValues(card[digit]) - 2].append(hand)
  
        
        collectBuckets(hands, buckets)
        
    return hands

file = [line.strip().split(" ") for line in open("f.txt").read().split("\n")]
rankings = [[] for i in range(7)]  


for line in file:
    
    if 1 == (size := len((hand := Counter(line[0])).keys())):
        rankings[6].append(line)
    elif size == 5:
        rankings[0].append(line)
    elif size == 2:
        for amount in hand.values():
            if amount == 1:
                rankings[5].append(line)
                break
        else:
            rankings[4].append(line)
        
    elif size == 3:
        for amount in hand.values():
            if amount == 3:
                rankings[3].append(line)
                break
        else:
            rankings[2].append(line)
    elif size == 4:
        rankings[1].append(line)
    
        
for rank in rankings:
    radixSort(rank)
   
idx = 1
result = 0   
for rank in rankings:
    for hand in reversed(rank):
        result += int(hand[1]) * idx
        idx += 1

print(result)
