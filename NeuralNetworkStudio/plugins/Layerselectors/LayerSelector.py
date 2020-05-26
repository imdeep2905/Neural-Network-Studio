'''
TODO 
# Set appropiate Styling
# Fix paths
'''
import os
import sys 
from pathlib import Path
from PySide2.QtWidgets import QPushButton, QVBoxLayout, QApplication ,QListWidget,QScrollArea, QListView, QLabel, QWidget, QAbstractItemView, QSplitter 
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon, Qt, QDrag
from PySide2 import QtCore
from PySide2 import QtGui

PATH = os.path.join('.','img_src')
print('LayerSelector Loaded with path:' , PATH)
        
class LayersList(QWidget):
    '''
    LayerList class which acts as collapsable list.
    '''
    def __init__(self, name, layers, expand = True):
        super().__init__()
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.currently_expanded = True
        self.main_layout = QVBoxLayout()
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.expand_button = QPushButton(name)
        self.expand_button.setToolTip(f"List of {name} Layers")
        self.expand_button.setIcon(QIcon(os.path.join(PATH,'LayersList_Up.png')))
        
        self.layer_list = QListView()
        self.layer_list.setDragEnabled(True)
        self.layer_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.layer_list.setWrapping(False)
        self.layer_list.setViewMode(self.layer_list.ListMode)
        self.layer_list.setResizeMode(self.layer_list.Fixed)
        
        self.container_model = QStandardItemModel()
        for l in layers:
            self.container_model.appendRow(QStandardItem(QIcon(os.path.join(PATH,'LayersList_Layer_Icon.png')),l))
        
        self.layer_list.setModel(self.container_model)
        self.layer_list.setMaximumSize(self.get_container_sizes())
        self.layer_list.setMinimumSize(self.get_container_sizes())
        
        self.main_layout.addWidget(self.expand_button,0, Qt.AlignTop)
        self.main_layout.addWidget(self.layer_list, 0, Qt.AlignTop)
        self.expand_button.clicked.connect(self.expand)
        
        self.setLayout(self.main_layout)
        self.resized_size = self.layer_list.maximumHeight()
        
        self.set_styling()
        
        if not expand:
            self.expand()
            
    @QtCore.Slot()
    def expand(self):
        if self.currently_expanded:
            self.currently_expanded = False
            self.expand_button.setIcon(QIcon(os.path.join(PATH,'LayersList_Down.png')))
            self.layer_list.setMaximumHeight(0)
        else:
            self.currently_expanded = True
            self.expand_button.setIcon(QIcon(os.path.join(PATH,'LayersList_Up.png')))
            self.layer_list.setMinimumHeight(self.resized_size)
            
    def get_container_sizes(self):
        w, h = 0, 0
        for i in range(self.container_model.columnCount()):
            pass
            #w += self.container_model.takeColumn(i) 
        for i in range(self.container_model.rowCount()):
            for r in self.container_model.takeRow(i):
                h += r.sizeHint().height()
        return QtCore.QSize(w, h)
    
    def set_styling(self):
        self.setStyleSheet("background-color:white;")
        self.expand_button.setStyleSheet("background-color:lightgrey;text-align:left;")

class LayersSelectorWidget(QWidget):
    '''
    LayerChoiceWidget class provide widget plugin for picking layers.
    '''
    def __init__(self):
        super().__init__()
        names = ['Core Layers',
                 'Convolution Layers',
                 'Pooling Layers',
                 'Recurrent Layers',
                 'Preprocessing Layers',
                 'Attention Layers',
                 'Reshaping Layers',
                 'Locally-Connected Layers'
                 ]
        layers = [
            ['Dense', 'Activation', 'Embedding', 'Masking', 'Lambda'],
            ['Conv1D', 'Conv2D', 'Conv3D', 'SeparableConv1D', 'SeparableConv2D', 'DepthwiseConv2D', 'Conv2DTranspose', 'Conv3Dtranspose'],
            ['MaxPooling1D', 'MaxPooling2D', 'MaxPooling3D', 'AveragePooling1D', 'AveragePooling2D', 'AveragePooling3D', 'GlobalMaxPooling1D', 'GlobalMaxPooling2D', 'GlobalMaxPooling3D', 'GlobalAveragePooling1D', 'GlobalAveragePooling2D', 'GlobalAveragePooling3D'],
            ['LSTM', 'GRU', 'SimpleRNN', 'TimeDistributed', 'BiDirectional', 'ConvLSTM2D'],
            ['TextToVector', 'Normalization'],
            ['Attention', 'AdditiveAttention'],
            ['Reshape', 'Flatten', 'Cropping1D', 'Cropping2D', 'Cropping3D', 'UpSampling1D', 'UpSampling2D', 'UpSampling3D', 'ZeroPadding1D', 'ZeroPadding2D', 'ZeroPadding3D'],
            ['LocallyConnected1D', 'LocallyConnected2D']
        ]
        self.main_layout = QVBoxLayout()
        for i in range(len(names)):
            if i > 3:
                self.main_layout.addWidget(LayersList(names[i], layers[i], False))
            else:
                self.main_layout.addWidget(LayersList(names[i], layers[i]))                
        self.main_layout.setSpacing(0)
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area = QScrollArea()
        names = QWidget()
        names.setLayout(self.main_layout)
        self.scroll_area.setWidget(names)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setMargin(0)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setAlignment(Qt.AlignTop)
        self.scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_area)
        self.setLayout(self.main_layout)
        del(names)
        del(layers)
        
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")