'''
@File    :   Logic.py
@Time    :   09.05.2023 19:19:59
@Author  :   Karri Korsu 
@Version :   1.0
@Contact :   karri.korsu@edu.turkuamk.fi
@Desc    :   Logic class to store the game logic. 
'''

class Logic:
    og_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    def __init__(self):
        self.win = False
        self.matrix = [[0,1,2],[3,4,5],[6,7,8]]#[[0,0,0],[0,0,0],[0,0,0]]

    '''
    error checked for empty value in matrix
    '''
    def ec_selection(self, x, y):
        if self.matrix[x][y] != 0:
            yield print('You cant add a value there')
            return False
        else:
            return True
    
    '''
    Actual selection function which changes or doesn't change the value of matrix.
    Listens to UI.
    '''
    def selection(self, input, x, y):
        if self.ec_selection(x,y):
            self.matrix[x][y] = input
    
    '''
    Checks all possible outcomes where a user wins.
    '''
    def check_win(self, matrix, me):
        # rows
        for item in matrix:
            if item == [me,me,me]:
                self.win = True
        # columns    
        for i in range(len(matrix)):
            if matrix[i][0] != me:
                break
            elif i == len(matrix):
                self.win == True
        # nw - se
        if matrix[0][0] == me and matrix[1][1] == me and matrix[2][2] == me:
            self.win = True
        # ne - sw
        if matrix[2][0] == me and matrix[1][1] == me and matrix[0][2] == me:
            self.win = True

        return self.win

    '''
    Restart function which sets the matrix to original standing and sets self.win=False
    '''            
    def restart(self):
        self.matrix = Logic.og_matrix
        self.win = False
                    