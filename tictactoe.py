"""
Tic Tac Toe Player
"""
import copy
import math
from util import Node, StackFrontier, QueueFrontier

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    qntdO = 0
    qntdX = 0
    for i in board:
        for j in i:
            if j == X:
                qntdX = qntdX + 1
            elif j == O:
                qntdO = qntdO + 1
    if qntdX > qntdO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    jogadas = []
    for i in range(0,3):
        for j in range(0,3):  
            if board[i][j] == EMPTY:
                jogadas.append((i,j))
    return jogadas


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tabuleiro = copy.deepcopy(board)
    if tabuleiro[action[0]][action[1]] == EMPTY:
        tabuleiro[action[0]][action[1]] = player(board)
    return tabuleiro


def winner(board):
    """
    Returns the winner of the game, if there is one.
    falta a diagonal
    """
    qntdO = 0
    qntdX = 0
    qntdOh = 0
    qntdXh = 0

    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == X and qntdO == 0:
                qntdX = qntdX + 1           
            elif board[i][j] == O and qntdX == 0: 
                qntdO = qntdO + 1
            if board[j][i] == X and qntdOh == 0:
                qntdXh = qntdXh + 1           
            elif board[j][i] == O and qntdXh == 0:
                qntdOh = qntdOh + 1
        if qntdX == 3 or qntdXh == 3:
            return X
        elif qntdO == 3 or qntdOh == 3:
            return O
        else:
            qntdO = 0 
            qntdX = 0
            qntdOh = 0 
            qntdXh = 0

    for i in range(0,3):
        if board[i][i] == X and qntdO == 0:
            qntdX = qntdX + 1           
        elif board[i][i] == O and qntdX == 0:
            qntdO = qntdO + 1
        if board[i][2 - i] == X and qntdOh == 0:
            qntdXh = qntdXh + 1           
        elif board[i][2 - i] == O and qntdXh == 0:
            qntdOh = qntdOh + 1
    if qntdX == 3 or qntdXh == 3:
            return X
    elif qntdO == 3 or qntdOh == 3:
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    result = winner(board)
    if result == X or result == O:
        return True
    elif checkBoard(board) == True:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        result = winner(board)
        if result == X:
            return 1
        elif result == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    noOrigem = Node(board, None, player(board), None)
    print("Jogador inicial :", noOrigem.player)
    noFinal = ajudinha(noOrigem)
    print("Action: ", noFinal.value)
    return noFinal.action

def ajudinha(no):
    if terminal(no.board) == True:
        no.value = utility(no.board)
        return no
    jogadas = actions(no.board)
    for jogada in jogadas:  
        boardNew = result(no.board, jogada)
        noNovo = ajudinha(Node(boardNew, jogada, player(boardNew), no))
        if pruning(noNovo, no):
            return no
        no.setValueJogada(noNovo.value,no.player,jogada)
    return no


def pruning(noNovo, no):
    if (noNovo.value < no.value and no.player == X):
        return True
    elif (noNovo.value > no.value and no.player == O):
        return True
    else:
        return False


def checkBoard(board):
    """
    Returns True in case the board has no empty spots.
    """
    for i in range(0,3):
        for j in range(0,3):  
            if board[i][j] == EMPTY:
                return False
    return True
