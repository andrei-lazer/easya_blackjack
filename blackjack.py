
import random

class Person():
    name = ""
    hand_cards = []
     
def createCard():
    suits = ['S', 'H', 'C', 'D']
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    Stack=[]
    deck=[(x,y)for x in cards for y in suits]
    # for x in suits:
    #     for y in cards:
    #         Stack.append(x,y)
    deck=deck*6
    for i in deck:
        print(i)
    return deck


def Users():
   
    Num_Users=int(input("Enter number of people: "))

    Users=[]
    for i in range(Num_Users):
        
        Names = input("Enter Your Name: ")
        Person1 = Person()
        Person1.name = Names
        Users.append(Names)
    print(Person1.name)
    return Users

def distributeCard(deck,users):
    random.shuffle(deck)
    for i in range(len(users)):
        player = [deck.pop(),deck.pop() ]
    dealer = [deck.pop(), deck.pop()]
    print(player)

# # Stack= 
# Users()
deck = createCard()
users = Users()
distributeCard(deck,users)

