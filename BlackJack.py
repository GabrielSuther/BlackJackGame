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
    howManyHands(balance)
    
#Asks player how many hands they want to play with and has a max of 6
def howManyHands(balance):
    num_hands = input("How many hands would you like to be dealt max 6: ")
    if int(num_hands) > 6:
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
    print("You're balance after placing bets is:",balance)
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
    
#Asks player gets option to Hit, Stay, Double or Split their hand and dealer hand gets dealt as well
def action(hands, bets, balance, deck):
    #Initalizes var splitCount to count how many split hands and var amountList holds hand value of player hands and splitHands dict
    splitCount = 0
    amountList = []
    splitHands = {}
    #Dealers hand
    dealerHand = []
    if dealerHand == []:
        for i in range(2):
            dealerCard = deck[i][0], "of", deck[i][1]
            dealerHand.append(str(dealerCard))
            deck.pop([i][0])
            print("The dealer hand:",dealerHand)
    for hand in hands:
        split = 0
        doublecount = 0
        amount = 0
        print("Your hand(s):", hands[hand],"Total:", sumHands(hands, hand, dealerHand, amount))
        print("Amount bet $"+str(bets[hand])) 
        #Runs hand and should go to next hand if player busts 
        while amount < 21:
            print("START", amount)
            option = input("What do you want to do [1] Hit [2] Stay [3] Double [4] Split: ")
            #Adds one card to hand while taking on out of deck and returning new amount of hand
            if option == "1":
                print("Hit!")
                card= deck[i][0], "of", deck[i][1]
                #Adds card to respective hand dictionary and removes it from deck
                hands[hand].append(str(card))
                deck.pop([i][0])
                print("Your hand(s):", hands[hand],"Total:", sumHands(hands, hand, dealerHand, amount),"\n")
                amount = sumHands(hands, hand, dealerHand, amount)
            #Breaks and goes to next hand of player Hands
            elif option == '2':
                print("Stay!")
                amountList.append(sumHands(hands, hand, dealerHand, amount))
                break
            #Doubles bet as long as player has enough money, gives/removes one card, continues game to next player hand
            elif option == '3':
                if balance > bets[hand] * 2:
                    balance -= bets[hand] * 2
                    print("Updated Balance $"+str(balance))
                    bets[hand] *= 2
                    print("New bet amount $", bets[hand])
                    card= deck[i][0], "of", deck[i][1]
                     #Adds card to respective hand dictionary and removes it from deck
                    hands[hand].append(str(card))
                    deck.pop([i][0])
                    print("Your hand(s):", hands[hand],"Total:", sumHands(hands, hand, dealerHand, amount))
                    amountList.append(sumHands(hands, hand, dealerHand, amount))
                    break
                elif balance < bets[hand] * 2:
                    print("Not enough funds to double bet")
            elif option == '4':
                if split == 0:
                    if balance > bets[hand]:
                        x = []
                        y = []
                        x, y = hands[hand]
                        splitHands[splitCount] = x
                #print(hands[hand])
                        hands[hand].remove(x)
                #print(hands[hand])
                #print(splitHands)
                        print(bets)
                        bets.append(bets[hand])
                        print(bets)
                    elif balance < bets[hand]:
                        print("Not enough funds to split hand")
                else:
                    print("You already split this hand")
                split = 1

#Adds cards in a hand together
def sumHands(hands, hand, dealer, amount):
    print("BEFORE",amount)
    for x in hands[hand]:
        if "13" in x:
            amount += 10 
        elif "12" in x:
            amount += 10
        elif "11" in x:
            amount += 10
        elif "10" in x:
            amount += 10
        elif "9" in x:
            amount += 9
        elif "8" in x:
            amount += 8
        elif "7" in x:
            amount += 7
        elif "6" in x:
            amount += 6
        elif "5" in x:
            amount += 5
        elif "4" in x:
            amount += 4
        elif "3" in x:
            amount += 3
        elif "2" in x:
            amount += 2
        elif "(1," in x:
            amount += 11
            #if amount > 21:
                #amount -= 10
    cards = hands[hand]       
    
    
    if amount > 21:
        
        print("TESTTY",amount)
        for x in cards:
            print(x)
            if "(1," in x:
                print("HFJHFDKJLSFHSDKJHKDFS")
                amount -= 10
                print("MIDDLE",amount)
        if amount > 21:
            print("========================================!BUST!========================================")
    elif amount == 21:
        print("========================================!!!BJ!!!========================================")
            
    #1print(hand)
    print("END",amount)
    return amount
            

    
       
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# shuffle the cards
random.shuffle(deck) 
deal([101, 3, 2, 1, 7, 1], 100, deck)
#welcome()