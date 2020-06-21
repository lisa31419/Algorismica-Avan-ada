import math
import random
import networkx as nx
import numpy as np
class NPuzzle:

    def create_board(self, n=3, solved=False):
        board = np.roll(np.arange(n*n),-1).reshape((n,n))
        if solved: return board
        for i in range(100):
            moves = self.allowed_moves(board)
            board = self.move(board, random.choice(moves))
        return board
    
    def allowed_moves(self, board):
        moves = []
        n = board.shape[0]
        # Find the 0 in the board
        posy, posx = np.where(board==0)
        posx, posy = posx[0], posy[0]
        if posx>0:moves.append('L')
        if posx<n-1:moves.append('R')
        if posy>0:moves.append('U')
        if posy<n-1:moves.append('D')
        return moves

    def move(self, bb, dd): #dd is the direction noted by: ['R','L','U','D']
        board = np.copy(bb)
        if not dd in self.allowed_moves(board): return board
        posy, posx = np.where(board==0)
        posx, posy = posx[0], posy[0]
        excx, excy = posx, posy
        if dd=='D': excy+=1
        elif dd=='U': excy-=1
        elif dd=='R': excx+=1
        elif dd=='L': excx-=1
        board[posy,posx] = board[excy,excx]
        board[excy,excx] = 0
        return board
    
    def rank(self, board):
        sol = np.roll(np.arange(board.shape[0]*board.shape[1]),-1)
        rr = board.ravel()
        return np.sum(sol!=rr)
    
    def get_state_id(self, board):
        return ''.join([str(x) for x in board.flatten()])
    
    def state(self, board):
        return self.rank(board)==0
    
    def print_board(self,board):
        nzeros = int(math.floor(math.log10(np.amax(board))))
        for i in board:
            print "+"+ ("-"*((board.shape[0]*(4+nzeros))-1)) +"+"
            print "|",
            for j in i:
                if j != 0:
                    diff = nzeros-int(math.floor(math.log10(j)))
                    print (" "*diff)+(str(j)+" |"),
                else:
                    print (" "*nzeros)+"  |",

            print ""
        print "+"+ ("-"*((board.shape[0]*(4+nzeros))-1))+"+"
    
    def manhattan_distance(self, board):
        sol = np.roll(np.arange(board.shape[0]*board.shape[1]),-1).reshape(board.shape)
        diff = 0
        for i in range(board.shape[0]*board.shape[1]):
            pos_sol = np.asarray(np.where(sol==i)).ravel()
            pos_board = np.asarray(np.where(board==i)).ravel()
            diff += np.sum(np.abs(pos_board-pos_sol))
        return diff
    
    def hamming_distance(self, board):
        sol = np.roll(np.arange(board.shape[0]*board.shape[1]),-1).reshape(board.shape)
        return np.sum(board!=sol)
    