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
from Logic import Logic

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
        self.game = Logic()
        self.buttonlist = []

        self.bind('<Escape>', lambda e: self.__close())

        # Close button
        ttk.Button(self,
                   text='Close',
                   command=lambda e=None: self.__close(),
                   ).place(x=400,y=400)

        # Buttons for selecting a place where you mark your
        self.create_select_buttons()
        
        self.you_won()
    
    '''
    Functions for creating buttons
    '''
    def create_select_buttons(self):
        coord_y=100
        
        for i in range(len(self.game.matrix)):
            coord_x=100
            for j in range(len(self.game.matrix[0])):
                self.buttonlist.append(ttk.Button(self, text=f'{self.game.matrix[i][j]}', 
                           command=[Logic.selection(self.game,input=1,x=i,y=j), self.update_buttons()],
                           width=5
                           ).place(y=coord_y,x=coord_x))
                coord_x+=50
            coord_y+=30

    '''
    Renders an update button
    '''
    def update_buttons(self, ):
        for i in range(len(self.buttonlist)):
            
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