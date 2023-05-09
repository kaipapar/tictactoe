Object oriented tic tac toe
classes: 
- UI: tkinter class for rendering the logic
  - functionality
    - tic tac toe matrix buttons
    - quit button
    - initialize frame and window
    - talks to the **Logic class**
      -  sends and accepts data 
      -  win / lose signal from Logic causes an **messagebox** to pop up
    
- Logic: holds game logic
  - functionality
    - initializes empty 3x3 matrix / 2d nested list
    - updates the game list according to the signal from the UI class
    - error checking for adding a value to the matrix, if theres a value in list where the update is wanted it doesn't go through
    - 
