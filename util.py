class Node():    
    def __init__(self, board, action, player, parent):
        self.board = board
        self.action = action
        self.parent = parent
        self.player = player
        self.value = self.valueDefaultDefiner()
    
    def valueDefaultDefiner(self):
        if self.player == 'X':
            return float('-inf')
        else:
            return float('inf')
    
    def setValue(self, value):
            self.value = value  
    
    def setValueJogada(self, value, player, action):
        if player == 'X' and self.value < value:
            self.action = action
            self.value = value
        elif player == 'O' and self.value > value:
            self.action = action
            self.value = value

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_board(self, board):
        return any(node.board == board for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    def printer(self):
        for node in self.frontier:
            print(node.board)

class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

