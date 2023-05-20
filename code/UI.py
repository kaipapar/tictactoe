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
import os
'''
Handles the creation of button widgets

class CustomButtonWidget(ttk.Button):
    def __init__(self, parent, command, x, y, coordx, coordy):
        super().__init__(self, parent, x=coordx, y=coordy, command=command)
        self.command = '''
'''
Handles rendering game logic, 
Data flow: Logic <-> UI -> Main
'''
class UI(ttk.Frame):
    #class Tictactoe():

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
        self.og_button_dict
        '''
        # Buttons for selecting a place where you mark your.
        # Done like this to avoid stupid garbage collection
        self.button1 = ttk.Button(self, text=f'{self.game.matrix[0][0]}', width=5)
        self.button1.config(command=lambda e=1: self.click_button(btn=self.button1,x=0,y=0),)
        self.button1.place(y=100,x=100)

        self.button2 = ttk.Button(self, text=f'{self.game.matrix[0][1]}', width=5)
        self.button2.config(command=lambda e=1: self.click_button(btn=self.button2,x=0,y=1),)
        self.button2.place(y=100,x=150)

        self.button3 = ttk.Button(self, text=f'{self.game.matrix[0][2]}', width=5)
        self.button3.config(command=lambda e=1: self.click_button(btn=self.button3,x=0,y=2),)
        self.button3.place(y=100,x=200)

        self.button4 = ttk.Button(self, text=f'{self.game.matrix[1][0]}', width=5)
        self.button4.config(command=lambda e=1: self.click_button(btn=self.button4,x=1,y=0),)
        self.button4.place(y=130,x=100)

        self.button5 = ttk.Button(self, text=f'{self.game.matrix[1][1]}', width=5)
        self.button5.config(command=lambda e=1: self.click_button(btn=self.button5,x=1,y=1),)
        self.button5.place(y=130,x=150)

        self.button6 = ttk.Button(self, text=f'{self.game.matrix[1][2]}', width=5)
        self.button6.config(command=lambda e=1: self.click_button(btn=self.button6,x=1,y=2),)
        self.button6.place(y=130,x=200)

        self.button7 = ttk.Button(self, text=f'{self.game.matrix[2][0]}', width=5)                
        self.button7.config(command=lambda e=1: self.click_button(btn=self.button7,x=2,y=0),)
        self.button7.place(y=160,x=100)

        self.button8 = ttk.Button(self, text=f'{self.game.matrix[2][1]}', width=5)                          
        self.button8.config(command=lambda e=1: self.click_button(btn=self.button8,x=2,y=1),)
        self.button8.place(y=160,x=150)
        
        self.button9 = ttk.Button(self, text=f'{self.game.matrix[2][2]}', width=5)
        self.button9.config(command=lambda button=self.button9, e=1: self.click_button(btn=button, x=2, y=2),)
        self.button9.place(y=160, x=200)
        '''
        
        
    
    '''
    Functions for creating buttons
    '''
    @property
    def og_button_dict(self):
        print('49')
        self.button_dict = self.create_buttons()
        return self.button_dict
    
    #### FIXME: buttondict is local so it doesnt work properly.. garbage collection
    def create_buttons(self):
        coord_y=100
        buttondict = {}
        for i in range(len(self.game.matrix)):
            coord_x=100
            for j in range(len(self.game.matrix[0])):
                buttondict[f'[{i},{j}]'] = ttk.Button(self, text=f'{self.game.matrix[i][j]}', width=5)
                buttondict[f'[{i},{j}]'].config(command=lambda e=1: self.click_button(btn=buttondict[f'[{i},{j}]'],x=i,y=j))
                buttondict[f'[{i},{j}]'].place(y=coord_y,x=coord_x)
                print(f'[{i},{j}]')
                print(buttondict.keys())
                print(buttondict.values())
                coord_x+=50
            coord_y+=30
        return buttondict
    
    
    '''
    Gives necessary info to other functions when button is pressed
    '''
    def click_button(self, btn:tk.Button,x:int, y:int, input=1):
        self.game.selection(x,y)
        #self.update_button(x,y)
        btn.config(text= f'{input}')
        if self.game.check_win(self.game.matrix):
            self.you_won()


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
            #os.system('python3 code/Main.py')
            self.game.restart()
        else:
            #self.parent.destroy()
            self.__close()