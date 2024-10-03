
from collections import Counter, defaultdict


def cardValues(char):
    if char.isdigit():
        return int(char)
    cardMap = {"T" : 10, "J" : 1, "Q" : 11, "K" : 12, "A" : 13}
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
            buckets[cardValues(card[digit]) - 1].append(hand)
  
        
        collectBuckets(hands, buckets)
        
    return hands

file = [line.strip().split(" ") for line in open("f.txt").read().split("\n")]
rankings = [[] for i in range(7)]  


for line in file:
    
    if 1 == (size := len((hand := Counter(line[0])).keys())):
        rankings[6].append(line)
    
    elif size == 2:
        for amount in hand.values():
            if amount == 1:
                if "J" in hand.keys():
                    rankings[6].append(line)
                else:
                    rankings[5].append(line)
                break
        else:
            if "J" in hand.keys():
                rankings[6].append(line)
            else: 
                rankings[4].append(line)
        
    elif size == 3:
        for amount in hand.values():
            if amount == 3:
                if "J" in hand.keys():
                    rankings[5].append(line)
                else:
                    rankings[3].append(line)
                break
        else:
            if "J" in hand.keys():
                if hand["J"] > 1:
                    rankings[5].append(line)
                else:
                    rankings[4].append(line)
            else:
                rankings[2].append(line)
    elif size == 4:
        if "J" in hand.keys():
                rankings[3].append(line)
        else: 
            rankings[1].append(line)
    elif size == 5:
        if "J" in hand.keys():
                rankings[1].append(line)
        else: 
            rankings[0].append(line)
    
        
for rank in rankings:
    radixSort(rank)
   
idx = 1
result = 0   
for rank in rankings:
    for hand in reversed(rank):
        result += int(hand[1]) * idx
        idx += 1

print(result)

