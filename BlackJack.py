#Created August 24, 2022    Gabriel Sutherland BlackJack Game
import random, itertools
#Things to add Dealer/#of user hands, Card list, Split/Double Hand, Hit or Stand, Place Bets, Shuffle Deck, $$Rules$$.
def welcome():

    start = input("Would you like to [1] Start playing BlackJack or [2] Learn how to play BlackJack: ")

    if start == "1":
        gameSetup(0)
    elif start == "2":
        rules()
    else:
        welcome()
    
#Prints out rules of BlackJack game and returns welcome message again
def rules():
    print("""           ============================================================RULES==================================================================
            The Rules of Gabriels BlackJack are very simple you place a bet of $1 or higher and try to get as close to 21 as possible without
            going over. Then recieve two cards per hand(s) you have. Every Card is worth its own value Example. 8 of Diamonds would equal 8.
            While Face cards (Jack-Queen-King) are all equal to 10. Ace is a little more complicated as it can be either equal 
            to either 1 or 11.  Meaning if my hand consistes of a Jack, an 8, and an Ace the hand could equal 19 or 29 defaulting to 19
            since its below 21 if your hand ever goes over 21 while having an Ace in the hand the Ace will then become a 1 automatically.
           ===================================================================================================================================""")
    welcome()
           
#Asks the player if they would like to Deposit/Withdraw money and How many hands they would like to be dealt when the game starts 
def gameSetup(balance):
    ans = input("Would you like to [1] Depost or [2] Withdraw money: ")
    if ans == '1':
        deposit = input("How much money do you want to deposit: ")
        balance += int(deposit)
    elif ans == '2':
        withdraw = input("How much money do you want to withdraw: ")
        if int(withdraw) <= balance:
            balance -= int(withdraw)
        else:        
            print("Not enough funds")
            gameSetup(balance)
    else:
        gameSetup(balance)
    print("You now have a balance of $",balance)
    
#Asks player how many hands they want to play with and has a max of 6
def howManyHands(balance):
    num_hands = input("How many hands would you like to be dealt max 6: ")
    if num_hands > 6:
        print("Too many hands please choose 6 or less")
        howManyHands(balance)
    bets(balance, num_hands)
        
#Makes sure bets are eligible and shuffles the deck 
def bets(balance, hands):
    bet_list = []
    for i in range(int(hands)):
        i += 1
        bet = input("How much do you want to bet for hand #"+str(i)+": ")
        bet_list.append(int(bet))
    total = sum(bet_list)
    if total > balance:
        print("Not enough money to place bets. Try again")
        bets(balance, hands)
    balance -= total
    print(balance)
    deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# shuffle the cards
    random.shuffle(deck)
    deal(bet_list, balance, deck)
   
#Deals out hands to player and removes dealt hands from deck, Passes hands, bets, balance and deck to action() 
def deal(bets, balance, deck):
    hand = []
    hands = {}
    for index in range(len(bets)):
        #Deals two cards to each hand
        for i in range(2):
            card= deck[i][0], "of", deck[i][1]
            #Adds card to respective hand dictionary and removes it from deck
            hand.append(str(card))
            deck.pop([i][0])
            #If only getting dealt one card hands change hand[2:5] to either hand[3:5] or hand[2:5] across all hand variables in if/elif statments 
            if index == 0:
                hands[index] = hand[0:2]
            elif index == 1:
                hands[index] = hand[2:5]
            elif index == 2:
                hands[index] = hand[4:7]
            elif index == 3:
                hands[index] = hand[6:9]
            elif index == 4:
                hands[index] = hand[8:11]
            elif index == 5:
                hands[index] = hand[10:]
    action(hands, bets, balance, deck)
    
#R
def action(hands, bets, balance, deck, amount = 0):
    #Dealers hand
    dealerHand = []
    if dealerHand == []:
        for i in range(2):
            dealerCard = deck[i][0], "of", deck[i][1]
            dealerHand.append(str(dealerCard))
            deck.pop([i][0])
    print("The dealer hand:",dealerHand)
    for hand in hands:
        
        print("Your hand(s):", hands[hand],"Total:", sumHands(hands, hand, dealerHand, amount))

def sumHands(hands, hand, dealer, amount = 0):
    for x in hands[hand]:
        if "1" in x:
            if amount > 21:
                amount += 1
            else:
                amount += 11
        if "2" in x:
            amount += 2
        if "3" in x:
            amount += 3
        if "4" in x:
            amount += 4
        if "5" in x:
            amount += 5
        if "6" in x:
            amount += 6
        if "7" in x:
            amount += 7
        if "8" in x:
            amount += 8
        if "9" in x:
            amount += 9
        if "10" in x:
            amount += 10
        if "11" in x:
            amount += 10
        if "12" in x:
            amount += 10
        if "13" in x:
            amount += 10       
    print(hands[hand])
    print(amount)
    return amount
            
    
       
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# shuffle the cards
random.shuffle(deck) 
deal([5, 10, 15, 1, 2, 2], 200, deck)