import sys 
from pathlib import Path
from PySide2.QtWidgets import QFileDialog,QPushButton, QGridLayout, QApplication ,QListWidget, QListView, QLabel, QWidget, QAbstractItemView, QSplitter, QComboBox, QTextEdit, QHBoxLayout, QMessageBox
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide2 import QtCore

class customDesigner(QWidget):
    def __init__(self):
        super().__init__()

        self.fileName = None
        self.filters = "Text files (*.txt)"
        self.customList = QComboBox()
        self.customList.addItems(["Layer","Loss Function","Optimizer"])
        self.customList.currentIndexChanged[int].connect(self.editorText)

        self.newButton = QPushButton("New")
        self.newButton.clicked.connect(self.newAction)

        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(self.saveAction)

        self.openButton = QPushButton("Open")
        self.openButton.clicked.connect(self.openAction)
        self.init_GUI()
        self.set_styling()

    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.hbox = QHBoxLayout()
        self.TextEditor = QTextEdit()
        self.TextEditor.setText("class customLayer(Layer):\n\tpass")
        self.hbox.addWidget(self.customList)
        self.hbox.addWidget(self.newButton)
        self.hbox.addWidget(self.saveButton)
        self.hbox.addWidget(self.openButton)
        self.main_layout.addLayout(self.hbox,0,0)
        self.main_layout.addWidget(self.TextEditor,1,0)
        self.setLayout(self.main_layout)
        self.set_styling()

    
    def newAction(self):
        response = self.msgApp("Confirmation","Do you like to save the current file?")
        if response == "Y":
            self.saveAction()
        print(self.customList.currentIndex)
        self.editorText(self.customList.currentIndex())

    def saveAction(self):
        if self.fileName == None or self.fileName == '':
            self.fileName, self.filterName = QFileDialog.getSaveFileName(self, filter=self.filters)
        if(self.fileName != ''):
            file = open(self.fileName, 'w')
            file.write(self.TextEditor.toPlainText())

    def openAction(self):
        response = self.msgApp("Confirmation","Do you like to save the current file?")
        if response == "Y":
            self.saveAction()

        self.fileName, self.filterName = QFileDialog.getOpenFileName(self)
        self.TextEditor.setText(open(self.fileName).read())

    def msgApp(self,title,msg):
        userInfo = QMessageBox.question(self,title,msg,QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return "Y"
        if userInfo == QMessageBox.No:
            return "N"
        self.close()

    def editorText(self,index):
        if(index == 0):
            self.TextEditor.setText("class customLayer(Layer):\n\tpass")
        if(index == 1):
            self.TextEditor.setText("class customLossFunction():\n\tpass")
        if(index == 2):
            self.TextEditor.setText("class customOptimizer():\n\tpass")

    def set_styling(self):
        pass
