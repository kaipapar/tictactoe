'''
@File    :   UI.py
@Time    :   09.05.2023 19:19:42
@Author  :   Karri Korsu 
@Version :   1.0
@Contact :   karri.korsu@edu.turkuamk.fi
@Desc    :   None
'''


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Logic

'''
Handles rendering game logic, 
Data flow: Logic <-> UI -> Main
'''
class UI(ttk.Frame):
    def __init__(self, parent):
        # Initializing tkinter
        super().__init__(master=parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=1)
        self.game = Logic.Logic()
        self.button_dict = {}

        self.bind('<Escape>', lambda e: self.__close())

        # Close button
        ttk.Button(self,
                   text='Close',
                   command=lambda e=None: self.__close(),
                   ).place(x=400,y=400)

        # Buttons for selecting a place where you mark your
        #self.create_select_buttons()
        
        
        
    
    '''
    Functions for creating buttons
    '''
    
    @property
    def og_button_dict(self):
        coord_y=100
        
        for i in range(len(self.game.matrix)):
            coord_x=100
            for j in range(len(self.game.matrix[0])):
                self.button_dict[f'[{i},{j}]'] = ttk.Button(self, text=f'{self.game.matrix[i][j]}', 
                           command=lambda e=1: self.click_button(input=e,x=i,y=j),
                           width=5).place(y=coord_y,x=coord_x)
                coord_x+=50
            coord_y+=30
        return self.button_dict
    
    '''
    Gives necessary info to other functions when button is pressed
    '''
    def click_button(self, x:int, y:int, input=1):
        self.game.selection(input,x,y)
        self.update_button(x,y)
        if self.game.check_win(self.game.matrix):
            self.you_won()

    '''
    updates the text of a button to correct value and makes it so that the button no longer does anything
    '''
    def update_button(self, x, y):
        print(self.button_dict[f'[{x},{y}]'])#.config(text=f'{self.game.matrix[x][y]}', command=None)
        
    '''
    Function for terminating the program. Double underscore for fancy obfuscation reasons.
    '''
    def __close(self):
        if messagebox.askyesno('Close', 'Do you want to terminate the program?'):
            self.destroy()
            quit()
    
    '''
    Function for notifying user of winning
    '''
    def you_won(self):
        if messagebox.askretrycancel('You won!', 'Would you like to play again?'):
            self.game.restart()
        else:
            self.__close()