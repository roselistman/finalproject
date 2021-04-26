import random

# Here are some coding examples that I looked at / took inspiration from:
# https://www.askpython.com/python/examples/blackjack-game-using-python
# https://samarakoon-gayan.medium.com/a-game-of-black-jack-on-python-as-a-fun-exercise-3cd54efb9d83
# https://towardsdatascience.com/lets-play-blackjack-with-python-913ec66c732f
# https://codereview.stackexchange.com/questions/149889/simple-blackjack-game-in-python
# https://gist.github.com/mjhea0/5680216

def makeDeck():
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

    deck = []
    for card in faces:
        for suit in suits:
            deck.append(card + " " + suit)

    return deck

def handValue(hand):
    tenValues = ["1", "J", "Q", "K"]
    total = 0
    aceCount = 0
    for card in hand:
        if card[0] in tenValues:
            total += 10
        elif card[0] == "A":
            total += 11
            aceCount += 1
        else:
            total += int(card[0])

    while total > 21 and aceCount > 0:
        total -= 10
        aceCount -= 1

    return total

def possibleMoves(hand, turn):
    card1 = hand[0]
    card2 = hand[1]
    if turn > 1:
        moves = ['hit', 'stand']
    elif turn == 1:
        if card1[0] == card2[0]:
            moves = ['hit', 'stand', 'double', 'split']
        else:
            moves = ['hit', 'stand', 'double']
    return moves

def split(pHand, dHand, deck, playerBet, playerBetSplit):

    du = dHand[1]
    dd = dHand[0]
    dValue = handValue(dHand)

    newCard1 = deck.pop(0)
    pHandSplit1 = [pHand[0], newCard1]
    print("Hand 1 new card: " + newCard1)
    pSplitValue1 = handValue(pHandSplit1)
    print("Hand 1 new value: " + str(pSplitValue1))

    newCard2 = deck.pop(0)
    pHandSplit2 = [pHand[1], newCard2]
    print("Hand 2 new card: " + newCard2)
    pSplitValue2 = handValue(pHandSplit2)
    print("Hand 2 new value: " + str(pSplitValue2))

    turn = 1
    stillPlaying = True


    while stillPlaying == True:

        if pSplitValue1 >= 21:
            stillPlaying = False

        if stillPlaying == True:
        
            print("Hand 1 possible moves: ")

            moves = possibleMoves(pHandSplit1, turn)
            for move in moves:
                if move == 'split':
                    pass
                else:
                    print(move)

            pMove = input("What would you like to do with hand 1? ").lower()

            while pMove not in moves or pMove == 'split':
                pMove = input("Enter an acceptable move: ").lower()

            correctMove = basicStrategyMove(pHandSplit1[0], pHandSplit1[1], pHandSplit1, du, moves)

            if pMove == correctMove:
                print('That is the correct move according to basic strategy')
            else:
                print('That is the incorrect move according to basic strategy, the correct move is ' + correctMove)

            if pMove == 'stand':
                stillPlaying = False

            if pMove == 'double':
                
                playerBet *= 2

                newCard = deck.pop(0)
                pHandSplit1.append(newCard)
                print("New card: " + newCard)
                pSplitValue1 = handValue(pHandSplit1)
                print("New value: " + str(pSplitValue1))
                stillPlaying = False

            if pMove == 'hit':
                newCard = deck.pop(0)
                pHandSplit1.append(newCard)
                print("New card: " + newCard)
                pSplitValue1 = handValue(pHandSplit1)
                print("New value: " + str(pSplitValue1))

            if pSplitValue1 >= 21:
                stillPlaying = False

            turn += 1

    turn = 1
    stillPlaying = True

    while stillPlaying == True:

        if pSplitValue2 >= 21:
           stillPlaying = False

        if stillPlaying == True:
        
            print("Hand 2 possible moves: ")
            moves = possibleMoves(pHandSplit2, turn)
            for move in moves:
                if move == 'split':
                    pass
                else:
                    print(move)

            pMove = input("What would you like to do with hand 2? ").lower()

            while pMove not in moves or pMove == 'split':
                pMove = input("Enter an acceptable move: ").lower()

            correctMove = basicStrategyMove(pHandSplit2[0], pHandSplit2[1], pHandSplit2, du, moves)

            if pMove == correctMove:
                print('That is the correct move according to basic strategy')
            else:
                print('That is the incorrect move according to basic strategy, the correct move is ' + correctMove)

            if pMove == 'stand':
                stillPlaying = False

            if pMove == 'double':

                playerBetSplit *= 2

                newCard = deck.pop(0)
                pHandSplit2.append(newCard)
                print("New card: " + newCard)
                pSplitValue2 = handValue(pHandSplit2)
                print("New value: " + str(pSplitValue2))
                stillPlaying = False

            if pMove == 'hit':
                newCard = deck.pop(0)
                pHandSplit2.append(newCard)
                print("New card: " + newCard)
                pSplitValue2 = handValue(pHandSplit2)
                print("New value: " + str(pSplitValue2))
        
            if pSplitValue2 >= 21:
                stillPlaying = False

            turn += 1

    if pSplitValue2 > 21 and pSplitValue1 > 21:
        return pSplitValue1, pSplitValue2, dValue, playerBet, playerBetSplit
 
    print("Dealer down card: " + dd)
    print("Dealer value: " + str(dValue))

    while dValue <= 16:
        newCard = deck.pop(0)
        dHand.append(newCard)
        print("New card: " + newCard)
        dValue = handValue(dHand)
        print("New value: " + str(dValue))

    return pSplitValue1, pSplitValue2, dValue, playerBet, playerBetSplit

    
def mainGame(deck, playerBet, playerBetSplit):

    random.shuffle(deck)

    p1 = deck.pop(0)
    dd = deck.pop(0)
    p2 = deck.pop(0)
    du = deck.pop(0)

    pHand = [p1, p2]
    dHand = [dd, du]
    pHandSplit1 = []
    pHandSplit2 = []    

    pValue = handValue(pHand)
    dValue = handValue(dHand)

    pSplitValue1 = 0
    pSplitValue2 = 0

    print("Your hand: " + p1 + ", " + p2)
    print("Player value: " + str(pValue))
    print("Dealer up card: " + du)

    stillPlaying = True

    turn = 1

    while stillPlaying == True:

        if pValue >= 21:
            if pValue > 21:
                return "player bust"
                stillPlaying = False
            else:
                stillPlaying = False

        if stillPlaying == True:
            print("Possible moves: ")
            moves = possibleMoves(pHand, turn)
            for move in moves:
                print(move)

            pMove = input("What would you like to do? ").lower()

            while pMove not in moves:
                pMove = input("Enter an acceptable move: ").lower()

            correctMove = basicStrategyMove(p1, p2, pHand, du, moves)

            if pMove == correctMove:
                print('That is the correct move according to basic strategy')
            else:
                print('That is the incorrect move according to basic strategy, the correct move is ' + correctMove)

            if pMove == 'stand':
                stillPlaying = False

            if pMove == 'double':

                playerBet *= 2

                newCard = deck.pop(0)
                pHand.append(newCard)
                print("New card: " + newCard)
                pValue = handValue(pHand)
                print("New value: " + str(pValue))
                stillPlaying = False

            if pMove == 'hit':
                newCard = deck.pop(0)
                pHand.append(newCard)
                print("New card: " + newCard)
                pValue = handValue(pHand)
                print("New value: " + str(pValue))

            if pMove == 'split':
                return split(pHand, dHand, deck, playerBet, playerBetSplit)

            if pValue >= 21:
                if pValue > 21:
                    return "player bust"
                stillPlaying = False

            turn += 1

    
    print("Dealer down card: " + dd)
    print("Dealer value: " + str(dValue))

    while dValue <= 16:
        newCard = deck.pop(0)
        dHand.append(newCard)
        print("New card: " + newCard)
        dValue = handValue(dHand)
        print("New value: " + str(dValue))

    return pValue, dValue, playerBet

def endGame(playerChips):

    playerBet = 10
    playerBetSplit = 10
    output = ""
    output2 = ""

    deck = makeDeck()

    result = mainGame(deck, playerBet, playerBetSplit)

    if result == "player bust":
        playerChips -= playerBet
        output = "Player Bust, Dealer Win!"

    elif len(result) == 3:

        player = result[0]
        dealer = result[1]
        playerBet = int(result[2])

        if player == 21:
            if dealer == 21:
                output = "Player Blackjack, Dealer Blackjack, Push!"
            elif dealer > 21:
                playerChips += playerBet
                output = "Dealer Bust, Player Blackjack, Player Win!"
            else:
                playerChips += playerBet
                output = "Player Blackjack, Player Win!"
        elif dealer == 21:
            playerChips -= playerBet
            output = "Dealer Blackjack, Dealer Win!"
        elif dealer > 21:
            playerChips += playerBet
            output = "Dealer Bust, Player Win!"
        elif dealer > player:
            playerChips -= playerBet
            output = "Dealer Win!"
        elif player > dealer:
            playerChips += playerBet
            output = "Player Win!"
        elif dealer == player:
            output = "Push!"

    elif len(result) == 5:
        player1 = result[0]
        player2 = result[1]
        dealer = result[2]
        playerBet = int(result[3])
        playerBetSplit = int(result[4])

        if player1 > 21:
            playerChips -= playerBet
            output = "Hand 1 Bust, Dealer Win!"
        elif player1 == 21:
            if dealer == 21:
                output = "Hand 1 Blackjack, Dealer Blackjack, Push!"
            elif dealer > 21:
                playerChips += playerBet
                output = "Dealer Bust, Hand 1 Blackjack, Hand 1 Win!"
            else:
                playerChips += playerBet
                output = "Hand 1 Blackjack, Hand 1 Win!"
        elif dealer == 21:
            playerChips -= playerBet
            output = "Hand 1 Dealer Blackjack, Dealer Win!"
        elif dealer > 21:
            playerChips += playerBet
            output = "Dealer Bust, Hand 1 Win!"
        elif dealer > player1:
            playerChips -= playerBet
            output = "Hand 1 Dealer Win!"
        elif player1> dealer:
            playerChips += playerBet
            output = "Hand 1 Win!"
        elif dealer == player1:
            output = "Hand 1 Push!"

        if player2 > 21:
            playerChips -= playerBet
            output2 = "Hand 2 Bust, Dealer Win!"
        elif player2 == 21:
            if dealer == 21:
                output2 = "Hand 2 Blackjack, Dealer Blackjack, Push!"
            elif dealer > 21:
                playerChips += playerBetSplit
                output2 = "Dealer Bust, Hand 2 Blackjack, Hand 2 Win!"
            else:
                playerChips += playerBetSplit
                output2 = "Hand 2 Blackjack, Hand 2 Win!"
        elif dealer == 21:
            playerChips -= playerBetSplit
            output2 = "Hand 2 Dealer Blackjack, Dealer Win!"
        elif dealer > 21:
            playerChips += playerBetSplit
            output2 = "Dealer Bust, Hand 2 Win!"
        elif dealer > player2:
            playerChips -= playerBetSplit
            output2 = "Hand 2 Dealer Win!"
        elif player2 > dealer:
            playerChips += playerBetSplit
            output2 = "Hand 2 Win!"
        elif dealer == player2:
            output2 = "Hand 2 Push!"

    return output, output2, playerChips

def play(condition, playerChips):   
    print('\n')
    result = endGame(playerChips)
    output = result[0]
    output2 = result[1]
    if output2 == "":
        print(output)
        print('\n')
    else:
        print(output)
        print(output2)
        print('\n')
    playerChips = result[2]

    print('Chips left: ' + str(playerChips))
    print('\n')

    return playerChips


def basicStrategyMove(pCard1, pCard2, pHand, du, possibleMoves):
    faces = ['J','Q','K']
    dCard = du[0]
    if dCard == '1':
        dCard = '10'
    if dCard in faces:
        dCard = '10'   

    pValue = handValue(pHand)

    if 'split' not in possibleMoves:
        if pCard1[0] != 'A' and pCard2[0] != 'A':
            if pValue >= 17 and pValue <= 21:
                correctMove = 'stand'
            elif pValue >= 13:
                if dCard == '6' or dCard == '5' or dCard == '4' or dCard == '3' or dCard == '2':
                    correctMove = 'stand'
                else:
                    correctMove = 'hit'
            elif pValue == 12:
                if dCard == '2' or dCard == '3':
                    correctMove = 'hit'
                elif dCard == '4' or dCard == '5' or dCard == '6':
                    correctMove = 'stand'
                else:
                    correctMove = 'hit'
            elif pValue == 11:
                if dCard == 'A':
                    correctMove = 'hit'
                else:
                    if 'double' in possibleMoves:
                        correctMove = 'double'
                    else:
                        correctMove = 'hit'
            elif pValue == 10:
                if dCard == 'A' or dCard == '10':
                    correctMove = 'hit'
                else:
                    if 'double' in possibleMoves:
                        correctMove = 'double'
                    else:
                        correctMove = 'hit'
            elif pValue == 9:
                if dCard == 'A' or dCard == '10' or dCard == '9' or dCard == '8' or dCard == '7' or dCard == '2':
                    correctMove = 'hit'
                else:
                    if 'double' in possibleMoves:
                        correctMove = 'double'
                    else:
                        correctMove = 'hit'
            elif pValue >= 5:
                correctMove = 'hit'
        elif pCard1[0] == 'A' or pCard2[0] == 'A':
            if pValue >= 19 and pValue <= 21:
                correctMove = 'stand'
            elif pValue == 18:
                if dCard == '2' or dCard == '7' or dCard == '8':
                    correctMove = 'stand'
                elif dCard == '9' or dCard == '10' or dCard == 'A':
                    correctMove = 'hit'
                else:
                    if 'double' in possibleMoves:
                        correctMove = 'double'
                    else:
                        correctMove = 'hit'
            elif pValue == 17:
                if dCard == '2' or dCard == '7' or dCard == '8' or dCard == '9' or dCard == '10' or dCard == 'A':
                    correctMove = 'hit'
                else:
                    if 'double' in possibleMoves:
                        correctMove = 'double'
                    else:
                        correctMove = 'hit'
            elif pValue >= 15:
                if dCard == '2' or dCard == '3' or dCard == '7' or dCard == '8' or dCard == '9' or dCard == '10' or dCard == 'A':
                    correctMove = 'hit'
                else:
                    if 'double' in possibleMoves:
                        correctMove = 'double'
                    else:
                        correctMove = 'hit'
            elif pValue >= 13:
                if dCard == '2' or dCard == '3' or dCard == '4' or dCard == '7' or dCard == '8' or dCard == '9' or dCard == '10' or dCard == 'A':
                    correctMove == 'hit'
                else:
                    if 'double' in possibleMoves:
                        correctMove = 'double'
                    else:
                        correctMove = 'hit'
    elif 'split' in possibleMoves:
        if pCard1[0] == 'A' or pCard1[0] == '8':
            correctMove = 'split'
        elif pCard1[0] == '1' or pCard1[0] in faces:
            correctMove = 'stand'
        elif pCard1[0] == '9':
            if dCard == '7' or dCard == '10' or dCard == 'A':
                correctMove = 'stand'
            else:
                correctMove = 'split'
        elif pCard1[0] == '7':
            if dCard == '8' or dCard == '9' or dCard == '10' or dCard == 'A':
                correctMove = 'hit'
            else:
                correctMove = 'split'
        elif pCard1[0] == '6':
            if dCard == '7' or dCard == '8' or dCard == '9' or dCard == '10' or dCard == 'A':
                correctMove = 'hit'
            else:
                correctMove = 'split'
        elif pCard1[0] == '5':
            if dCard == '10' or dCard == 'A':
                correctMove = 'hit'
            else:
                if 'double' in possibleMoves:
                    correctMove = 'double'
                else:
                    correctMove = 'hit'
        elif pCard1[0] == '4':
            if dCard == '5' or dCard == '6':
                correctMove = 'split'
            else:
                correctMove = 'hit'
        elif pCard1[0] == '3' or pCard1[0] == '2':
            if dCard == '8' or dCard == '9' or dCard == '10' or dCard == 'A':
                correctMove = 'hit'
            else:
                correctMove = 'split'

    return correctMove


condition = (input('Start game (y/n)? ')).lower()

acceptableConditions = ['y','n']

while condition not in acceptableConditions:
    condition = (input('Start game (y/n)? Please input an acceptable response: ')).lower()

playerChips = 300

if condition == 'y':
    print('\n')
    print('The game will stop when you choose, or when you have less than 40 chips left')
    print('Blackjack pays 1:1, no resplitting allowed')
    print("Deck shuffles every hand so you can't count cards")
    print("No splitting non-matching face cards")
    print('\n')
    
    playerChips = 300

    print('Starting chips: ' + str(playerChips))
    print('\n')

while condition == 'y' and playerChips >= 40:
    playerChips = play(condition, playerChips)
    if playerChips >= 40:
            condition = input('Keep playing (y/n)? ').lower()
            while condition not in acceptableConditions:
                condition = (input('Keep playing (y/n)? Please input an acceptable response: ')).lower()
            print('\n')

print("End of game. Final chip count: " + str(playerChips))
