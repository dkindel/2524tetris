#Tetris

Contributors: dkindel, taylorm17, mxj, brianmay27

Not all the files are required to run our Tetris Application.  The only required files are "Controller.py", "Matrix.py", and "Shape.py".
The rest of the files are text documents and testing files.  Instructions on how to play are included in the game by clicking on the 
"Help" button in the main menu.

To install tkinter (required for running this application), run 

    sudo apt-get install python-tk

Run the Application by running
    
    ./Controller.py

in the directory containing "Controller.py", "Matrix.py", and "Shape.py".  If the Application fails to run, in 'Controller.py', replace 

    from Tkinter import *

with 

    from tkinter import *

in line 7 (notice the capitilization on Tkinter).  The change is due to changes from python 2 to python 3. 
