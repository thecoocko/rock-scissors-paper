import math


def game(player1,player2):
    values = [0,1,2]
    flag = True
    try:
        values.index(player1) 
        values.index(player2)
        while flag:
            
            if player1==player2:
                print("Draw")
                player1 = int(input('Player one: '))
                player2 = int(input('Player two: '))
            elif player1/player2==0:
                flag = False
                return f"Player 1 wins"
            elif player1/player2<1 and player1/player2 !=0:
                flag = False
                return f"Player 2 wins"
            elif player1/player2>1:
                flag = False
                return f"Player 1 wins"
            elif math.isinf(player1/player2):
                flag = False
                return f"Player 2 wins" 
    except Exception:
        print("Error")



if __name__=="__main__":
    p1 = int(input('Player one: '))
    p2 = int(input('Player two: '))
    print(game(p1,p2))