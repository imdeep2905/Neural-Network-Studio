'''
TODO 
# Set appropiate Styling
# Fix paths
'''
from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QToolBar, QWidget
import sys
import os
from PySide2.QtGui import QIcon, QFont


PATH = os.path.join('.','img_src')
print('ToolBar Loaded with path:' , PATH)

class ToolBarWidget(QToolBar):
    '''
    ToolBar class Provides toolbar for window.
    '''
    def __init__(self):
        super().__init__()
        names = ['New Project',
        'Save project', 
        'Load Project', 
        'Custom', 
        'Start' ,
        'Reset',
        'Launch Data Preprocessor',
        'Fullscreen Mode',
        'Preferences',
        'Python Path',
        'Performance',
        'Help']
        icons = [os.path.join(PATH,'ToolBar_New'),
                 os.path.join(PATH,'ToolBar_Save'),
                 os.path.join(PATH,'ToolBar_Load'),
                 os.path.join(PATH,'ToolBar_Custom'),
                 os.path.join(PATH,'ToolBar_Start'),
                 os.path.join(PATH,'ToolBar_Reset'),
                 os.path.join(PATH,'ToolBar_Data'),
                 os.path.join(PATH,'ToolBar_Fullscreen'),
                 os.path.join(PATH,'ToolBar_Preferences'),
                 os.path.join(PATH,'ToolBar_Python'),
                 os.path.join(PATH,'ToolBar_Performance'),
                 os.path.join(PATH,'ToolBar_Help')]
        self.setMovable(False)
        for i in range(len(names)):
            self.addAction(QAction(QIcon(icons[i]), names[i], self))
        del(names)
        del(icons)
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")