from calendar import setfirstweekday
from curses import BUTTON_SHIFT
from re import X
from tkinter.tix import Tree
from typing_extensions import Self
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
sutunSayi=3
setirSayi=3
w=600
btnW=sutunSayi
h=600
btnH=h/setirSayi
btnX=0
btnY=0

btnStatus=True


def clikcFunc():
    print('x')
    
app=QApplication()

game=QWidget()
game.resize(w,h)
class TicButton(QPushButton):
    def __init__(self,*args):
      QPushButton.__init__(self,*args)
      self.clicked.connect(self.clikcFunc)
      self.setStyleSheet("background:lightgray; font-size:25px")
      self.clickCount=0
      
    def clikcFunc(self):
     global btnStatus
     self.clickCount+=1
     if self.clickCount<=1:
      if btnStatus:
         self.setText('X')
         btnStatus=False
      else:
        self.setText('O')
        btnStatus=True
        
    print(self.clickCount)
       
for setir in range(1,setirSayi+1):
 for sutun in range(1,sutunSayi+1):
     btn=TicButton('', game)
     btn.setGeometri(btnX,btnY, btnW,btnH)
     btn.setStyleSheet("background:lightgray;")
    
     btnX+=btnW
     btnX=0
     btnY+=btnH
    
game.show()

app.exec_()