from PySide2.QtWidgets import QWidget, QLabel, QGridLayout
from PySide2 import QtCore
#from NeuralNetworkStudio.plugins.LayerControllers.LayerControllers import *
from plugins.LayerControllers.LayerControllers import *
    
class LayerBoxWidget(QWidget):
    def __init__(self, name):
        super().__init__()
        self.control_widget = get_control_widget(name) 
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(QLabel(name), 0, 2)
        self.setLayout(self.main_layout)
        self.setGeometry(10, 10, 10, 10)
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
        
    def mouseDoubleClickEvent(self, event):
        print(event)
        
    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(LayerBoxWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(LayerBoxWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(LayerBoxWidget, self).mouseReleaseEvent(event)    
        
def get_control_widget(name):
    '''
    Get Layer control widget according to name of dropped layer
    '''
    if name == 'Dense':
        return DenseLayerControlWidget()
    elif name == 'Activation':
        return ActivationLayerControlWidget()
    elif name == 'Embedding':
        return EmbeddingLayerControlWidget()
    elif name == 'Masking':
        return MaskingLayerControlWidget()
    elif name == 'Lambda':
        return LambdaLayerControlWidget()
    elif name == 'Conv1D':
        return Conv1DLayerControlWidget()
    elif name == 'Conv2D':
        return Conv2DLayerControlWidget()
    elif name == 'Conv3D':
        return Conv3DLayerControlWidget()
    elif name == 'SeprableConv1D':
        return SeparableConv1DLayerControlWidget()
    elif name == 'SeprableConv2D':
        return SeparableConv2DLayerControlWidget()
    elif name == 'DepthwiseConv2D':
        return DepthwiseConv2DLayerControlWidget()
    elif name == 'Conv2DTranspose':
        return Conv2DTransposeLayerControlWidget()
    elif name == 'Conv3DTranspose':
        return Conv3DTransposeLayerControlWidget()
    elif name == 'MaxPooling1D':
        return MaxPooling1DLayerControlWidget()
    elif name == 'MaxPooling2D':
        return MaxPooling2DLayerControlWidget()
    elif name == 'MaxPooling3D':
        return MaxPooling3DLayerControlWidget()
    elif name == 'AveragePooling1D':
        return AveragePooling1DLayerControlWidget()
    elif name == 'AveragePooling2D':
        return AveragePooling2DLayerControlWidget()
    elif name == 'AveragePooling3D':
        return AveragePooling3DLayerControlWidget()
    elif name == 'GlobalMaxPooling1D':
        return GlobalMaxPooling1DLayerControlWidget()
    elif name == 'GlobalMaxPooling2D':
        return GlobalAveragePooling2DLayerControlWidget()
    elif name == 'GlobalMaxPooling3D':
        return GlobalMaxPooling3DLayerControlWidget()
    elif name == 'GlobalAveragePooling1D':
        return GlobalAveragePooling1DLayerControlWidget()
    elif name == 'GlobalAveragePooling2D':
        return GlobalAveragePooling2DLayerControlWidget()
    elif name == 'GlobalAveragePooling3D':
        return GlobalAveragePooling3DLayerControlWidget()
    elif name == 'LSTM':
        return LSTMLayerControlWidget()
    elif name == 'GRU':
        return GRULayerControlWidget()
    elif name == 'SimpleRNN':
        return SimpleRNNLayerWidget()
    elif name == 'TimeDistributed':
        return None #Not yet implemented
    elif name == 'BiDirectional':
        return None #^
    elif name == 'ConvLSTM2D':
        return ConvLSTM2DLayerControlWidget()
    elif name == 'TextToVector':
        return TextVectorizationLayerControlWidget()
    elif name == 'Normalization':
        return NormalizationLayerControlWidget()
    elif name == 'Attention':
        return AttentionLayerControlWidget()
    elif name == 'AdditiveAttention':
        return AdditiveAttentionLayerControlWidget()
    elif name == 'Reshape':
        return ReshapeLayerControlWidget()
    elif name == 'Flatten':
        return FlattenLayerControlWidget()
    elif name =='Cropping1D':
        return Cropping1DLayerControlWidget()
    elif name =='Cropping2D':
        return Cropping2DLayerControlWidget()
    elif name =='Cropping3D':
        return Cropping3DLayerControlWidget()
    elif name == 'UpSampling1D':
        return UpSampling1DLayerControlWidget()
    elif name == 'UpSampling2D':
        return UpSampling2DLayerControlWidget()
    elif name == 'UpSampling3D':
        return UpSampling3DLayerControlWidget()
    elif name == 'ZeroPadding1D':
        return ZeroPadding1DLayerControlWidget()
    elif name == 'ZeroPadding2D':
        return ZeroPadding2DLayerControlWidget()
    elif name == 'ZeroPadding3D':
        return ZeroPadding3DLayerControlWidget()
    elif name == 'LocallyConnected1D':
        return LocallyConnected1DLayerControlWidget()
    elif name == 'LocallyConnected2D':
        return LocallyConnected2DLayerControlWidget()
    else:
        '''
        Custom Layers
        '''
        return None