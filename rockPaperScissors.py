def winCon(player1,player2):
    if (player1+1)%3==player2:
        return 1
    else:
        if(player1==player2):
            return 0
        else:
            return -1
while(True):
    print("======================\n+       MENU         +\n======================")
    choice =int(input("Select a choice\n1).Play\n2).Exit\n"))
    if(choice==2):
        break
    elif(choice==1):
        print("Choice menu:\n1 - Rock\n2 - Scissors\n3 - Paper\n")
        player1,player2 = input("Enter both player 1 and player 2's choices: ").split()
        player1 = int(player1)
        player2 = int(player2)
        winningStatus = winCon(player1-1,player2-1)
        if(not winningStatus):
            print("Draw")
        else:
            if(winningStatus == 1):
                print("Player 1 wins")
            else:
                print("Player 2 wins")
    else:
        print("Invalid choice")

