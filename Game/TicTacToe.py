from curses import BUTTON_SHIFT
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
w=600
btnW=w/3
h=600
btnH=h/3
btnX=0
btnY=0

def clikcFunc():
    print('x')
    
app=QApplication()

game=QWidget()
game.resize(w,h)
for setir in range(1,4):
 for sutun in range(1,4):
     btn=QPushButton('{setir}.{sutun}', game)
     btn.setGeometri(btnX,btnY, btnW,btnH)
     btn.setStyleSheet("background:lightgray")
     btn.clicked.connect(clikcFunc)
     btnX+=btnW
     btnX=0
     btnY+=btnH
    
game.show()

app.exec_()