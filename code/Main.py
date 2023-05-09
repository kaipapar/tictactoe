'''
@File    :   Main.py
@Time    :   09.05.2023 19:19:48
@Author  :   Karri Korsu 
@Version :   1.0
@Contact :   karri.korsu@edu.turkuamk.fi
@Desc    :   None
'''

import tkinter as tk
from UI import UI

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x500')
    root.title('tictactoe')
    app = UI(root)
    root.mainloop()