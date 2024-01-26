
import random as r

# Welcome message:
print("--- Welcome to High-Low ---")
print("Start with 100 points. Each round a card will be drawn and shown. \nSelect whether you think the 2nd card will be Higher or Lower than the 1st card.")
print("Then enter the amount you want to bet. \nIf you are right, you win the amount you bet, otherwise you lose. \nTry to make it to 500 points within 10 tries.")

# Main Program:
initial_points = 100

def getCardValue():
    rand =r.randint(2, 14)
    return rand


def getCardStr(cardValue):
    if cardValue >= 2 and cardValue <= 9:
        return str(cardValue)
    elif cardValue > 9 and cardValue <= 14:
        if cardValue == 10:
            cardValue = "T"
        elif cardValue == 11:
            cardValue = "J"
        elif cardValue == 12:
            cardValue = "Q"
        elif cardValue == 13:
            cardValue = "K"
        elif cardValue == 14:
            cardValue = "A"
        return cardValue
    else:
        print("Card Value is not valid")

def getHLGuess():
    HorL = input("High or Low (H/L)?: ")
    while HorL == "H" or HorL == "h" or HorL == "L"or HorL == "l":
        if HorL == "H" or HorL == "h":
            return "HIGH"
        elif HorL == "L" or HorL == "l":
            return "LOW"


def getBetAmount(maximum):
    while maximum > curPoint or maximum <= 0:
        maximum = int(input("Please enter again \nbet:"))

    return maximum

def playerGuessCorrect(card1, card2, betType):
    card1 = getCardStr(card1)
    card2 = getCardStr(card2)
    if betType == "HIGH":
        if card2 > card1:
            return True
        else:
            return False
    elif betType == "LOW":
        if card1 > card2:
            return True
        else:
            return False





def main():
    global curPoint
    curPoint = initial_points
    for i in range(0, 10):
        cardv1 = getCardValue()
        cardv2 = getCardValue()
        # getCardStr(cardValue)
        print("-------------------------------------")
        print("Overall Points: ", curPoint, "Round", str(i+1),"/10")
        print("First Card is a "+ "["+ getCardStr(cardv1)+"]")
        # HorL = input("High or Low (H/L)?: ")
        getHLGuess()
        bet = int(input("Input bet amount: "))
        getBetAmount(bet)
        print("Second Card is a " + "[" + getCardStr(cardv2) + "]")

        if playerGuessCorrect(cardv1, cardv2, "HIGH") == True:
            print("Card1 " + "["+ getCardStr(cardv1) +"] " +" Card 2 " + " [" + getCardStr(cardv2) + "] " + " - You bet " + "HIGH" + " for " + str(getBetAmount(bet)), "- YOU WIN")
            curPoint = curPoint + bet

        elif  playerGuessCorrect(cardv1, cardv2, "LOW") == True:
            print("Card1", "[" + getCardStr(cardv1) + "]", "Card 2", "[" + getCardStr(cardv2) + "]", "- You bet", "LOW", "for",
                  str(getBetAmount(bet)), "- YOU WIN")
            curPoint = curPoint + bet

        elif playerGuessCorrect(cardv1, cardv2, "HIGH") == False:
            print("Card1 " + "[" + getCardStr(cardv1) + "] " + " Card 2 " + " [" + getCardStr(
                cardv2) + "] " + " - You bet " + "HIGH" + " for " + str(getBetAmount(bet)), "- YOU LOSE")
            curPoint = curPoint - bet

        elif playerGuessCorrect(cardv1, cardv2, "LOW") == False:
            print("Card1 " + "[" + getCardStr(cardv1) + "] " + " Card 2 " + " [" + getCardStr(
                cardv2) + "] " + " - You bet " + "LOW" + " for " + str(getBetAmount(bet)), "- YOU LOSE")
            curPoint = curPoint - bet

        if curPoint >= 500:
            print("YOU WIN in ", str(i+1), "Round(s)")
            break
        elif curPoint == 0:
            print("YOU LOSE in", str(i+1), "Round(s)")
            break




main()
input("Press enter to exit. ")  # input statement to pause code when finished
