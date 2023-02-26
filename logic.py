from tkinter import *
import random

class grid:

    def __init__(self , n : int) -> None:
        self.g = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    # def start_game(self):
    #     self.add_two()

    def add_two(self):
        can = [] 
        for i in range(self.n):
            for j in range(self.n):
                if self.g[i][j] == 0:
                    can.append((i , j))
        if not can:
            return 
        a , b = random.choice(can)
        self.g[a][b] = 2

    def transpose(self):
        mat = []
        for i in range( self.n-1 , -1 , -1):
            ma = []
            for j in range(self.n):
                ma.append(self.g[j][i])
            mat.append(ma)

        for i in range(self.n):
            for j in range(self.n):
                self.g[i][j] = mat[i][j]

    def reverse(self):
        mat = []
        for i in range(self.n):
            ma = []
            for j in range(self.n):
                ma = [self.g[j][i]] + ma
            mat.append(ma)
            
        for i in range(self.n):
            for j in range(self.n):
                self.g[i][j] = mat[i][j]

    def com_right(self):
        mat = [[0 for _ in range(self.n)] for _ in range(self.n)]
        ch = False
        for i in range(self.n):
            pos = self.n-1
            for j in range(self.n-1 , -1 , -1):
                if self.g[i][j] != 0:
                    mat[i][pos] = self.g[i][j]
                    if pos != j:
                        ch = True
                    pos -= 1

        for i in range(self.n):
            for j in range(self.n):
                self.g[i][j] = mat[i][j]
        return ch

    def merge_r(self):
        changed = False
        for i in range(self.n):
            for j in range(self.n-2 ,-1 , -1 ):
                if self.g[i][j] != 0 and self.g[i][j] == self.g[i][j+1]:
                    self.g[i][j] = 0 
                    self.g[i][j+1] *= 2
                    changed = True
        return changed
                
    def merge_l(self):
        changed = False
        for i in range(self.n):
            for j in range(1 , self.n):
                if self.g[i][j] != 0 and self.g[i][j] == self.g[i][j-1]:
                    self.g[i][j] = 0
                    self.g[i][j-1] *= 2
                    changed = True
        return changed

    def com_left(self):
        mat = [[0 for _ in range(self.n)] for _ in range(self.n)]
        ch = False
        for i in range(self.n):
            pos = 0
            for j in range(self.n):
                if self.g[i][j] != 0:
                    mat[i][pos] = self.g[i][j]
                    if pos != j:
                        ch = True
                    pos += 1
        for i in range(self.n):
            for j in range(self.n):
                self.g[i][j] = mat[i][j]
        return ch

        
    def is_on(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.g[i][j] == 0:
                    return True , 'keep playing!'
                if self.g[i][j] >= 2048:
                    return False , 'U Won!'
        
        for i in range(self.n -1):
            for j in range(self.n-1):
                if self.g[i][j] == self.g[i][j+1] or self.g[i][j] == self.g[i+1][j]:
                    return True , 'keep playing!'
        
        for i in range(self.n-1):
            if self.g[self.n-1][i] == self.g[self.n-1][i+1] or self.g[i][self.n-1] == self.g[i+1][self.n-1]:
                return True , 'keep playing!'

        return False , 'U Lose!'


def valid1(n):
    if not n:
        return False , '?? '
    for i in n:
        if ord(i) not in range(48 , 58):
            return False , 'type in a number (form 2 to 20): '
    if int(n) < 2 or int(n) > 20 :
        return False , 'choose a number from 2 to 20: '
    return True, ''

    
