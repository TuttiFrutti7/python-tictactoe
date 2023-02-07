import random       #for random bot choice

board = [{1: "-", 2: "-", 3: "-"}, {1: "-", 2: "-", 3: "-"}, {1: "-", 2: "-", 3: "-"}]

class Game():

    def display(self):  #displays the board
        print()
        for i in board:
            print(" ".join([i[j] for j in i]))
        print()

    def turn(self, you, bot):   #turn and move for each player
        player_now = you
        while self.check_winner() is not True:
            if(player_now == you):      #changes player
                player_now = bot
            else:
                player_now = you

            if(player_now == you):
                first_try = True
                while int(int(choice[0])-1) > 2 or int(choice[1]) > 3 or board[int(choice[0])-1][int(choice[1])] == "O"\
                or board[int(choice[0])-1][int(choice[1])] == "X" or first_try == True:
                    choice = input("Which field will you choose (column,row: 1-3) ? ")      #player choice
                    choice = [x.strip() for x in choice.split(",")]
                    first_try = False
                board[int(choice[0])-1][int(choice[1])] = "X"       #set choice on field

            elif(player_now == bot):
                choice = [random.randint(1,3) for i in range(2)]       #random choice for bot
                while board[int(choice[0])-1][int(choice[1])] == "O" or board[int(choice[0])-1][int(choice[1])] == "X":
                    choice = [random.randint(1,3) for i in range(2)]
                    if board[int(choice[0])-1][int(choice[1])] != "O" and board[int(choice[0])-1][int(choice[1])] != "X":
                        break       #make list "choice" empty wrong choices or add the correct choices to a list containing correct values
                board[choice[0]-1][choice[1]] = "O"     #set choice on field
                print("Bot has made his move")

            self.display()      #displays table after each players turn

    def check_winner(self):        #checks for winner
        values_list = ["X", "O"]
        for value in values_list:        #???ONLY CHECKS FIRST ITEM OF VALUES LIST FOR UNKNOWN REASON  OR  CHECKS FOR BOTH BUT GAME ENDS???
            
            if value == "X":
                winner = "You have won!"
            else:
                winner = "Bot has won!"

            for row in range(0,3):
                if board[row][1] == value and board[row][2] == value and board[row][3] == value:
                    print(winner)
                    return True
            for column in range(1,4):
                if board[0][column] == value and board[1][column] == value and board[2][column] == value:
                    print(winner)
                    return True
            if board[0][1] == value and board[1][2] == value and board[2][3] == value:
                print(winner)
                return True
            elif board[0][3] == value and board[1][2] == value and board[2][1] == value:
                print(winner)
                return True

    def game(self):   #main game function
        print("The game has started!")
        self.turn("you", "bot")
        print("Thanks for playing!")

Go = Game()
Go.game()