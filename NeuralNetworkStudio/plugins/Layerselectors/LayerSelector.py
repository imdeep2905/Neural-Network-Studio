'''
TODO 
# Set appropiate Styling
# Fix paths
'''
import sys 
from pathlib import Path
from PySide2.QtWidgets import QPushButton, QVBoxLayout, QApplication ,QListWidget, QListView, QLabel, QWidget, QAbstractItemView, QSplitter 
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon, Qt
from PySide2 import QtCore

class LayersList(QWidget):
    '''
    LayerList class which acts as collapsable list.
    '''
    def __init__(self, name, layers):
        super().__init__()
        self.currently_expanded = True
        self.main_layout = QVBoxLayout()
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.expand_button = QPushButton(name)
        self.expand_button.setToolTip(f"List of {name} Layers")
        self.expand_button.setIcon(QIcon(str(Path('NeuralNetworkStudio/img_src/LayersList_Up.png'))))
        self.layer_list = QListView()
        self.container_model = QStandardItemModel()
        for l in layers:
            self.container_model.appendRow(QStandardItem(QIcon(str(Path('NeuralNetworkStudio/img_src/LayersList_Layer_Icon.png'))),l))
        self.layer_list.setDragEnabled(True)
        self.layer_list.setModel(self.container_model)
        self.layer_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.main_layout.addWidget(self.expand_button,0, Qt.AlignTop)
        self.main_layout.addWidget(self.layer_list, 0, Qt.AlignTop)
        self.expand_button.clicked.connect(self.expand)
        self.setLayout(self.main_layout)
        self.resized_size = 19 * len(layers)
        self.set_styling()
        
        
    @QtCore.Slot()
    def expand(self):
        if self.currently_expanded:
            self.layer_list.setMaximumHeight(0)
            self.expand_button.setIcon(QIcon(str(Path('NeuralNetworkStudio/img_src/LayersList_Down.png'))))
            self.currently_expanded = False
        else:
            self.layer_list.setMaximumHeight(self.resized_size)
            self.expand_button.setIcon(QIcon(str(Path('NeuralNetworkStudio/img_src/LayersList_Up.png'))))
            self.currently_expanded = True
            
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue ;")
        self.expand_button.setStyleSheet("text-align:left;")
        self.layer_list.setStyleSheet("background-color:aliceblue; border:1px solid;border-style: ridge;")

class LayersSelectorWidget(QWidget):
    '''
    LayerChoiceWidget class provide widget plugin for picking layers.
    '''
    def __init__(self, names, layers):
        super().__init__()
        self.main_layout = QVBoxLayout()
        for i in range(len(names)):
            self.main_layout.addWidget(LayersList(names[i], layers[i]))
        self.main_layout.setSpacing(0)
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue; border:0px solid;border-style: solid;")