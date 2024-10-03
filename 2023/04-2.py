
MAX_CARD = 199
cards = {}
with open("f.txt") as f:
    cardNum = 1
    for line in f:
        card = [set([num for num in card.split()]) for card in line.strip().split(": ")[-1].split(" | ")]
        cards[cardNum] = [1, card[0] & card[-1]]
        cardNum += 1
        
for line in range(1, len(cards) + 1):
    
    if cards[line][1]:
        for num in range(1, len(cards[line][1]) + 1):
            cards[line + num][0] += cards[line][0]
            
             
print(sum(cards[card][0] for card in cards))

    
