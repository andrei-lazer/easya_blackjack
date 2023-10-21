
import random

class Person(): # player info class
    name = ""
    hand_cards = []
    value=0
    money=0
    inGame=True
     
def createCard(): # function to create an intial deck
    suits = ['S', 'H', 'C', 'D']
import random

class Person(): # player info class
    name = ""
    hand_cards = []
    value=0
    money=0
    inGame=True
     
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



def dealer(users,deck,OutofGameArray,WinningArray):
    loop = ingame(users[0].value)
    while (loop): 
        
        if users[0].value<11:
            drawCard(users,0,deck)
            print("-dealer draws card")

        elif users[0].value == 21:
            print("-dealer got 21")
            loop = False
            out = users.pop(0)
            WinningArray.append(out.name)
        
        elif users[0].value>=11:
            draw_var = random.randint(0,1)
            if draw_var == 1 and users[0].value<21:
                drawCard(users,0,deck)
                print("-dealer draws card")
            elif users[0].value == 21:
                print("-dealer got 21")
                loop = False
                out = users.pop(0)
                WinningArray.append(out.name)
            else:
                print("-dealer stop")
                loop = False
        
        # elif users[0].value> 21:
        #     print("-dealer stop")
        #     loop = False
        #     out = users.pop(0)
        #     OutofGameArray.append(out)
                
    return deck,users


def getval(card):
    if card in ["Q","J","K"]:
        return 10
    elif card == "A":
        return 11
    else:
        return int(card)

def ingame(val):
    
    if val>21:
        print("-Player out")
        return False
    else:
        return True

def gameover(WinningArray,users):
    print ("- The Game over")
    winningbets(users, WinningArray, 50)
    quit()
    


def start(deck,users):

    OutofGameArray = []
    IngameCount=len(users)
    WinningArray = []
    deck,users=dealer(users,deck,OutofGameArray,WinningArray)
    loop=True
    
   
    while loop:
        for i in range (1,IngameCount):
            print(" ")
            print("dealer")
            print(users[0].hand_cards)
            
            hit=True
            while (hit):
                print (users[i].name)
                if (users[i].value) == 21:
                    IngameCount=IngameCount-1
                    if (IngameCount==1):
                            gameover(WinningArray,users)
                            loop=False
                    out = users.pop(i)
                    WinningArray.append(out.name)
                    hit = False

                play=input("Enter 1 to hit or 0 to stop")
                if play=="1":
                    print ("you hit")
                    deck,users=drawCard(users,i,deck)
                    if(ingame(users[i].value)):
                        users[i].inGame=True
                    else:
                        users[i].inGame=False
                        IngameCount=IngameCount-1
                        out = users.pop(i)
                        OutofGameArray.append(out.name)
                        if (IngameCount==1):
                            gameover(WinningArray,users)
                            loop=False
                        
                elif play=="0":
                    print("you stopped")
                    users[i].inGame=False
                    IngameCount=IngameCount-1
                    if (IngameCount==1):
                            gameover(WinningArray,users)
                            loop=False
                    hit=False
    
    return deck,users

def winningbets(users,WinningArray,totalbets):
    if(len(WinningArray)!=0):
        print("The winners are: ",WinningArray)
        bets=totalbets/len(WinningArray)
        print(bets)
        return WinningArray, bets
            #multiple 21 winner split total equally
    else:
        
        for i in range (1,len(users)):
            print("The Winners are: ", users[i].name)
        bets=totalbets/len(users)
        print(bets)
        return users, bets



deck = createCard() #intial deck of 6
users = Users() #number of players playing
users,deck =distributeCard(deck,users) # distribution of cards
printall(deck,users)

deck,users=start(deck,users)
printall(deck,users)





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



def dealer(users,deck,OutofGameArray,WinningArray):
    loop = ingame(users[0].value)
    while (loop): 
        
        if users[0].value<11:
            drawCard(users,0,deck)
            print("-dealer draws card")

        elif users[0].value == 21:
            print("-dealer got 21")
            loop = False
            out = users.pop(0)
            WinningArray.append(out.name)
        
        elif users[0].value>=11:
            draw_var = random.randint(0,1)
            if draw_var == 1 and users[0].value<21:
                drawCard(users,0,deck)
                print("-dealer draws card")
            elif users[0].value == 21:
                print("-dealer got 21")
                loop = False
                out = users.pop(0)
                WinningArray.append(out.name)
            else:
                print("-dealer stop")
                loop = False
        
        # elif users[0].value> 21:
        #     print("-dealer stop")
        #     loop = False
        #     out = users.pop(0)
        #     OutofGameArray.append(out)



                
    return deck,users


def getval(card):
    if card in ["Q","J","K"]:
        return 10
    elif card == "A":
        return 11
    else:
        return int(card)

def ingame(val):
    
    if val>21:
        print("-Player out")
        return False
    else:
        return True

def gameover(WinningArray):
    print ("- The Game over")
    print(WinningArray, "These guys Win the Game")
    quit()
    


def start(deck,users):

    OutofGameArray = []
    IngameCount=len(users)
    WinningArray = []
    deck,users=dealer(users,deck,OutofGameArray,WinningArray)
    loop=True
    
   
    while loop:
        for i in range (1,IngameCount):
            print(" ")
            print("dealer")
            print(users[0].hand_cards)
            
            hit=True
            while (hit):
                print (users[i].name)
                if (users[i].value) == 21:
                    IngameCount=IngameCount-1
                    if (IngameCount==1):
                            gameover(WinningArray)
                            loop=False
                    out = users.pop(i)
                    WinningArray.append(out.name)
                    hit = False

                play=input("Enter 1 to hit or 0 to stop")
                if play=="1":
                    print ("you hit")
                    deck,users=drawCard(users,i,deck)
                    if(ingame(users[i].value)):
                        users[i].inGame=True
                    else:
                        users[i].inGame=False
                        IngameCount=IngameCount-1
                        out = users.pop(i)
                        OutofGameArray.append(out.name)
                        if (IngameCount==1):
                            gameover(WinningArray)
                            loop=False
                        
                elif play=="0":
                    print("you stopped")
                    users[i].inGame=False
                    IngameCount=IngameCount-1
                    if (IngameCount==1):
                            gameover(WinningArray)
                            loop=False
                    hit=False
    
    return deck,users

        

deck = createCard() #intial deck of 6
users = Users() #number of players playing
users,deck =distributeCard(deck,users) # distribution of cards
printall(deck,users)

deck,users=start(deck,users)
printall(deck,users)




