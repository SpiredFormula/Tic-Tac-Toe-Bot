import discord
from discord.ext import commands
from discord.ext.commands import context

GameStarted = False
P1canmove = False
P2canmove = False

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
board_num = "null"
print("",board[0], "|", board[1], "|", board[2],"\n",
board[3], "|", board[4], "|", board[5],"\n",
board[6], "|", board[7], "|", board[8])

#winning conditions
row1 = f'{board[0]} {board[1]} {board[2]}'
row2 = f'{board[3]} {board[4]} {board[5]}'
row3 = f'{board[6]} {board[7]} {board[8]}'

collum1 = f'{board[0]} {board[3]} {board[6]}'
collum2 = f'{board[1]} {board[4]} {board[7]}'
collum3 = f'{board[2]} {board[5]} {board[8]}'

diagonal1 = f'{board[0]} {board[4]} {board[8]}'
diagonal2 = f'{board[2]} {board[4]} {board[6]}'

print(f"{row1}|{row2}|{row3}")
print(f"{collum1}|{collum2}|{collum3}")
print(f"{diagonal1}|{diagonal2}")
TOKEN = "Token goes here"



client = commands.Bot(command_prefix= "!")

#When the bot is online it will display a message
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

    #Debug
    print(P1canmove, P2canmove)


#Command to start the game
@client.command()
async def play(ctx, * ,message):

    
    #Global values
    global GameStarted
    global P1canmove
    global P2canmove


    #Tells everyone when a game has started and what the game is called
    print(f"Someone has started a game called : {message}")
    await ctx.send(f"A New game has started called: {message}")
    await ctx.send("Player 1: Please make a move by typing !p1 (where you will place it)")
    
    await ctx.send("1  |  2  |  3""\n""4  |  5  |  6""\n""7  |  8  |  9")

    GameStarted = True
    P1canmove = True

    return GameStarted, P1canmove


#Command to allow player one make a move
@client.command()
async def p1(ctx, *, space):
    #global values
    global GameStarted
    global P1canmove
    global P2canmove
    global board
    global board_num
    global row1
    global row2
    global row3
    global collum1
    global collum2
    global collum3
    global diagonal1
    global diagonal2
    #debug
    print(P1canmove, P2canmove)
    print(board)

    #check if it is player one's turn
    if GameStarted == True and P1canmove == True:

        P2canmove = True
        P1canmove = False
        board_num = int(space) - 1

        #check what space they selected
        if space == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            if board[board_num] == "-":
                await ctx.send(f"placed in space {space}")
                board[board_num] = "o"

                print("",board[0], "|", board[1], "|", board[2],"\n",
                board[3], "|", board[4], "|", board[5],"\n",
                board[6], "|", board[7], "|", board[8])

                await ctx.send(f'{board[0]} | {board[1]} | {board[2]}''\n'f'{board[3]} | {board[4]} | {board[5]}''\n'f'{board[6]} | {board[7]} | {board[8]}')

                board_num = "null"


                row1 = f'{board[0]} {board[1]} {board[2]}'
                row2 = f'{board[3]} {board[4]} {board[5]}'
                row3 = f'{board[6]} {board[7]} {board[8]}'

                collum1 = f'{board[0]} {board[3]} {board[6]}'
                collum2 = f'{board[1]} {board[4]} {board[7]}'
                collum3 = f'{board[2]} {board[5]} {board[8]}'

                diagonal1 = f'{board[0]} {board[4]} {board[8]}'
                diagonal2 = f'{board[2]} {board[4]} {board[6]}'
                
                #debug
                print(f"{row1}|{row2}|{row3}")
                print(f"{collum1}|{collum2}|{collum3}")
                print(f"{diagonal1}|{diagonal2}")

                if row1 == 'o o o' or row2 == 'o o o' or row3 == 'o o o' or collum1 == 'o o o' or collum2 == 'o o o' or collum3 == 'o o o' or diagonal1 == 'o o o' or diagonal2 == 'o o o':
                    print("win")
                    board = ["-","-","-",
                             "-","-","-",
                             "-","-","-",]
                    GameStarted = False
                    P1canmove = False
                    P2canmove = False
                    await ctx.send("PLAYER ONE WINS!!!!!!!")
                    return P2canmove, P1canmove, board, board_num

                else:
                    #Check if it is not a tie
                    if  '-' in row1 or '-' in row2 or '-' in row3  or '-' in collum1  or '-' in collum2  or '-' in collum3  or '-' in diagonal1 or '-' in diagonal2:
                        print("no win :(")
                        return P2canmove, P1canmove, board, board_num
                    #check for tie
                    else:
                        board = ["-","-","-",
                                 "-","-","-",
                                 "-","-","-",]
                        GameStarted = False
                        P1canmove = False
                        P2canmove = False
                        print("TIE!")
                        await ctx.send("TIE!!!")
                        return P2canmove, P1canmove, board, board_num
            else:
                board_num = "null"
                print("already placed there")
                await ctx.send("already placed there!")
                P2canmove = False
                P1canmove = True
                return P1canmove, P2canmove, board_num
    #Check if it is player two's turn
    elif GameStarted == True and P2canmove == True:
        await ctx.send("It is player two's turn!!")
        return
    #Check if the game has not started
    elif GameStarted == False:
        await ctx.send("Please start a game by typing !play (the name of your game)")
        return
    
    else:
        await ctx.send("ERROR!!!")
        return


    return P2canmove, P1canmove, board



@client.command()
async def p2(ctx, *, space):
    #global values
    global GameStarted
    global P1canmove
    global P2canmove
    global board
    global board_num
    global row1
    global row2
    global row3
    global collum1
    global collum2
    global collum3
    global diagonal1
    global diagonal2

    #debug
    print(P1canmove, P2canmove)
    print(board)

    #check if it is player two's turn
    if GameStarted == True and P2canmove == True:

        P2canmove = False
        P1canmove = True
        board_num = int(space) - 1

        #check what space they selected
        if space == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            if board[board_num] == "-":
                await ctx.send(f"placed in space {space}")
                board[board_num] = "x"


                print("",board[0], "|", board[1], "|", board[2],"\n",
                board[3], "|", board[4], "|", board[5],"\n",
                board[6], "|", board[7], "|", board[8])

                await ctx.send(f'{board[0]} | {board[1]} | {board[2]}''\n'f'{board[3]} | {board[4]} | {board[5]}''\n'f'{board[6]} | {board[7]} | {board[8]}')

                row1 = f'{board[0]} {board[1]} {board[2]}'
                row2 = f'{board[3]} {board[4]} {board[5]}'
                row3 = f'{board[6]} {board[7]} {board[8]}'

                collum1 = f'{board[0]} {board[3]} {board[6]}'
                collum2 = f'{board[1]} {board[4]} {board[7]}'
                collum3 = f'{board[2]} {board[5]} {board[8]}'

                diagonal1 = f'{board[0]} {board[4]} {board[8]}'
                diagonal2 = f'{board[2]} {board[4]} {board[6]}'
                
                #debug
                print(f"{row1}|{row2}|{row3}")
                print(f"{collum1}|{collum2}|{collum3}")
                print(f"{diagonal1}|{diagonal2}")
                
                board_num = "null"
                if row1 == 'x x x' or row2 == 'x x x' or row3 == 'x x x' or collum1 == 'x x x' or collum2 == 'x x x' or collum3 == 'x x x' or diagonal1 == 'x x x' or diagonal2 == 'x x x':
                    print("win")

                    board = ["-","-","-",
                             "-","-","-",
                             "-","-","-",]
                    GameStarted = False
                    P1canmove = False
                    P2canmove = False
                    await ctx.send("PLAYER TWO WINS!!!!!!!")
                    return P2canmove, P1canmove, board, board_num

                else:
                    #Check if it is not a tie
                    if  '-' in row1 or '-' in row2 or '-' in row3  or '-' in collum1  or '-' in collum2  or '-' in collum3  or '-' in diagonal1 or '-' in diagonal2:
                        print("no win :(")
                        return P2canmove, P1canmove, board, board_num
                    #check for tie
                    else:
                        board = ["-","-","-",
                                 "-","-","-",
                                 "-","-","-",]
                        GameStarted = False
                        P1canmove = False
                        P2canmove = False
                        print("TIE!")
                        await ctx.send("TIE!!!")
                        return P2canmove, P1canmove, board, board_num
            else:
                board_num = "null"
                P2canmove = True
                P1canmove = False
                print("already placed there")
                await ctx.send("already placed there!")
                return P1canmove, P2canmove, board_num
                
    #Check if it is player one's turn
    elif GameStarted == True and P1canmove == True:
        await ctx.send("It is player one's turn!!")
        return
    #Check if the game has not started
    elif GameStarted == False:
        await ctx.send("Please start a game by typing !play (the name of your game)")
        return
    
    else:
        await ctx.send("ERROR!!!")
        return


    return P2canmove, P1canmove, board
    
# MADE BY: SpiredFormula

client.run(TOKEN)
