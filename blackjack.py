
import random

class Person(): # player info class
    name = ""
    hand_cards = []
     
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
        i.hand_cards=[c1,c2]
    return users,deck


def printall(deck,users):
    for i in users:
        print(i.hand_cards)
        print(i.name)

def start(deck,users):
    
    

deck = createCard() #intial deck of 6
users = Users() #number of players playing
users,deck =distributeCard(deck,users) # distribution of cards
printall(deck,users)

