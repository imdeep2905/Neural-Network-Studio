from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QToolBar
import sys
from PySide2.QtGui import QIcon, QFont


class toolbar(QMainWindow):
    def __init__(self,names,icons):
        super(toolbar,self).__init__()

        self.setWindowTitle('Toolbar')
        self.setWindowIcon(QIcon('new.png'))
        self.createtoolbar()
        
        for i in range(len(names)):
            self.addaction(names[i],icons[i])

        

    def addaction(self,name,icon):
        action = QAction(QIcon(icon),name,self)
        self.toolBar.addAction(action)

    def createtoolbar(self):
        self.toolBar = self.addToolBar('tool')