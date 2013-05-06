Title: Tetris
Contributors: dkindel, taylorm17, mxj, brianmay27
Type: game
Description: A GUI based Tetris Game
repo: https://github.com/dkindel/2524tetris.git

To install tkinter (required for running this application), run 

    sudo apt-get install python-tk

Run the Application by running
    
    ./Controller.py

in the directory containing "Controller.py", "Matrix.py", and "Shape.py".  If the Application fails to run, in 'Controller.py', replace 

    from Tkinter import *

with 

    from tkinter import *

in line 7 (notice the capitilization on Tkinter).  The change is due to changes from python 2 to python 3. 
