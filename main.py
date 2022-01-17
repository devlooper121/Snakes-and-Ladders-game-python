import os # for clearing screen
from time import sleep # for little break before clearing console
from random import randint # for dice rool
# ladders dictonary with start as key and end as value
ladders = {2:23,8:34,20:77,32:68,41:79,74:88,78:99,85:95}
# snakes dictonary with start as key and end as value
snakes = {29:9,38:15,47:5,53:33,62:37,86:54,92:70,97:25}
# this repersent different players TOKEN
logo = "abcdefghijklmnopqrstuvwxyz"
rank = 1

# this is clear function 
# from os module we can get os name and the we apply command for clearing screen
def clear():
    '''
    this is clear function 
    from os module we can get os name and the we apply command for clearing screen
    '''
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

# this is first function that can draw board for only one time
# it can access memory of previous players TOKEN position from players list by index
# and repersent all at once without problem
# it draws snake board from 1 to 100 and also repersents ladders and snake position
# it take two argument. 1st as player number or index 2nd as player list(array)
# after every full iteration it increase the value of player location by 1 point
# means it also move TOKEN by one move  
def draw(player, players)->None:
    '''
    this is first function that can draw board for only one time
    it can access memory of previous players TOKEN position from players list by index
    and repersent all at once without problem
    it draws snake board from 1 to 100 and also repersents ladders and snake position
    it take two argument. 1st as player number or index 2nd as player list(array)
    after every full iteration it increase the value of player location by 1 point
    means it also move TOKEN by one move 
    '''
    x = 100
    players[player] = players[player]+1
    for i in range(21):
        for j in range(22):
            temp = ""
            ex = ''
            if(x in ladders):
                ex = "LS"
            elif x in ladders.values():
                ex = "LE"
            elif x in snakes:
                ex = "SM"
            elif x in snakes.values():
                ex = "ST"
            else:
                ex = str(x)
            if i == 0 or j == 0 or i == 20 or j == 21:
                print("####",end="")
            elif(i%2 == 0):
                print("----",end="")
            elif(i%2 != 0 and j%2==0):
                print("|",end="")
            else:
                for i in range(len(players)):
                    if players[i] == x:
                        temp += logo[i]
                    else:
                        temp += " "
                if (x == 100):
                    print("Finish.",end="")
                else:
                    print("{0:<2} {temp}".format(ex,temp=temp),end="")
                x -= 1
        print()
    print("NOTE: LS= ladder Start, LE= ladder End, SM= snake mouth ST= snake tail")

# It is Extention of draw() function that take 3ree arguments 
# 1st as player index 2nd as final point where it gonna move
# 3rd as player list(array)
# it runs draw() until end position making totaly running TOKEN
# sleep make sure we can see all move of TOKEN

def draw_me(player, end, players):
    '''
    It is Extention of draw() function that take 3ree arguments 
    1st as player index 2nd as final point where it gonna move
    3rd as player list(array)
    it runs draw() until end position making totaly running TOKEN
    sleep make sure we can see all move of TOKEN
    '''
    while players[player] < end:
        sleep(1)
        clear()
        draw(player,players)
# this is main game function that take only one argument as players list(array)
# It change global rank so we can assign winner respective rank and main can be able stop the code
# It follow the rule that any player only start game when he has a first dice of 1.
# and if he not get then he get additional 2 more chance in every round
# there is not any special chances
# after getting first 1 game move on and at every move we change players list prespective value
# by the snakes and ladders dictonary is calculate ladder up or snakes down
def game(players):
    '''
    # this is main game function that take only one argument as players list(array)
    # It change global rank so we can assign winner respective rank and main can be able stop the code
    # It follow the rule that any player only start game when he has a first dice of 1.
    # and if he not get then he get additional 2 more chance in every round
    # there is not any special chances
    # after getting first 1 game move on and at every move we change players list prespective value
    # by the snakes and ladders dictonary is calculate ladder up or snakes down
    '''
    for i in range(len(players)):
        global rank
        for j in range(len(players)):
            print(f"Player {j+1} is at Point {players[j]}")
        if players[i] < 100:
            print(f"Its Player {i+1} chance.")
        if players[i] == 0: # means player have not given their TOKEN now
            for j in range(1,4):
                input(f"Player {i+1} press Enter!")
                point = randint(1,6)
                print(f"Player {i+1} get {point}\n")
                if point == 1:
                    draw_me(i,point,players)
                    break
                else:
                    if j < 3:
                        print(f"Player {i+1} get another chance.\n")
        elif(players[i] > 0 and players[i] < 100): # means they are playing and not win yet!
            input(f"Player {i+1} press Enter!") # it is for just confirmation of player
            point = randint(1,6)
            print(f"Player {i+1} get {point}")
            prev = players[i]
            next = prev+point
            if next > 100: # when we get more than we need to go to the finish line
                print(f"Player {i+1} get invalid spin.")
                continue
            draw_me(i,next,players)
            if next == 100: # when player have won the match 
                print(f"Player {i+1} won and get RANK {rank}")
                rank += 1
                continue  # we can not use break here because is just skip others chances also when someone wins.
            # for ladders and snakes
            for start, end in ladders.items():
                if(next == start):
                    players[i] = end-1
                    draw_me(i,end,players)
                    print(f"Wow Player {i+1} get Ladder from {start} to {end}")
            for start, end in snakes.items():
                if(next == start):
                    players[i] = end-1
                    draw_me(i,end,players)
                    print(f"Ohh Snake got Player {i+1} from {start} to {end}")
            

def main():
    '''
    # this is driver function and input for how many players are playing
    # create palyers list of the size of no_of_players
    and run while loop until 
    '''
    no_of_players = int(input("Enter the no of players : "))
    players = [0]*no_of_players
    while(rank <= no_of_players):
        game(players)
        

if __name__ == "__main__":
    main()
