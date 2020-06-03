#!/usr/bin/env python
# coding=utf-8
from IPython.display import clear_output
import sys
import random

def display_board(board):
    clear_output()
    print('   |   |   ')
    print(' '+board[6]+' | '+board[7]+' | '+board[8])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' '+board[3]+' | '+board[4]+' | '+board[5])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' '+board[0]+' | '+board[1]+' | '+board[2])
    print('   |   |   ')
    print('------------')

    pass

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
      if sys.version_info >= (3, 0):
          marker = input('Player1, você quer ser X ou O?').upper()
      else:
          marker = raw_input('Player1, você quer ser X ou O?').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (
        (board[6] == mark and board[7] == mark and board[8] == mark) or #vitória pelo topo
        (board[3] == mark and board[4] == mark and board[5] == mark) or #vitória pelo meio
        (board[0] == mark and board[1] == mark and board[2] == mark) or #vitória pelo baixo
        (board[6] == mark and board[3] == mark and board[0] == mark) or #vitória pelo esquerda
        (board[7] == mark and board[4] == mark and board[1] == mark) or #vitória pelo meio
        (board[8] == mark and board[5] == mark and board[2] == mark) or #vitória pelo direita
        (board[6] == mark and board[4] == mark and board[2] == mark) or #vitória pelo diagonal
        (board[8] == mark and board[4] == mark and board[0] == mark) #vitória pelo diagonal
    )

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    #print("'%i'->'%s'"%(position,board))
    return (board[position] == ' ')

def full_board_check(board):
    for i in range(0,9):
        if space_check(board,i):
            return False

    return True

def player_choise(board):
    position = ' '
    posn = -1
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, posn):
        if sys.version_info >= (3, 0):
            position = input('Escolha a sua jogada (1 a 9):')
        else:
            position = raw_input('Escolha a sua jogada (1 a 9):')
        posn = (int(position) - 1)
    return posn

def replay():
    if sys.version_info >= (3, 0):
        return input('Quer jogar novamente? "SIM" ou "NAO"').lower().startswith('s')
    else:
        return raw_input('Quer jogar novamente? "SIM" ou "NAO"').lower().startswith('s')

#---------------------------------------------------------------------

print("\n%s\nBeiriz - v1.1 - 02/06/2020\nBem vindo ao jogo da velha!\n%s\nPosições:" % ('#'*60,'#'*60))
display_board(["1","2","3","4","5","6","7","8","9"])

while True:
    #Defina o jogo
    board = [' '] * 9

    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print("%s começa!" % turn)

    game_on = True
    while game_on:
        #Vez do jogador1
        if turn == 'Player 1':
            display_board(board)
            print("%s(%s):" % (turn,player1_marker))
            position = player_choise(board)
            place_marker(board,player1_marker,position)
        #Checa a vitória do player1
        if win_check(board, player1_marker):
            display_board(board)
            print("Parabéns, %s venceu!" % turn)
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print("Empate!")
                break
            else:
                turn = "Player 2"
        #Vez do jogador2
        if turn == 'Player 2':
            display_board(board)
            print("%s(%s):" % (turn, player2_marker))
            position = player_choise(board)
            place_marker(board,player2_marker,position)
        #Checa a vitória do player2
        if win_check(board, player2_marker):
            display_board(board)
            print("Parabéns, %s venceu!" % turn)
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print("Empate!")
                break
            else:
                turn = "Player 1"

    if not replay():
        break
print("Fim!")