
import random

class Person(): # player info class
    name = ""
    hand_cards = []
    value=0
    money=0
     
def createCard(): # function to create an intial deck
    suits = ['S', 'H', 'C', 'D']
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck=[(x,y)for x in cards for y in suits]
    deck=deck*6
    return deck


def Users(): # number of players 
    while True:
        try:
            Num_Users=int(input("Enter number of people: "))
        except ValueError:
            print("Provide an integer value...")
            continue
        else:
            break
            


    Users=[]
    Users.append(Person())
    Users[0].name="Dealer"
    for i in range(Num_Users):
        Users.append(Person())
        Name = input("Enter Your Name: ")
        Users[i+1].name = Name
    
    return Users


def distributeCard(deck,users):
    random.shuffle(deck)
    for i in users:
        c1=deck.pop()
        c2=deck.pop()
        val=getval(c1[0])+getval(c2[0])
        i.value=val
        i.hand_cards=[c1,c2]
    return users,deck


def printall(deck,users):
    for i in users:
        print (i.name)
        print (i.hand_cards)
        print (i.value)
        
def drawCard(users,pos,deck):
    c=deck.pop()
    users[pos].value=users[pos].value+getval(c[0])
    users[pos].hand_cards.append(c)
    print (users[pos].hand_cards)
    print (users[pos].value)
    
    return deck,users

def start(deck,users):
    for i in range (1,len(users)):
        play=input("Enter 1 to hit or 0 to stop")
        if play=="1":
            print ("you hit")
            deck,users=drawCard(users,i,deck)
        elif play=="0":
            print("you stopped")
    return deck,users
def dealer(users,deck):
    while (users[0].value != 21): 
        if users[0].value<11:
            drawCard(users,0,deck)
        elif users[0].value>=11:
            draw_var = random.randint(0,1)
            if draw_var == 1:
                drawCard(users,0,deck)
            else:
                print("stop")
                break
        
def getval(card):
    if card in ["Q","J","K"]:
        return 10
    elif card == "A":
        return 11
    else:
        return int(card)


deck = createCard() #intial deck of 6
users = Users() #number of players playing
users,deck =distributeCard(deck,users) # distribution of cards
printall(deck,users)
deck,users=start(deck,users)
deck,users=dealer(users,deck)



