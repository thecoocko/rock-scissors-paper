def game(player1,player2):
    values = ['rock','paper','scissors']
    winner = ''
    flag = True
    while flag:
        if player1==values[0] and player2==values[1]:
            winner = f"{player2} wins"
            flag = False 
        elif player1==values[0] and player2==values[2]:
            winner = f"{player1} wins"
            flag = False 
        elif player1==values[1] and player2==values[0]:
            winner = f"{player2} wins"
            flag = False 
        elif player1==values[1] and player2==values[2]:
            winner = f"{player2} wins"
            flag = False 
        elif player1==values[2] and player2==values[0]:
            winner = f"{player2} wins"
            flag = False 
        elif player1==values[2] and player2==values[1]:
            winner = f"{player2} wins"
            flag = False 
    return winner



if __name__=="__main__":
    p1 = str(input('Player one: '))
    p2 = str(input('Player two: '))
    print(game(p1,p2))