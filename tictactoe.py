# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:46:21 2020

@author: hp
"""


import itertools
from colorama import Fore,Back,Style, init
init()

def win(current_game):
    
    def compare_all(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
        
    # horizontal
    for row in game:
        print(row)
        if compare_all(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True
    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if compare_all(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if compare_all(diags):
        print(f"Player {diags[0]} has won Diagonally (/)")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if compare_all(diags):
        print(f"Player {diags[0]} has won Diagonally (\\)")
        return True

    return False

#game Board
def game_board(game_map,player=0, row =0, column=0, just_display=False):
    try:      
        if game_map[row][column]!=0:
            print("position occupied, Choose another!")
            return game_map,False
        if not just_display:
            game_map[row][column]=player
        print("   0  1  2")
        for count,row in enumerate(game_map):
            colored_row= ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.BLUE + ' O ' + Style.RESET_ALL
            print(count,colored_row)
        return game_map,True
    
    except IndexError as e:
        print("Enter Row and Column values between 0 to 2",e)
        return game_map,False
    
    except Exception as e:
        print("Something went wrong",e)
        return game_map,False
#win(game)
        
play = True
players = [1,2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    
    game_won= False
    game,_ = game_board(game,just_display=True)
    player_choice= itertools.cycle([1,2])
    while not game_won:
        current_player=next(player_choice)
        print(f"Current Player:{current_player}")
        played = False
        
        while not played:
            column_choice= int(input("enter column number(0,1,2):"))
            row_choice = int(input("enter row number(0,1,2):"))
            game,played= game_board(game, current_player,row_choice,column_choice)
            
        if win(game):
            game_won=True
            again= input("Game Over!, Would you like to play again?(y/n):")
            if again.lower()=="y":
                print("restarting")
            elif again.lower()=="n":
                print("Game end")
                play=False
            else:
                print("Not a valid answer, see you later!")
                play= False
                
