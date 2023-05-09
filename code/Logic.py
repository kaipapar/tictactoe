'''
@File    :   Logic.py
@Time    :   09.05.2023 19:19:59
@Author  :   Karri Korsu 
@Version :   1.0
@Contact :   karri.korsu@edu.turkuamk.fi
@Desc    :   None
'''

class Logic:
    def __init__(self):
        self.win = False
        self.matrix = [[0,0,0][0,0,0][0,0,0]]

    def ec_selection(self, x, y):
        if self.matrix[x][y] != 0:
            yield print('You cant add a value there')
            return False
        else:
            return True
        
    def selection(self, input, x, y):
        if self.ec_selection(x,y):
            self.matrix[x][y] = input
    
    def check_win(self, matrix, me, other):
        while not self.win:
            '''
            match case structure
            '''