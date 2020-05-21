'''
TODO 
# Set appropiate Styling
# Fix paths
'''
from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QToolBar, QWidget
import sys
from PySide2.QtGui import QIcon, QFont


class ToolBarWidget(QToolBar):
    '''
    ToolBar class Provides toolbar for window.
    '''
    def __init__(self, names, icons):
        super().__init__()
        self.setMovable(False)
        for i in range(len(names)):
            self.addAction(QAction(QIcon(icons[i]), names[i], self))
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")