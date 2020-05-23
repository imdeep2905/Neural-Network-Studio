'''
TODO
# Add proper scaling, arrangement, styling
# optimize code
'''
from PySide2.QtCore import *
from PySide2.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QApplication, QLineEdit, QGridLayout, QLabel, QPushButton, QComboBox, QHBoxLayout, QStackedWidget,QStackedLayout,QStackedWidget,  QScrollBar, QScrollArea, QVBoxLayout, QFormLayout
from PySide2.QtGui import *
import sys
"""
Random uniform class provide UI of random Uniform

"""
######################## Core layers ############################### 
'''
DONE
'''
class DenseLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.neuron = QLineEdit("0")
        self.activation = QComboBox()
        self.activation.addItems([
            "sigmoid",
            "tanh",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])
        self.use_bias = QComboBox()
        self.use_bias.addItems(["True","False"])

        """
        Kernel Initializer

        """
        self.kernel_initializer = QComboBox()
        self.kernel_initializer.addItems([
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Orthogonal",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "glorot_uniform",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.kernel_initializer.currentIndexChanged[int].connect(lambda index: self.kernel_initializer_stack.setCurrentIndex(index))
    

        self.kernel_initializer_stack = QStackedWidget()
        self.kernel_initializer_stack.addWidget(RandomUniformUI())
        self.kernel_initializer_stack.addWidget(ZerosUI())
        self.kernel_initializer_stack.addWidget(OnesUI())
        self.kernel_initializer_stack.addWidget(ConstantUI())
        self.kernel_initializer_stack.addWidget(RandomNormalUI())
        self.kernel_initializer_stack.addWidget(TruncatedNormalUI())
        self.kernel_initializer_stack.addWidget(VarianceScalingUI())
        self.kernel_initializer_stack.addWidget(OrthogonalUI())
        self.kernel_initializer_stack.addWidget(IdentityUI())
        self.kernel_initializer_stack.addWidget(lecunUniformUI())
        self.kernel_initializer_stack.addWidget(glorotNormalUI())
        self.kernel_initializer_stack.addWidget(glorotUniformUI())
        self.kernel_initializer_stack.addWidget(heNormalUI())
        self.kernel_initializer_stack.addWidget(lecunNormalUI())
        self.kernel_initializer_stack.addWidget(heUniformUI())

        """
        Bias Initializer

        """
        self.bias_initializer = QComboBox()
        self.bias_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.bias_initializer.currentIndexChanged[int].connect(lambda index : self.bias_initializer_stack.setCurrentIndex(index))
        self.bias_initializer_stack = QStackedWidget()
        self.bias_initializer_stack.addWidget(RandomUniformUI())
        self.bias_initializer_stack.addWidget(ZerosUI())
        self.bias_initializer_stack.addWidget(OnesUI())
        self.bias_initializer_stack.addWidget(ConstantUI())
        self.bias_initializer_stack.addWidget(RandomNormalUI())
        self.bias_initializer_stack.addWidget(TruncatedNormalUI())
        self.bias_initializer_stack.addWidget(VarianceScalingUI())
        self.bias_initializer_stack.addWidget(OrthogonalUI())
        self.bias_initializer_stack.addWidget(IdentityUI())
        self.bias_initializer_stack.addWidget(lecunUniformUI())
        self.bias_initializer_stack.addWidget(glorotNormalUI())
        self.bias_initializer_stack.addWidget(glorotUniformUI())
        self.bias_initializer_stack.addWidget(heNormalUI())
        self.bias_initializer_stack.addWidget(lecunNormalUI())
        self.bias_initializer_stack.addWidget(heUniformUI())
        """
        Kernal regularizer
        """
        self.kernel_regularizer = QComboBox()
        self.kernel_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.kernel_regularizer.currentIndexChanged[int].connect(lambda index : self.kernel_regularizer_stack.setCurrentIndex(index))

        self.kernel_regularizer_stack = QStackedLayout()
        self.kernel_regularizer_stack.addWidget(QLabel("None"))
        self.kernel_regularizer_stack.addWidget(l1UI())
        self.kernel_regularizer_stack.addWidget(l2UI())
        self.kernel_regularizer_stack.addWidget(l1_l2UI())

        """
        Bias regularizer

        """

        self.bias_regularizer = QComboBox()
        self.bias_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.bias_regularizer.currentIndexChanged[int].connect(lambda index : self.bias_regularizer_stack.setCurrentIndex(index))

        self.bias_regularizer_stack = QStackedLayout()
        self.bias_regularizer_stack.addWidget(QLabel("None"))
        self.bias_regularizer_stack.addWidget(l1UI())
        self.bias_regularizer_stack.addWidget(l2UI())
        self.bias_regularizer_stack.addWidget(l1_l2UI())

        """
        activity_regularizer

        """
        self.activity_regularizer = QComboBox()
        self.activity_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.activity_regularizer.currentIndexChanged[int].connect(lambda index : self.activity_regularizer_stack.setCurrentIndex(index))

        self.activity_regularizer_stack = QStackedLayout()
        self.activity_regularizer_stack.addWidget(QLabel("None"))
        self.activity_regularizer_stack.addWidget(l1UI())
        self.activity_regularizer_stack.addWidget(l2UI())
        self.activity_regularizer_stack.addWidget(l1_l2UI())

        """
        kernel_constraint

        """
        self.kernel_constraint = QComboBox()
        self.kernel_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.kernel_constraint.currentIndexChanged[int].connect(lambda index : self.kernel_constraint_stack.setCurrentIndex(index))
        self.kernel_constraint_stack = QStackedWidget()
        self.kernel_constraint_stack.addWidget(QLabel("None"))
        self.kernel_constraint_stack.addWidget(MaxNormUI())
        self.kernel_constraint_stack.addWidget(NonNegUI())
        self.kernel_constraint_stack.addWidget(UnitNormUI())
        self.kernel_constraint_stack.addWidget(MinMaxNormUI())

        """
        bias_constraint

        """
        self.bias_constraint = QComboBox()
        self.bias_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.bias_constraint.currentIndexChanged[int].connect(lambda index : self.bias_constraint_stack.setCurrentIndex(index))
        self.bias_constraint_stack = QStackedWidget()
        #self.bias_constraint_stack.setAlignment(Qt.AlignTop)        
        #self.bias_constraint_stack.setSpacing(0)
        self.bias_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.bias_constraint_stack.addWidget(MaxNormUI())
        self.bias_constraint_stack.addWidget(NonNegUI())
        self.bias_constraint_stack.addWidget(UnitNormUI())
        self.bias_constraint_stack.addWidget(MinMaxNormUI())
        self.init_GUI()

    def init_GUI(self):
        """
        self.main_layout

        """
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(QLabel('Neurons:'),0,0)
        self.main_layout.addWidget(self.neuron,0,1)

        self.main_layout.addWidget(QLabel("Activation:"),1,0)
        self.main_layout.addWidget(self.activation,1,1)

        self.main_layout.addWidget(QLabel("Use Bias:"),2,0)
        self.main_layout.addWidget(self.use_bias,2,1)

        self.main_layout.addWidget(QLabel("kernelInitializer"),3,0)
        self.main_layout.addWidget(self.kernel_initializer,3,1)
        self.main_layout.addWidget(self.kernel_initializer_stack,4,1)

        self.main_layout.addWidget(QLabel("Bias Initializer"),5,0)
        self.main_layout.addWidget(self.bias_initializer,5,1)
        self.main_layout.addWidget(self.bias_initializer_stack,6,1)

        self.main_layout.addWidget(QLabel("kernel_regularizer"),7,0)
        self.main_layout.addWidget(self.kernel_regularizer,7,1)
        self.main_layout.addLayout(self.kernel_regularizer_stack,8,1)

        self.main_layout.addWidget(QLabel("bias_regularizer"),9,0)
        self.main_layout.addWidget(self.bias_regularizer,9,1)
        self.main_layout.addLayout(self.bias_regularizer_stack,10,1)

        self.main_layout.addWidget(QLabel("activity_regularizer"),11,0)
        self.main_layout.addWidget(self.activity_regularizer,11,1)
        self.main_layout.addLayout(self.activity_regularizer_stack,12,1)

        self.main_layout.addWidget(QLabel("kernel_constraint"),13,0)
        self.main_layout.addWidget(self.kernel_constraint,13,1)
        self.main_layout.addWidget(self.kernel_constraint_stack,14,1)

        self.main_layout.addWidget(QLabel("bias_constraint"),15,0)
        self.main_layout.addWidget(self.bias_constraint,15,1)
        self.main_layout.addWidget(self.bias_constraint_stack,16,1)
        self.setLayout(self.main_layout)        
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")

    def parse_arguments(self):
        '''
        Should be changed to parse arguments
        '''
        Units = int(self.neuron.text())
        print(self.activation.currentText())
        print(self.use_bias.currentText())
        print(self.kernel_initializer.currentText())

class ActivationLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.activation = QComboBox()
        self.activation.addItems([
            "sigmoid",
            "tanh",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("Activation:"))
        self.main_layout.addWidget(self.activation)
        self.setLayout(self.main_layout)
        self.set_styling()
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass    
    
class EmbeddingLayerControlWidget(QWidget):
    '''
    Need to figure out it's usage in our app.
    Because it can only be used as first Layer in network. 
    '''
    pass

class MaskingLayerControlWidget(QWidget):    
    def __init__(self):
        super().__init__()
        self.masking = QLineEdit("0.0")
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("Masking value:"))
        self.main_layout.addWidget(self.masking)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class LambdaLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        '''
        Impliment it when doing custom activation, layer, optimizer etc...
        Directly give text box to write function which will be wrapped to make layer
        '''
                
        
#############################################################################

######################## Convolution layers #################################   
'''
DONE
'''
class Conv1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.filters = QLineEdit("(0)")
        self.kernal_size = QLineEdit("(0)")
        self.strides = QLineEdit("1")
        self.padding = QComboBox()
        self.padding.addItems(["same", "valid", "casual"])
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_first", "channels_last"])
        self.dilation_rate = QLineEdit("0")
        self.activation = QComboBox()
        self.activation.addItems([
            "sigmoid",
            "tanh",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])
        self.use_bias = QComboBox()
        self.use_bias.addItems(["True","False"])

        """
        Kernel Initializer

        """
        self.kernel_initializer = QComboBox()
        self.kernel_initializer.addItems([
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Orthogonal",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "glorot_uniform",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.kernel_initializer.currentIndexChanged[int].connect(lambda index: self.kernel_initializer_stack.setCurrentIndex(index))
    

        self.kernel_initializer_stack = QStackedWidget()
        self.kernel_initializer_stack.addWidget(RandomUniformUI())
        self.kernel_initializer_stack.addWidget(ZerosUI())
        self.kernel_initializer_stack.addWidget(OnesUI())
        self.kernel_initializer_stack.addWidget(ConstantUI())
        self.kernel_initializer_stack.addWidget(RandomNormalUI())
        self.kernel_initializer_stack.addWidget(TruncatedNormalUI())
        self.kernel_initializer_stack.addWidget(VarianceScalingUI())
        self.kernel_initializer_stack.addWidget(OrthogonalUI())
        self.kernel_initializer_stack.addWidget(IdentityUI())
        self.kernel_initializer_stack.addWidget(lecunUniformUI())
        self.kernel_initializer_stack.addWidget(glorotNormalUI())
        self.kernel_initializer_stack.addWidget(glorotUniformUI())
        self.kernel_initializer_stack.addWidget(heNormalUI())
        self.kernel_initializer_stack.addWidget(lecunNormalUI())
        self.kernel_initializer_stack.addWidget(heUniformUI())

        """
        Bias Initializer

        """
        self.bias_initializer = QComboBox()
        self.bias_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.bias_initializer.currentIndexChanged[int].connect(lambda index : self.bias_initializer_stack.setCurrentIndex(index))
        self.bias_initializer_stack = QStackedWidget()
        self.bias_initializer_stack.addWidget(RandomUniformUI())
        self.bias_initializer_stack.addWidget(ZerosUI())
        self.bias_initializer_stack.addWidget(OnesUI())
        self.bias_initializer_stack.addWidget(ConstantUI())
        self.bias_initializer_stack.addWidget(RandomNormalUI())
        self.bias_initializer_stack.addWidget(TruncatedNormalUI())
        self.bias_initializer_stack.addWidget(VarianceScalingUI())
        self.bias_initializer_stack.addWidget(OrthogonalUI())
        self.bias_initializer_stack.addWidget(IdentityUI())
        self.bias_initializer_stack.addWidget(lecunUniformUI())
        self.bias_initializer_stack.addWidget(glorotNormalUI())
        self.bias_initializer_stack.addWidget(glorotUniformUI())
        self.bias_initializer_stack.addWidget(heNormalUI())
        self.bias_initializer_stack.addWidget(lecunNormalUI())
        self.bias_initializer_stack.addWidget(heUniformUI())
        """
        Kernal regularizer
        """
        self.kernel_regularizer = QComboBox()
        self.kernel_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.kernel_regularizer.currentIndexChanged[int].connect(lambda index : self.kernel_regularizer_stack.setCurrentIndex(index))

        self.kernel_regularizer_stack = QStackedLayout()
        self.kernel_regularizer_stack.addWidget(QLabel("None"))
        self.kernel_regularizer_stack.addWidget(l1UI())
        self.kernel_regularizer_stack.addWidget(l2UI())
        self.kernel_regularizer_stack.addWidget(l1_l2UI())

        """
        Bias regularizer

        """

        self.bias_regularizer = QComboBox()
        self.bias_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.bias_regularizer.currentIndexChanged[int].connect(lambda index : self.bias_regularizer_stack.setCurrentIndex(index))

        self.bias_regularizer_stack = QStackedLayout()
        self.bias_regularizer_stack.addWidget(QLabel("None"))
        self.bias_regularizer_stack.addWidget(l1UI())
        self.bias_regularizer_stack.addWidget(l2UI())
        self.bias_regularizer_stack.addWidget(l1_l2UI())

        """
        activity_regularizer

        """
        self.activity_regularizer = QComboBox()
        self.activity_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.activity_regularizer.currentIndexChanged[int].connect(lambda index : self.activity_regularizer_stack.setCurrentIndex(index))

        self.activity_regularizer_stack = QStackedLayout()
        self.activity_regularizer_stack.addWidget(QLabel("None"))
        self.activity_regularizer_stack.addWidget(l1UI())
        self.activity_regularizer_stack.addWidget(l2UI())
        self.activity_regularizer_stack.addWidget(l1_l2UI())

        """
        kernel_constraint

        """
        self.kernel_constraint = QComboBox()
        self.kernel_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.kernel_constraint.currentIndexChanged[int].connect(lambda index : self.kernel_constraint_stack.setCurrentIndex(index))
        self.kernel_constraint_stack = QStackedWidget()
        self.kernel_constraint_stack.addWidget(QLabel("None"))
        self.kernel_constraint_stack.addWidget(MaxNormUI())
        self.kernel_constraint_stack.addWidget(NonNegUI())
        self.kernel_constraint_stack.addWidget(UnitNormUI())
        self.kernel_constraint_stack.addWidget(MinMaxNormUI())

        """
        bias_constraint

        """
        self.bias_constraint = QComboBox()
        self.bias_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.bias_constraint.currentIndexChanged[int].connect(lambda index : self.bias_constraint_stack.setCurrentIndex(index))
        self.bias_constraint_stack = QStackedWidget()
        self.bias_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.bias_constraint_stack.addWidget(MaxNormUI())
        self.bias_constraint_stack.addWidget(NonNegUI())
        self.bias_constraint_stack.addWidget(UnitNormUI())
        self.bias_constraint_stack.addWidget(MinMaxNormUI())        
        self.init_GUI()
    
    def init_GUI(self):
        """
        Gearup main layout
        """
        self.main_layout.addWidget(QLabel("Filters:"), 0, 0)
        self.main_layout.addWidget(self.filters, 0 , 1)
        self.main_layout.addWidget(QLabel("Kernal Size:"), 1, 0)
        self.main_layout.addWidget(self.kernal_size, 1, 1)
        self.main_layout.addWidget(QLabel("Strides:"), 2, 0)
        self.main_layout.addWidget(self.strides, 2 ,1)
        self.main_layout.addWidget(QLabel("Padding:"), 3, 0)
        self.main_layout.addWidget(self.padding, 3, 1)
        self.main_layout.addWidget(QLabel("Data Format:"), 4, 0)
        self.main_layout.addWidget(self.data_format, 4 ,1)
        self.main_layout.addWidget(QLabel("Dilation rate:"), 5, 0)
        self.main_layout.addWidget(self.dilation_rate, 5, 1)
        self.main_layout.addWidget(QLabel("Activation"), 6, 0)
        self.main_layout.addWidget(self.activation, 6 ,1)
        self.main_layout.addWidget(QLabel("Use Bias:"), 7 , 0)
        self.main_layout.addWidget(self.use_bias, 7, 1)
        
        self.main_layout.addWidget(QLabel("kernelInitializer"),8,0)
        self.main_layout.addWidget(self.kernel_initializer,8,1)
        self.main_layout.addWidget(self.kernel_initializer_stack,9,1)

        self.main_layout.addWidget(QLabel("Bias Initializer"),9,0)
        self.main_layout.addWidget(self.bias_initializer,9,1)
        self.main_layout.addWidget(self.bias_initializer_stack,10,1)

        self.main_layout.addWidget(QLabel("kernel_regularizer"),11,0)
        self.main_layout.addWidget(self.kernel_regularizer,11,1)
        self.main_layout.addLayout(self.kernel_regularizer_stack,12,1)

        self.main_layout.addWidget(QLabel("bias_regularizer"),13,0)
        self.main_layout.addWidget(self.bias_regularizer,13,1)
        self.main_layout.addLayout(self.bias_regularizer_stack,14,1)

        self.main_layout.addWidget(QLabel("activity_regularizer"),15,0)
        self.main_layout.addWidget(self.activity_regularizer,15,1)
        self.main_layout.addLayout(self.activity_regularizer_stack,16,1)

        self.main_layout.addWidget(QLabel("kernel_constraint"),17,0)
        self.main_layout.addWidget(self.kernel_constraint,17,1)
        self.main_layout.addWidget(self.kernel_constraint_stack,18,1)

        self.main_layout.addWidget(QLabel("bias_constraint"),19,0)
        self.main_layout.addWidget(self.bias_constraint,19,1)
        self.main_layout.addWidget(self.bias_constraint_stack,20,1)
        
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass        
    
class Conv2DLayerControlWidget(Conv1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass

class Conv3DLayerControlWidget(Conv1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass

class SeparableConv1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.filters = QLineEdit("(0)")
        self.kernal_size = QLineEdit("(0)")
        self.strides = QLineEdit("1")
        self.padding = QComboBox()
        self.padding.addItems(["same", "valid", "casual"])
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_first", "channels_last"])
        self.dilation_rate = QLineEdit("0")
        self.activation = QComboBox()
        self.activation.addItems([
            "sigmoid",
            "tanh",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])
        self.use_bias = QComboBox()
        self.use_bias.addItems(["True","False"])
        """
        Bias Initializer

        """
        self.bias_initializer = QComboBox()
        self.bias_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.bias_initializer.currentIndexChanged[int].connect(lambda index : self.bias_initializer_stack.setCurrentIndex(index))
        self.bias_initializer_stack = QStackedWidget()
        self.bias_initializer_stack.addWidget(RandomUniformUI())
        self.bias_initializer_stack.addWidget(ZerosUI())
        self.bias_initializer_stack.addWidget(OnesUI())
        self.bias_initializer_stack.addWidget(ConstantUI())
        self.bias_initializer_stack.addWidget(RandomNormalUI())
        self.bias_initializer_stack.addWidget(TruncatedNormalUI())
        self.bias_initializer_stack.addWidget(VarianceScalingUI())
        self.bias_initializer_stack.addWidget(OrthogonalUI())
        self.bias_initializer_stack.addWidget(IdentityUI())
        self.bias_initializer_stack.addWidget(lecunUniformUI())
        self.bias_initializer_stack.addWidget(glorotNormalUI())
        self.bias_initializer_stack.addWidget(glorotUniformUI())
        self.bias_initializer_stack.addWidget(heNormalUI())
        self.bias_initializer_stack.addWidget(lecunNormalUI())
        self.bias_initializer_stack.addWidget(heUniformUI())
        """
        depthwise_initializer
        """
        self.depthwise_initializer = QComboBox()
        self.depthwise_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.depthwise_initializer.currentIndexChanged[int].connect(lambda index : self.depthwise_initializer_stack.setCurrentIndex(index))
        self.depthwise_initializer_stack = QStackedWidget()
        self.depthwise_initializer_stack.addWidget(RandomUniformUI())
        self.depthwise_initializer_stack.addWidget(ZerosUI())
        self.depthwise_initializer_stack.addWidget(OnesUI())
        self.depthwise_initializer_stack.addWidget(ConstantUI())
        self.depthwise_initializer_stack.addWidget(RandomNormalUI())
        self.depthwise_initializer_stack.addWidget(TruncatedNormalUI())
        self.depthwise_initializer_stack.addWidget(VarianceScalingUI())
        self.depthwise_initializer_stack.addWidget(OrthogonalUI())
        self.depthwise_initializer_stack.addWidget(IdentityUI())
        self.depthwise_initializer_stack.addWidget(lecunUniformUI())
        self.depthwise_initializer_stack.addWidget(glorotNormalUI())
        self.depthwise_initializer_stack.addWidget(glorotUniformUI())
        self.depthwise_initializer_stack.addWidget(heNormalUI())
        self.depthwise_initializer_stack.addWidget(lecunNormalUI())
        self.depthwise_initializer_stack.addWidget(heUniformUI())
        """
        pointwise_initializer
        """
        self.pointwise_initializer = QComboBox()
        self.pointwise_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.pointwise_initializer.currentIndexChanged[int].connect(lambda index : self.pointwise_initializer_stack.setCurrentIndex(index))
        self.pointwise_initializer_stack = QStackedWidget()
        self.pointwise_initializer_stack.addWidget(RandomUniformUI())
        self.pointwise_initializer_stack.addWidget(ZerosUI())
        self.pointwise_initializer_stack.addWidget(OnesUI())
        self.pointwise_initializer_stack.addWidget(ConstantUI())
        self.pointwise_initializer_stack.addWidget(RandomNormalUI())
        self.pointwise_initializer_stack.addWidget(TruncatedNormalUI())
        self.pointwise_initializer_stack.addWidget(VarianceScalingUI())
        self.pointwise_initializer_stack.addWidget(OrthogonalUI())
        self.pointwise_initializer_stack.addWidget(IdentityUI())
        self.pointwise_initializer_stack.addWidget(lecunUniformUI())
        self.pointwise_initializer_stack.addWidget(glorotNormalUI())
        self.pointwise_initializer_stack.addWidget(glorotUniformUI())
        self.pointwise_initializer_stack.addWidget(heNormalUI())
        self.pointwise_initializer_stack.addWidget(lecunNormalUI())
        self.pointwise_initializer_stack.addWidget(heUniformUI())
        """
        Bias regularizer

        """

        self.bias_regularizer = QComboBox()
        self.bias_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.bias_regularizer.currentIndexChanged[int].connect(lambda index : self.bias_regularizer_stack.setCurrentIndex(index))

        self.bias_regularizer_stack = QStackedWidget()
        self.bias_regularizer_stack.addWidget(QLabel("None"))
        self.bias_regularizer_stack.addWidget(l1UI())
        self.bias_regularizer_stack.addWidget(l2UI())
        self.bias_regularizer_stack.addWidget(l1_l2UI())

        """
        activity_regularizer

        """
        self.activity_regularizer = QComboBox()
        self.activity_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.activity_regularizer.currentIndexChanged[int].connect(lambda index : self.activity_regularizer_stack.setCurrentIndex(index))

        self.activity_regularizer_stack = QStackedWidget()
        self.activity_regularizer_stack.addWidget(QLabel("None"))
        self.activity_regularizer_stack.addWidget(l1UI())
        self.activity_regularizer_stack.addWidget(l2UI())
        self.activity_regularizer_stack.addWidget(l1_l2UI())
        """
        activity_regularizer

        """
        self.depthwise_regularizer = QComboBox()
        self.depthwise_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.depthwise_regularizer.currentIndexChanged[int].connect(lambda index : self.depthwise_regularizer_stack.setCurrentIndex(index))

        self.depthwise_regularizer_stack = QStackedWidget()
        self.depthwise_regularizer_stack.addWidget(QLabel("None"))
        self.depthwise_regularizer_stack.addWidget(l1UI())
        self.depthwise_regularizer_stack.addWidget(l2UI())
        self.depthwise_regularizer_stack.addWidget(l1_l2UI())
        """
        activity_regularizer

        """
        self.pointwise_regularizer = QComboBox()
        self.pointwise_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.pointwise_regularizer.currentIndexChanged[int].connect(lambda index : self.pointwise_regularizer_stack.setCurrentIndex(index))

        self.pointwise_regularizer_stack = QStackedWidget()
        self.pointwise_regularizer_stack.addWidget(QLabel("None"))
        self.pointwise_regularizer_stack.addWidget(l1UI())
        self.pointwise_regularizer_stack.addWidget(l2UI())
        self.pointwise_regularizer_stack.addWidget(l1_l2UI())
        """
        bias_constraint

        """
        self.pointwise_constraint = QComboBox()
        self.pointwise_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.pointwise_constraint.currentIndexChanged[int].connect(lambda index : self.pointwise_constraint_stack.setCurrentIndex(index))
        self.pointwise_constraint_stack = QStackedWidget()
        self.pointwise_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.pointwise_constraint_stack.addWidget(MaxNormUI())
        self.pointwise_constraint_stack.addWidget(NonNegUI())
        self.pointwise_constraint_stack.addWidget(UnitNormUI())
        self.pointwise_constraint_stack.addWidget(MinMaxNormUI())        
        """
        bias_constraint

        """
        self.depthwise_constraint = QComboBox()
        self.depthwise_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.depthwise_constraint.currentIndexChanged[int].connect(lambda index : self.depthwise_constraint_stack.setCurrentIndex(index))
        self.depthwise_constraint_stack = QStackedWidget()
        self.depthwise_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.depthwise_constraint_stack.addWidget(MaxNormUI())
        self.depthwise_constraint_stack.addWidget(NonNegUI())
        self.depthwise_constraint_stack.addWidget(UnitNormUI())
        self.depthwise_constraint_stack.addWidget(MinMaxNormUI())        
        """
        bias_constraint

        """
        self.bias_constraint = QComboBox()
        self.bias_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.bias_constraint.currentIndexChanged[int].connect(lambda index : self.bias_constraint_stack.setCurrentIndex(index))
        self.bias_constraint_stack = QStackedWidget()
        self.bias_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.bias_constraint_stack.addWidget(MaxNormUI())
        self.bias_constraint_stack.addWidget(NonNegUI())
        self.bias_constraint_stack.addWidget(UnitNormUI())
        self.bias_constraint_stack.addWidget(MinMaxNormUI())        
        self.init_GUI()
        
    def init_GUI(self):
        """
        Gearup main layout
        """
        self.main_layout.addWidget(QLabel("Filters:"), 0, 0)
        self.main_layout.addWidget(self.filters, 0 , 1)
        self.main_layout.addWidget(QLabel("Kernal Size:"), 1, 0)
        self.main_layout.addWidget(self.kernal_size, 1, 1)
        self.main_layout.addWidget(QLabel("Strides:"), 2, 0)
        self.main_layout.addWidget(self.strides, 2 ,1)
        self.main_layout.addWidget(QLabel("Padding:"), 3, 0)
        self.main_layout.addWidget(self.padding, 3, 1)
        self.main_layout.addWidget(QLabel("Data Format:"), 4, 0)
        self.main_layout.addWidget(self.data_format, 4 ,1)
        self.main_layout.addWidget(QLabel("Dilation rate:"), 5, 0)
        self.main_layout.addWidget(self.dilation_rate, 5, 1)
        self.main_layout.addWidget(QLabel("Activation"), 6, 0)
        self.main_layout.addWidget(self.activation, 6 ,1)
        self.main_layout.addWidget(QLabel("Use Bias:"), 7 , 0)
        self.main_layout.addWidget(self.use_bias, 7, 1)
        self.main_layout.addWidget(QLabel("depthwise_initializer"), 8, 0)
        self.main_layout.addWidget(self.depthwise_initializer, 8, 1)
        self.main_layout.addWidget(self.depthwise_initializer_stack, 9, 1)
        self.main_layout.addWidget(QLabel("pointwise_initializer"), 10, 0)
        self.main_layout.addWidget(self.pointwise_initializer, 10, 1)
        self.main_layout.addWidget(self.pointwise_initializer_stack, 11 , 1)
        self.main_layout.addWidget(QLabel("bias_initializer"), 12, 0)
        self.main_layout.addWidget(self.bias_initializer, 12, 1)
        self.main_layout.addWidget(self.bias_initializer_stack, 13 , 1)
        self.main_layout.addWidget(QLabel("depthwise_regularizer"),14,0)
        self.main_layout.addWidget(self.depthwise_regularizer,14,1)
        self.main_layout.addWidget(self.depthwise_regularizer_stack,15,1)

        self.main_layout.addWidget(QLabel("pointwise_regularizer"),16,0)
        self.main_layout.addWidget(self.pointwise_regularizer,16,1)
        self.main_layout.addWidget(self.pointwise_regularizer_stack,17,1)

        self.main_layout.addWidget(QLabel("activity_regularizer"),18, 0)
        self.main_layout.addWidget(self.activity_regularizer,18,1)
        self.main_layout.addWidget(self.activity_regularizer_stack,19, 1)
        self.main_layout.addWidget(QLabel("bias_regularizer"),18, 0)
        self.main_layout.addWidget(self.bias_regularizer,18,1)
        self.main_layout.addWidget(self.bias_regularizer_stack,19, 1)
        
        self.main_layout.addWidget(QLabel("depthwise_constraint"),20,0)
        self.main_layout.addWidget(self.depthwise_constraint,20,1)
        self.main_layout.addWidget(self.depthwise_constraint_stack,21,1)
        self.main_layout.addWidget(QLabel("pointwise_constraint"),22,0)
        self.main_layout.addWidget(self.pointwise_constraint,22,1)
        self.main_layout.addWidget(self.pointwise_constraint_stack,23,1)
        self.main_layout.addWidget(QLabel("bias_constraint"),24,0)
        self.main_layout.addWidget(self.bias_constraint,24,1)
        self.main_layout.addWidget(self.bias_constraint_stack,25, 1)
        
        self.setLayout(self.main_layout)
        self.set_styling()
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class SeparableConv2DLayerControlWidget(SeparableConv1DLayerControlWidget):
    def __init__(self):
        super().__init__()       
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class DepthwiseConv2DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.kernal_size = QLineEdit("(0)")
        self.strides = QLineEdit("1")
        self.padding = QComboBox()
        self.padding.addItems(["same", "valid", "casual"])
        self.depth_multiplier = QLineEdit("1")
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_first", "channels_last"])
        self.dilation_rate = QLineEdit("0")
        self.activation = QComboBox()
        self.activation.addItems([
            "sigmoid",
            "tanh",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])
        self.use_bias = QComboBox()
        self.use_bias.addItems(["True","False"])
        """
        Bias Initializer

        """
        self.bias_initializer = QComboBox()
        self.bias_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.bias_initializer.currentIndexChanged[int].connect(lambda index : self.bias_initializer_stack.setCurrentIndex(index))
        self.bias_initializer_stack = QStackedWidget()
        self.bias_initializer_stack.addWidget(RandomUniformUI())
        self.bias_initializer_stack.addWidget(ZerosUI())
        self.bias_initializer_stack.addWidget(OnesUI())
        self.bias_initializer_stack.addWidget(ConstantUI())
        self.bias_initializer_stack.addWidget(RandomNormalUI())
        self.bias_initializer_stack.addWidget(TruncatedNormalUI())
        self.bias_initializer_stack.addWidget(VarianceScalingUI())
        self.bias_initializer_stack.addWidget(OrthogonalUI())
        self.bias_initializer_stack.addWidget(IdentityUI())
        self.bias_initializer_stack.addWidget(lecunUniformUI())
        self.bias_initializer_stack.addWidget(glorotNormalUI())
        self.bias_initializer_stack.addWidget(glorotUniformUI())
        self.bias_initializer_stack.addWidget(heNormalUI())
        self.bias_initializer_stack.addWidget(lecunNormalUI())
        self.bias_initializer_stack.addWidget(heUniformUI())
        """
        depthwise_initializer
        """
        self.depthwise_initializer = QComboBox()
        self.depthwise_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.depthwise_initializer.currentIndexChanged[int].connect(lambda index : self.depthwise_initializer_stack.setCurrentIndex(index))
        self.depthwise_initializer_stack = QStackedWidget()
        self.depthwise_initializer_stack.addWidget(RandomUniformUI())
        self.depthwise_initializer_stack.addWidget(ZerosUI())
        self.depthwise_initializer_stack.addWidget(OnesUI())
        self.depthwise_initializer_stack.addWidget(ConstantUI())
        self.depthwise_initializer_stack.addWidget(RandomNormalUI())
        self.depthwise_initializer_stack.addWidget(TruncatedNormalUI())
        self.depthwise_initializer_stack.addWidget(VarianceScalingUI())
        self.depthwise_initializer_stack.addWidget(OrthogonalUI())
        self.depthwise_initializer_stack.addWidget(IdentityUI())
        self.depthwise_initializer_stack.addWidget(lecunUniformUI())
        self.depthwise_initializer_stack.addWidget(glorotNormalUI())
        self.depthwise_initializer_stack.addWidget(glorotUniformUI())
        self.depthwise_initializer_stack.addWidget(heNormalUI())
        self.depthwise_initializer_stack.addWidget(lecunNormalUI())
        self.depthwise_initializer_stack.addWidget(heUniformUI())
        """
        Bias regularizer
        """
        self.bias_regularizer = QComboBox()
        self.bias_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.bias_regularizer.currentIndexChanged[int].connect(lambda index : self.bias_regularizer_stack.setCurrentIndex(index))

        self.bias_regularizer_stack = QStackedWidget()
        self.bias_regularizer_stack.addWidget(QLabel("None"))
        self.bias_regularizer_stack.addWidget(l1UI())
        self.bias_regularizer_stack.addWidget(l2UI())
        self.bias_regularizer_stack.addWidget(l1_l2UI())

        """
        activity_regularizer

        """
        self.activity_regularizer = QComboBox()
        self.activity_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.activity_regularizer.currentIndexChanged[int].connect(lambda index : self.activity_regularizer_stack.setCurrentIndex(index))

        self.activity_regularizer_stack = QStackedWidget()
        self.activity_regularizer_stack.addWidget(QLabel("None"))
        self.activity_regularizer_stack.addWidget(l1UI())
        self.activity_regularizer_stack.addWidget(l2UI())
        self.activity_regularizer_stack.addWidget(l1_l2UI())
        """
        depthwise_regularizer
        """
        self.depthwise_regularizer = QComboBox()
        self.depthwise_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.depthwise_regularizer.currentIndexChanged[int].connect(lambda index : self.depthwise_regularizer_stack.setCurrentIndex(index))

        self.depthwise_regularizer_stack = QStackedWidget()
        self.depthwise_regularizer_stack.addWidget(QLabel("None"))
        self.depthwise_regularizer_stack.addWidget(l1UI())
        self.depthwise_regularizer_stack.addWidget(l2UI())
        self.depthwise_regularizer_stack.addWidget(l1_l2UI())      
        """
        bias_constraint
        """
        self.depthwise_constraint = QComboBox()
        self.depthwise_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.depthwise_constraint.currentIndexChanged[int].connect(lambda index : self.depthwise_constraint_stack.setCurrentIndex(index))
        self.depthwise_constraint_stack = QStackedWidget()
        self.depthwise_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.depthwise_constraint_stack.addWidget(MaxNormUI())
        self.depthwise_constraint_stack.addWidget(NonNegUI())
        self.depthwise_constraint_stack.addWidget(UnitNormUI())
        self.depthwise_constraint_stack.addWidget(MinMaxNormUI())        
        """
        bias_constraint
        """
        self.bias_constraint = QComboBox()
        self.bias_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.bias_constraint.currentIndexChanged[int].connect(lambda index : self.bias_constraint_stack.setCurrentIndex(index))
        self.bias_constraint_stack = QStackedWidget()
        self.bias_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.bias_constraint_stack.addWidget(MaxNormUI())
        self.bias_constraint_stack.addWidget(NonNegUI())
        self.bias_constraint_stack.addWidget(UnitNormUI())
        self.bias_constraint_stack.addWidget(MinMaxNormUI())        
        self.init_GUI()
            
    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)  
        self.main_layout.addWidget(QLabel("Kernal Size:"), 0, 0)
        self.main_layout.addWidget(self.kernal_size, 0, 1)
        self.main_layout.addWidget(QLabel("Strides:"), 1, 0)
        self.main_layout.addWidget(self.strides, 1 ,1)
        self.main_layout.addWidget(QLabel("Padding:"), 2, 0)
        self.main_layout.addWidget(self.padding, 2, 1)
        self.main_layout.addWidget(QLabel("Data Format:"), 3, 0)
        self.main_layout.addWidget(self.data_format, 3 ,1)
        self.main_layout.addWidget(QLabel("Dilation rate:"), 4, 0)
        self.main_layout.addWidget(self.dilation_rate, 4, 1)
        self.main_layout.addWidget(QLabel("Activation"), 5, 0)
        self.main_layout.addWidget(self.activation, 5 ,1)
        self.main_layout.addWidget(QLabel("Use Bias:"),6 , 0)
        self.main_layout.addWidget(self.use_bias, 6, 1)
        self.main_layout.addWidget(QLabel("depthwise_initializer:"), 7, 0)
        self.main_layout.addWidget(self.depthwise_initializer, 7, 1)
        self.main_layout.addWidget(self.depthwise_initializer_stack, 8, 1)
        self.main_layout.addWidget(QLabel("bias_initializer:"), 9, 0)
        self.main_layout.addWidget(self.bias_initializer, 9 ,1)
        self.main_layout.addWidget(self.bias_initializer_stack, 10, 1)
        
        self.main_layout.addWidget(QLabel("depthwise_regularizer"),11,0)
        self.main_layout.addWidget(self.depthwise_regularizer,11,1)
        self.main_layout.addWidget(self.depthwise_regularizer_stack,12,1)

        self.main_layout.addWidget(QLabel("bias_regularizer"),13, 0)
        self.main_layout.addWidget(self.bias_regularizer,13,1)
        self.main_layout.addWidget(self.bias_regularizer_stack,14, 1)

        self.main_layout.addWidget(QLabel("activity_regularizer"),15, 0)
        self.main_layout.addWidget(self.activity_regularizer,15,1)
        self.main_layout.addWidget(self.activity_regularizer_stack,16, 1)
        
        self.main_layout.addWidget(QLabel("depthwise_constraint"),17,0)
        self.main_layout.addWidget(self.depthwise_constraint,17,1)
        self.main_layout.addWidget(self.depthwise_constraint_stack,18,1)

        self.main_layout.addWidget(QLabel("bias_constraint"),19, 0)
        self.main_layout.addWidget(self.bias_constraint,19, 1)
        self.main_layout.addWidget(self.bias_constraint_stack,20, 1)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
        
class Conv2DTransposeLayerControlWidget(Conv1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def init_GUI(self):
        self.main_layout.addWidget(QLabel("Filters:"), 0, 0)
        self.main_layout.addWidget(self.filters, 0 , 1)
        self.main_layout.addWidget(QLabel("Kernal Size:"), 1, 0)
        self.main_layout.addWidget(self.kernal_size, 1, 1)
        self.main_layout.addWidget(QLabel("Strides:"), 2, 0)
        self.main_layout.addWidget(self.strides, 2 ,1)
        self.main_layout.addWidget(QLabel("Padding:"), 3, 0)
        self.main_layout.addWidget(self.padding, 3, 1)
        self.main_layout.addWidget(QLabel("Data Format:"), 4, 0)
        self.main_layout.addWidget(self.data_format, 4 ,1)
        self.main_layout.addWidget(QLabel("Dilation rate:"), 5, 0)
        self.main_layout.addWidget(self.dilation_rate, 5, 1)
        self.main_layout.addWidget(QLabel("Activation"), 6, 0)
        self.main_layout.addWidget(self.activation, 6 ,1)
        self.main_layout.addWidget(QLabel("Use Bias:"), 7 , 0)
        self.main_layout.addWidget(self.use_bias, 7, 1)
        
        self.main_layout.addWidget(QLabel("kernelInitializer"),8,0)
        self.main_layout.addWidget(self.kernel_initializer,8,1)
        self.main_layout.addWidget(self.kernel_initializer_stack,9,1)

        self.main_layout.addWidget(QLabel("Bias Initializer"),9,0)
        self.main_layout.addWidget(self.bias_initializer,9,1)
        self.main_layout.addWidget(self.bias_initializer_stack,10,1)

        self.main_layout.addWidget(QLabel("kernel_regularizer"),11,0)
        self.main_layout.addWidget(self.kernel_regularizer,11,1)
        self.main_layout.addLayout(self.kernel_regularizer_stack,12,1)

        self.main_layout.addWidget(QLabel("bias_regularizer"),13,0)
        self.main_layout.addWidget(self.bias_regularizer,13,1)
        self.main_layout.addLayout(self.bias_regularizer_stack,14,1)

        self.main_layout.addWidget(QLabel("activity_regularizer"),15,0)
        self.main_layout.addWidget(self.activity_regularizer,15,1)
        self.main_layout.addLayout(self.activity_regularizer_stack,16,1)

        self.main_layout.addWidget(QLabel("kernel_constraint"),17,0)
        self.main_layout.addWidget(self.kernel_constraint,17,1)
        self.main_layout.addWidget(self.kernel_constraint_stack,18,1)

        self.main_layout.addWidget(QLabel("bias_constraint"),19,0)
        self.main_layout.addWidget(self.bias_constraint,19,1)
        self.main_layout.addWidget(self.bias_constraint_stack,20,1)

        self.output_padding = QLineEdit("None")        
        self.main_layout.addWidget(QLabel("Output Padding"), 21, 0)
        self.main_layout.addWidget(self.output_padding, 21, 1)
                
        self.setLayout(self.main_layout)
        self.set_styling()        
    
    def parse_arguments(self):
        pass    

class Conv3DTransposeLayerControlWidget(Conv2DTransposeLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass        

#############################################################################

##############################Pooling Layers#################################
'''
DONE
'''
class MaxPooling1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.pool_size = QLineEdit("2")
        self.stride = QLineEdit("None")
        self.padding = QComboBox()
        self.padding.addItems(["valid","same"])
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last","channels_first"])
        self.init_GUI()

    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(QLabel("pool_size:"),0,0)
        self.main_layout.addWidget(self.pool_size,0,1)
        self.main_layout.addWidget(QLabel("stride:"),1,0)
        self.main_layout.addWidget(self.stride,1,1)
        self.main_layout.addWidget(QLabel("padding"),2,0)
        self.main_layout.addWidget(self.padding,2,1)
        self.main_layout.addWidget(QLabel("data_format:"),3,0)
        self.main_layout.addWidget(self.data_format,3,1)
        self.setLayout(self.main_layout)
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass

class MaxPooling2DLayerControlWidget(MaxPooling1DLayerControlWidget):
    def __init__(self):
        super().__init__()
        self.pool_size.setText("(2,2)")

    def parse_argument(self):
        pass

class MaxPooling3DLayerControlWidget(MaxPooling1DLayerControlWidget):
    def __init__(self):
        super().__init__()
        self.pool_size.setText("(2,2,2)")

    def parse_arguments(self):
        pass
    
class AveragePooling1DLayerControlWidget(MaxPooling1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    def parse_arguments(self):
        pass

class AveragePooling2DLayerControlWidget(MaxPooling2DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass

class AveragePooling3DLayerControlWidget(MaxPooling3DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass
    
class GlobalMaxPooling1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.data_format = QComboBox()
        self.data_format.addItems(["None", "channels_last", "channels_first"])
        self.init_GUI()


    def init_GUI(self):
        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addRow(QLabel("data_format: "),self.data_format)

        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass
    
class GlobalMaxPooling2DLayerControlWidget(GlobalMaxPooling1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass

class GlobalMaxPooling3DLayerControlWidget(GlobalMaxPooling1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass
    
class GlobalAveragePooling1DLayerControlWidget(GlobalMaxPooling1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass

class GlobalAveragePooling2DLayerControlWidget(GlobalMaxPooling1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass

class GlobalAveragePooling3DLayerControlWidget(GlobalMaxPooling1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass

#############################################################################

######################## Recurrent layers ################################### 
class SimpleRNNLayerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.neuron = QLineEdit("0")
        self.activation = QComboBox()
        self.activation.addItems([
            "sigmoid",
            "tanh",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])
        self.use_bias = QComboBox()
        self.use_bias.addItems(["True","False"])

        """
        Kernel Initializer

        """
        self.kernel_initializer = QComboBox()
        self.kernel_initializer.addItems([
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Orthogonal",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "glorot_uniform",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.kernel_initializer.currentIndexChanged[int].connect(lambda index: self.kernel_initializer_stack.setCurrentIndex(index))
    

        self.kernel_initializer_stack = QStackedWidget()
        self.kernel_initializer_stack.addWidget(RandomUniformUI())
        self.kernel_initializer_stack.addWidget(ZerosUI())
        self.kernel_initializer_stack.addWidget(OnesUI())
        self.kernel_initializer_stack.addWidget(ConstantUI())
        self.kernel_initializer_stack.addWidget(RandomNormalUI())
        self.kernel_initializer_stack.addWidget(TruncatedNormalUI())
        self.kernel_initializer_stack.addWidget(VarianceScalingUI())
        self.kernel_initializer_stack.addWidget(OrthogonalUI())
        self.kernel_initializer_stack.addWidget(IdentityUI())
        self.kernel_initializer_stack.addWidget(lecunUniformUI())
        self.kernel_initializer_stack.addWidget(glorotNormalUI())
        self.kernel_initializer_stack.addWidget(glorotUniformUI())
        self.kernel_initializer_stack.addWidget(heNormalUI())
        self.kernel_initializer_stack.addWidget(lecunNormalUI())
        self.kernel_initializer_stack.addWidget(heUniformUI())

        """
        Bias Initializer

        """
        self.bias_initializer = QComboBox()
        self.bias_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.bias_initializer.currentIndexChanged[int].connect(lambda index : self.bias_initializer_stack.setCurrentIndex(index))
        self.bias_initializer_stack = QStackedWidget()
        self.bias_initializer_stack.addWidget(RandomUniformUI())
        self.bias_initializer_stack.addWidget(ZerosUI())
        self.bias_initializer_stack.addWidget(OnesUI())
        self.bias_initializer_stack.addWidget(ConstantUI())
        self.bias_initializer_stack.addWidget(RandomNormalUI())
        self.bias_initializer_stack.addWidget(TruncatedNormalUI())
        self.bias_initializer_stack.addWidget(VarianceScalingUI())
        self.bias_initializer_stack.addWidget(OrthogonalUI())
        self.bias_initializer_stack.addWidget(IdentityUI())
        self.bias_initializer_stack.addWidget(lecunUniformUI())
        self.bias_initializer_stack.addWidget(glorotNormalUI())
        self.bias_initializer_stack.addWidget(glorotUniformUI())
        self.bias_initializer_stack.addWidget(heNormalUI())
        self.bias_initializer_stack.addWidget(lecunNormalUI())
        self.bias_initializer_stack.addWidget(heUniformUI())
        """
        Kernal regularizer
        """
        self.kernel_regularizer = QComboBox()
        self.kernel_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.kernel_regularizer.currentIndexChanged[int].connect(lambda index : self.kernel_regularizer_stack.setCurrentIndex(index))

        self.kernel_regularizer_stack = QStackedLayout()
        self.kernel_regularizer_stack.addWidget(QLabel("None"))
        self.kernel_regularizer_stack.addWidget(l1UI())
        self.kernel_regularizer_stack.addWidget(l2UI())
        self.kernel_regularizer_stack.addWidget(l1_l2UI())

        """
        Bias regularizer

        """

        self.bias_regularizer = QComboBox()
        self.bias_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.bias_regularizer.currentIndexChanged[int].connect(lambda index : self.bias_regularizer_stack.setCurrentIndex(index))

        self.bias_regularizer_stack = QStackedLayout()
        self.bias_regularizer_stack.addWidget(QLabel("None"))
        self.bias_regularizer_stack.addWidget(l1UI())
        self.bias_regularizer_stack.addWidget(l2UI())
        self.bias_regularizer_stack.addWidget(l1_l2UI())

        """
        activity_regularizer

        """
        self.activity_regularizer = QComboBox()
        self.activity_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.activity_regularizer.currentIndexChanged[int].connect(lambda index : self.activity_regularizer_stack.setCurrentIndex(index))

        self.activity_regularizer_stack = QStackedLayout()
        self.activity_regularizer_stack.addWidget(QLabel("None"))
        self.activity_regularizer_stack.addWidget(l1UI())
        self.activity_regularizer_stack.addWidget(l2UI())
        self.activity_regularizer_stack.addWidget(l1_l2UI())

        """
        kernel_constraint

        """
        self.kernel_constraint = QComboBox()
        self.kernel_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.kernel_constraint.currentIndexChanged[int].connect(lambda index : self.kernel_constraint_stack.setCurrentIndex(index))
        self.kernel_constraint_stack = QStackedWidget()
        self.kernel_constraint_stack.addWidget(QLabel("None"))
        self.kernel_constraint_stack.addWidget(MaxNormUI())
        self.kernel_constraint_stack.addWidget(NonNegUI())
        self.kernel_constraint_stack.addWidget(UnitNormUI())
        self.kernel_constraint_stack.addWidget(MinMaxNormUI())

        """
        bias_constraint

        """
        self.bias_constraint = QComboBox()
        self.bias_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.bias_constraint.currentIndexChanged[int].connect(lambda index : self.bias_constraint_stack.setCurrentIndex(index))
        self.bias_constraint_stack = QStackedWidget()
        #self.bias_constraint_stack.setAlignment(Qt.AlignTop)        
        #self.bias_constraint_stack.setSpacing(0)
        self.bias_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.bias_constraint_stack.addWidget(MaxNormUI())
        self.bias_constraint_stack.addWidget(NonNegUI())
        self.bias_constraint_stack.addWidget(UnitNormUI())
        self.bias_constraint_stack.addWidget(MinMaxNormUI())
        """
        recurrent_initializer
        """
        self.recurrent_initializer = QComboBox()
        self.recurrent_initializer.addItems(["RandomUniform",
                                        "Zeros",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.recurrent_initializer.currentIndexChanged[int].connect(lambda index : self.recurrent_initializer_stack.setCurrentIndex(index))
        self.recurrent_initializer_stack = QStackedWidget()
        self.recurrent_initializer_stack.addWidget(RandomUniformUI())
        self.recurrent_initializer_stack.addWidget(ZerosUI())
        self.recurrent_initializer_stack.addWidget(OnesUI())
        self.recurrent_initializer_stack.addWidget(ConstantUI())
        self.recurrent_initializer_stack.addWidget(RandomNormalUI())
        self.recurrent_initializer_stack.addWidget(TruncatedNormalUI())
        self.recurrent_initializer_stack.addWidget(VarianceScalingUI())
        self.recurrent_initializer_stack.addWidget(OrthogonalUI())
        self.recurrent_initializer_stack.addWidget(IdentityUI())
        self.recurrent_initializer_stack.addWidget(lecunUniformUI())
        self.recurrent_initializer_stack.addWidget(glorotNormalUI())
        self.recurrent_initializer_stack.addWidget(glorotUniformUI())
        self.recurrent_initializer_stack.addWidget(heNormalUI())
        self.recurrent_initializer_stack.addWidget(lecunNormalUI())
        self.recurrent_initializer_stack.addWidget(heUniformUI())      
        """
        Recurrent regularizer
        """
        self.recurrent_regularizer = QComboBox()
        self.recurrent_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.recurrent_regularizer.currentIndexChanged[int].connect(lambda index : self.recurrent_regularizer_stack.setCurrentIndex(index))

        self.recurrent_regularizer_stack = QStackedWidget()
        self.recurrent_regularizer_stack.addWidget(QLabel("None"))
        self.recurrent_regularizer_stack.addWidget(l1UI())
        self.recurrent_regularizer_stack.addWidget(l2UI())
        self.recurrent_regularizer_stack.addWidget(l1_l2UI())
        """
        Recurrent constraint
        """
        self.recurrent_constraint = QComboBox()
        self.recurrent_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.recurrent_constraint.currentIndexChanged[int].connect(lambda index : self.recurrent_constraint_stack.setCurrentIndex(index))
        self.recurrent_constraint_stack = QStackedWidget()
        self.recurrent_constraint_stack.addWidget(QLabel("None"))
        self.recurrent_constraint_stack.addWidget(MaxNormUI())
        self.recurrent_constraint_stack.addWidget(NonNegUI())
        self.recurrent_constraint_stack.addWidget(UnitNormUI())
        self.recurrent_constraint_stack.addWidget(MinMaxNormUI())       
        
        self.dropout = QLineEdit("0.0")
        self.recurrent_dropout = QLineEdit("0.0")
        self.return_sequences = QComboBox()
        self.return_sequences.addItems(["False", "True"])
        self.return_state = QComboBox()
        self.return_state.addItems(["False", "True"])
        self.go_backwards = QComboBox()
        self.go_backwards.addItems(["False", "True"])
        self.stateful = QComboBox()
        self.stateful.addItems(["False", "True"])
        self.unroll = QComboBox()
        self.unroll.addItems(["False", "True"])      
        self.init_GUI()
        
    def init_GUI(self):
        """
        self.main_layout

        """
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(QLabel('Neurons:'),0,0)
        self.main_layout.addWidget(self.neuron,0,1)

        self.main_layout.addWidget(QLabel("Activation:"),1,0)
        self.main_layout.addWidget(self.activation,1,1)

        self.main_layout.addWidget(QLabel("Use Bias:"),2,0)
        self.main_layout.addWidget(self.use_bias,2,1)

        self.main_layout.addWidget(QLabel("kernelInitializer"),3,0)
        self.main_layout.addWidget(self.kernel_initializer,3,1)
        self.main_layout.addWidget(self.kernel_initializer_stack,4,1)

        self.main_layout.addWidget(QLabel("Bias Initializer"),5,0)
        self.main_layout.addWidget(self.bias_initializer,5,1)
        self.main_layout.addWidget(self.bias_initializer_stack,6,1)

        self.main_layout.addWidget(QLabel("kernel_regularizer"),7,0)
        self.main_layout.addWidget(self.kernel_regularizer,7,1)
        self.main_layout.addLayout(self.kernel_regularizer_stack,8,1)

        self.main_layout.addWidget(QLabel("bias_regularizer"),9,0)
        self.main_layout.addWidget(self.bias_regularizer,9,1)
        self.main_layout.addLayout(self.bias_regularizer_stack,10,1)

        self.main_layout.addWidget(QLabel("activity_regularizer"),11,0)
        self.main_layout.addWidget(self.activity_regularizer,11,1)
        self.main_layout.addLayout(self.activity_regularizer_stack,12,1)

        self.main_layout.addWidget(QLabel("kernel_constraint"),13,0)
        self.main_layout.addWidget(self.kernel_constraint,13,1)
        self.main_layout.addWidget(self.kernel_constraint_stack,14,1)

        self.main_layout.addWidget(QLabel("bias_constraint"),15,0)
        self.main_layout.addWidget(self.bias_constraint,15,1)
        self.main_layout.addWidget(self.bias_constraint_stack,16,1)        
        self.main_layout.addWidget(QLabel("Recurrent initializer") ,17, 0)
        self.main_layout.addWidget(self.recurrent_initializer, 17, 1)
        self.main_layout.addWidget(self.recurrent_initializer_stack, 18, 1)
        self.main_layout.addWidget(QLabel("Recurrent Regularizer: "), 19, 0)
        self.main_layout.addWidget(self.recurrent_regularizer, 19, 1)
        self.main_layout.addWidget(self.recurrent_regularizer_stack, 20, 1)
        self.main_layout.addWidget(QLabel("Recurrent_constraint:"), 21, 0)
        self.main_layout.addWidget(self.recurrent_constraint, 21, 1)
        self.main_layout.addWidget(self.recurrent_constraint_stack, 22, 1)
        self.main_layout.addWidget(QLabel("dropout:"), 23, 0)  
        self.main_layout.addWidget(self.dropout, 23, 1)
        self.main_layout.addWidget(QLabel("Return Sequance:"), 24, 0)
        self.main_layout.addWidget(self.return_sequences, 24 , 1)
        self.main_layout.addWidget(QLabel("Return State:"), 25, 0)
        self.main_layout.addWidget(self.return_state, 25, 1)
        self.main_layout.addWidget(QLabel("go Backwards"), 26, 0)
        self.main_layout.addWidget(self.go_backwards, 26, 1)
        self.main_layout.addWidget(QLabel("Stateful:"), 27, 0)
        self.main_layout.addWidget(self.stateful, 27, 1)
        self.main_layout.addWidget(QLabel("Unrool:"), 28, 0)
        self.main_layout.addWidget(self.unroll, 28, 1)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        pass 
    
    def parse_arguments(self):
        pass

class LSTMLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.units = QLineEdit("2")
        self.activation = QComboBox()
        self.activation.addItems([
            "tanh",
            "None",
            "sigmoid",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])
        self.recurrent_activation = QComboBox()
        self.recurrent_activation.addItems([
            "sigmoid",
            "None",
            "tanh",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])
        self.use_bias = QComboBox()
        self.use_bias.addItems(["True","False"])

        self.kernel_initializer = QComboBox()
        self.kernel_initializer.addItems([
            "glorot_uniform",
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Orthogonal",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.kernel_initializer.currentIndexChanged[int].connect(lambda index: self.kernel_initializer_stack.setCurrentIndex(index))
    

        self.kernel_initializer_stack = QStackedWidget()
        self.kernel_initializer_stack.addWidget(glorotUniformUI())
        self.kernel_initializer_stack.addWidget(RandomUniformUI())
        self.kernel_initializer_stack.addWidget(ZerosUI())
        self.kernel_initializer_stack.addWidget(OnesUI())
        self.kernel_initializer_stack.addWidget(ConstantUI())
        self.kernel_initializer_stack.addWidget(RandomNormalUI())
        self.kernel_initializer_stack.addWidget(TruncatedNormalUI())
        self.kernel_initializer_stack.addWidget(VarianceScalingUI())
        self.kernel_initializer_stack.addWidget(OrthogonalUI())
        self.kernel_initializer_stack.addWidget(IdentityUI())
        self.kernel_initializer_stack.addWidget(lecunUniformUI())
        self.kernel_initializer_stack.addWidget(glorotNormalUI())
        self.kernel_initializer_stack.addWidget(heNormalUI())
        self.kernel_initializer_stack.addWidget(lecunNormalUI())
        self.kernel_initializer_stack.addWidget(heUniformUI())

        self.recurrent_initializer = QComboBox()
        self.recurrent_initializer.addItems([
            "Orthogonal",
            "glorot_uniform",
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.recurrent_initializer.currentIndexChanged[int].connect(lambda index: self.recurrent_initializer_stack.setCurrentIndex(index))
    
        
        self.recurrent_initializer_stack = QStackedWidget()
        self.recurrent_initializer_stack.addWidget(OrthogonalUI())
        self.recurrent_initializer_stack.addWidget(RandomUniformUI())
        self.recurrent_initializer_stack.addWidget(ZerosUI())
        self.recurrent_initializer_stack.addWidget(OnesUI())
        self.recurrent_initializer_stack.addWidget(ConstantUI())
        self.recurrent_initializer_stack.addWidget(RandomNormalUI())
        self.recurrent_initializer_stack.addWidget(TruncatedNormalUI())
        self.recurrent_initializer_stack.addWidget(VarianceScalingUI())
        self.recurrent_initializer_stack.addWidget(IdentityUI())
        self.recurrent_initializer_stack.addWidget(lecunUniformUI())
        self.recurrent_initializer_stack.addWidget(glorotNormalUI())
        self.recurrent_initializer_stack.addWidget(glorotUniformUI())
        self.recurrent_initializer_stack.addWidget(heNormalUI())
        self.recurrent_initializer_stack.addWidget(lecunNormalUI())
        self.recurrent_initializer_stack.addWidget(heUniformUI())

        self.bias_initializer = QComboBox()
        self.bias_initializer.addItems(["Zeros",
                                        "RandomUniform",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.bias_initializer.currentIndexChanged[int].connect(lambda index : self.bias_initializer_stack.setCurrentIndex(index))\

        self.bias_initializer_stack = QStackedWidget()
        self.bias_initializer_stack.addWidget(ZerosUI())
        self.bias_initializer_stack.addWidget(RandomUniformUI())
        self.bias_initializer_stack.addWidget(OnesUI())
        self.bias_initializer_stack.addWidget(ConstantUI())
        self.bias_initializer_stack.addWidget(RandomNormalUI())
        self.bias_initializer_stack.addWidget(TruncatedNormalUI())
        self.bias_initializer_stack.addWidget(VarianceScalingUI())
        self.bias_initializer_stack.addWidget(OrthogonalUI())
        self.bias_initializer_stack.addWidget(IdentityUI())
        self.bias_initializer_stack.addWidget(lecunUniformUI())
        self.bias_initializer_stack.addWidget(glorotNormalUI())
        self.bias_initializer_stack.addWidget(glorotUniformUI())
        self.bias_initializer_stack.addWidget(heNormalUI())
        self.bias_initializer_stack.addWidget(lecunNormalUI())
        self.bias_initializer_stack.addWidget(heUniformUI())


        self.unit_forget_bias = QComboBox()
        self.unit_forget_bias.addItems(["True","False"])


        self.kernel_regularizer = QComboBox()
        self.kernel_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.kernel_regularizer.currentIndexChanged[int].connect(lambda index : self.kernel_regularizer_stack.setCurrentIndex(index))

        self.kernel_regularizer_stack = QStackedWidget()
        self.kernel_regularizer_stack.addWidget(QLabel("None"))
        self.kernel_regularizer_stack.addWidget(l1UI())
        self.kernel_regularizer_stack.addWidget(l2UI())
        self.kernel_regularizer_stack.addWidget(l1_l2UI())

        self.bias_regularizer = QComboBox()
        self.bias_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.bias_regularizer.currentIndexChanged[int].connect(lambda index : self.bias_regularizer_stack.setCurrentIndex(index))

        self.bias_regularizer_stack = QStackedWidget()
        self.bias_regularizer_stack.addWidget(QLabel("None"))
        self.bias_regularizer_stack.addWidget(l1UI())
        self.bias_regularizer_stack.addWidget(l2UI())
        self.bias_regularizer_stack.addWidget(l1_l2UI())

        """
        activity_regularizer

        """
        self.activity_regularizer = QComboBox()
        self.activity_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.activity_regularizer.currentIndexChanged[int].connect(lambda index : self.activity_regularizer_stack.setCurrentIndex(index))

        self.activity_regularizer_stack = QStackedWidget()
        self.activity_regularizer_stack.addWidget(QLabel("None"))
        self.activity_regularizer_stack.addWidget(l1UI())
        self.activity_regularizer_stack.addWidget(l2UI())
        self.activity_regularizer_stack.addWidget(l1_l2UI())



        self.recurrent_regularizer = QComboBox()
        self.recurrent_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.recurrent_regularizer.currentIndexChanged[int].connect(lambda index : self.recurrent_regularizer_stack.setCurrentIndex(index))

        self.recurrent_regularizer_stack = QStackedWidget()
        self.recurrent_regularizer_stack.addWidget(QLabel("None"))
        self.recurrent_regularizer_stack.addWidget(l1UI())
        self.recurrent_regularizer_stack.addWidget(l2UI())
        self.recurrent_regularizer_stack.addWidget(l1_l2UI())

        """
        kernel_constraint

        """
        self.kernel_constraint = QComboBox()
        self.kernel_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.kernel_constraint.currentIndexChanged[int].connect(lambda index : self.kernel_constraint_stack.setCurrentIndex(index))
        self.kernel_constraint_stack = QStackedWidget()
        self.kernel_constraint_stack.addWidget(QLabel("None"))
        self.kernel_constraint_stack.addWidget(MaxNormUI())
        self.kernel_constraint_stack.addWidget(NonNegUI())
        self.kernel_constraint_stack.addWidget(UnitNormUI())
        self.kernel_constraint_stack.addWidget(MinMaxNormUI())



        self.bias_constraint = QComboBox()
        self.bias_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.bias_constraint.currentIndexChanged[int].connect(lambda index : self.bias_constraint_stack.setCurrentIndex(index))

        self.bias_constraint_stack = QStackedWidget()
        self.bias_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.bias_constraint_stack.addWidget(MaxNormUI())
        self.bias_constraint_stack.addWidget(NonNegUI())
        self.bias_constraint_stack.addWidget(UnitNormUI())
        self.bias_constraint_stack.addWidget(MinMaxNormUI())

        self.recurrent_constraint = QComboBox()
        self.recurrent_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.recurrent_constraint.currentIndexChanged[int].connect(lambda index : self.recurrent_constraint_stack.setCurrentIndex(index))

        self.recurrent_constraint_stack = QStackedWidget()
        self.recurrent_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.recurrent_constraint_stack.addWidget(MaxNormUI())
        self.recurrent_constraint_stack.addWidget(NonNegUI())
        self.recurrent_constraint_stack.addWidget(UnitNormUI())
        self.recurrent_constraint_stack.addWidget(MinMaxNormUI())


        self.dropout = QLineEdit("0")
        self.recurrent_dropout = QLineEdit("0")
        self.implementation = QComboBox()
        self.implementation.addItems(["1","2"])

        self.return_sequences = QComboBox()
        self.return_sequences.addItems(["False","True"])

        self.return_state = QComboBox()
        self.return_state.addItems(["False","True"])

        self.go_backwards = QComboBox()
        self.go_backwards.addItems(["False","True"])

        self.stateful = QComboBox()
        self.stateful.addItems(["False","True"])

        self.time_major = QComboBox()
        self.time_major.addItems(["False","True"])

        self.unroll = QComboBox()
        self.unroll.addItems(["False","True"])
        self.init_GUI()

    def init_GUI(self):
        """
        MAin Layout
        """

        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addRow(QLabel("units: "),self.units)

        self.main_layout.addRow(QLabel("activation: "),self.activation)

        self.main_layout.addRow(QLabel("recurrent_activation"),self.recurrent_activation)
        self.main_layout.addRow(QLabel("use_bias"),self.use_bias)

        self.main_layout.addRow(QLabel("kernel_initializer: "),self.kernel_initializer)
        self.main_layout.addWidget(self.kernel_initializer_stack)

        self.main_layout.addRow(QLabel("recurrent_initializer: "),self.recurrent_initializer)
        self.main_layout.addWidget(self.recurrent_initializer_stack)

        self.main_layout.addRow(QLabel("bias_initializer: "),self.bias_initializer)
        self.main_layout.addWidget(self.bias_initializer_stack)

        self.main_layout.addRow(QLabel("unit_forget_bias"),self.unit_forget_bias)

        self.main_layout.addRow(QLabel("kernel_regularizer: "),self.kernel_regularizer)
        self.main_layout.addWidget(self.kernel_regularizer_stack)

        self.main_layout.addRow(QLabel("recurrent_regularizer: "),self.recurrent_regularizer)
        self.main_layout.addWidget(self.recurrent_regularizer_stack)

        self.main_layout.addRow(QLabel("bias_regularizer: "),self.bias_regularizer)
        self.main_layout.addWidget(self.bias_regularizer_stack)

        self.main_layout.addRow(QLabel("activity_regularizer: "),self.activity_regularizer)
        self.main_layout.addWidget(self.activity_regularizer_stack)

        self.main_layout.addRow(QLabel("kernel_constraint: "),self.kernel_constraint)
        self.main_layout.addWidget(self.kernel_constraint_stack)

        self.main_layout.addRow(QLabel("recurrent_constraint: "),self.recurrent_constraint)
        self.main_layout.addWidget(self.recurrent_constraint_stack)

        self.main_layout.addRow(QLabel("bias_constraint: "),self.bias_constraint)
        self.main_layout.addWidget(self.bias_constraint_stack)

        self.main_layout.addRow(QLabel("dropout: "),self.dropout)
        self.main_layout.addRow(QLabel("recurrent_dropout: "),self.recurrent_dropout)
        self.main_layout.addRow(QLabel("implementation: "),self.implementation)
        self.main_layout.addRow(QLabel("return_sequences: "),self.return_sequences)
        self.main_layout.addRow(QLabel("return_state: "),self.return_state)
        self.main_layout.addRow(QLabel("go_backwards: "),self.go_backwards)
        self.main_layout.addRow(QLabel("stateful: "),self.stateful)
        self.main_layout.addRow(QLabel("time_major: "),self.time_major)
        self.main_layout.addRow(QLabel("unroll: "),self.unroll)

        self.scroll_panel = QWidget()
        self.scroll_panel_layout = QGridLayout(self.scroll_panel)
        self.scroll_panel_layout.setContentsMargins(0,0,0,0)


        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.scroll_panel)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.scroll_area)
        self.scroll_panel_layout.addLayout(self.main_layout,0,0)
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_argument(self):
        pass

class GRULayerControlWidget(LSTMLayerControlWidget):
    def __init__(self):
        self.reset_after = QComboBox()
        self.reset_after.addItems(["True","False"])
        super().__init__()
        

    def init_GUI(self):
        """
        MAin Layout
        """

        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addRow(QLabel("units: "),self.units)

        self.main_layout.addRow(QLabel("activation: "),self.activation)

        self.main_layout.addRow(QLabel("recurrent_activation"),self.recurrent_activation)
        self.main_layout.addRow(QLabel("use_bias"),self.use_bias)

        self.main_layout.addRow(QLabel("kernel_initializer: "),self.kernel_initializer)
        self.main_layout.addWidget(self.kernel_initializer_stack)

        self.main_layout.addRow(QLabel("recurrent_initializer: "),self.recurrent_initializer)
        self.main_layout.addWidget(self.recurrent_initializer_stack)

        self.main_layout.addRow(QLabel("bias_initializer: "),self.bias_initializer)
        self.main_layout.addWidget(self.bias_initializer_stack)

        self.main_layout.addRow(QLabel("kernel_regularizer: "),self.kernel_regularizer)
        self.main_layout.addWidget(self.kernel_regularizer_stack)

        self.main_layout.addRow(QLabel("recurrent_regularizer: "),self.recurrent_regularizer)
        self.main_layout.addWidget(self.recurrent_regularizer_stack)

        self.main_layout.addRow(QLabel("bias_regularizer: "),self.bias_regularizer)
        self.main_layout.addWidget(self.bias_regularizer_stack)

        self.main_layout.addRow(QLabel("activity_regularizer: "),self.activity_regularizer)
        self.main_layout.addWidget(self.activity_regularizer_stack)

        self.main_layout.addRow(QLabel("kernel_constraint: "),self.kernel_constraint)
        self.main_layout.addWidget(self.kernel_constraint_stack)

        self.main_layout.addRow(QLabel("recurrent_constraint: "),self.recurrent_constraint)
        self.main_layout.addWidget(self.recurrent_constraint_stack)

        self.main_layout.addRow(QLabel("bias_constraint: "),self.bias_constraint)
        self.main_layout.addWidget(self.bias_constraint_stack)

        self.main_layout.addRow(QLabel("dropout: "),self.dropout)
        self.main_layout.addRow(QLabel("recurrent_dropout: "),self.recurrent_dropout)
        self.main_layout.addRow(QLabel("implementation: "),self.implementation)
        self.main_layout.addRow(QLabel("return_sequences: "),self.return_sequences)
        self.main_layout.addRow(QLabel("return_state: "),self.return_state)
        self.main_layout.addRow(QLabel("go_backwards: "),self.go_backwards)
        self.main_layout.addRow(QLabel("stateful: "),self.stateful)
        self.main_layout.addRow(QLabel("unroll: "),self.unroll)
        self.main_layout.addRow(QLabel("time_major: "),self.time_major)
        self.main_layout.addRow(QLabel("reset_after: "),self.reset_after)
        


        self.scroll_panel = QWidget()
        self.scroll_panel_layout = QGridLayout(self.scroll_panel)
        self.scroll_panel_layout.setContentsMargins(0,0,0,0)


        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.scroll_panel)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.scroll_area)
        self.scroll_panel_layout.addLayout(self.main_layout,0,0)
        self.set_styling()

class ConvLSTM2DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.filters = QLineEdit("2")
        self.kernel_size = QLineEdit("2")
        self.strides = QLineEdit("2")
        self.padding = QComboBox()
        self.padding.addItems(["valid","same"])
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last","channels_first"])
        self.dilation_rate = QLineEdit("1")
        self.activation = QComboBox()
        self.activation.addItems([
            "tanh",
            "None",
            "sigmoid",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "hard_sigmoid",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])

        self.recurrent_activation = QComboBox()
        self.recurrent_activation.addItems([
            "hard_sigmoid",
            "None",
            "sigmoid",
            "tanh",
            "relu",
            "softmax",
            "linear",
            "exponential",
            "softsign",
            "selu",
            "elu",
            "softplus",
            "Custom_my1"])

        self.use_bias = QComboBox()
        self.use_bias.addItems(["True","False"])

        self.kernel_initializer = QComboBox()
        self.kernel_initializer.addItems([
            "glorot_uniform",
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Orthogonal",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.kernel_initializer.currentIndexChanged[int].connect(lambda index: self.kernel_initializer_stack.setCurrentIndex(index))
    

        self.kernel_initializer_stack = QStackedWidget()
        self.kernel_initializer_stack.addWidget(glorotUniformUI())
        self.kernel_initializer_stack.addWidget(RandomUniformUI())
        self.kernel_initializer_stack.addWidget(ZerosUI())
        self.kernel_initializer_stack.addWidget(OnesUI())
        self.kernel_initializer_stack.addWidget(ConstantUI())
        self.kernel_initializer_stack.addWidget(RandomNormalUI())
        self.kernel_initializer_stack.addWidget(TruncatedNormalUI())
        self.kernel_initializer_stack.addWidget(VarianceScalingUI())
        self.kernel_initializer_stack.addWidget(OrthogonalUI())
        self.kernel_initializer_stack.addWidget(IdentityUI())
        self.kernel_initializer_stack.addWidget(lecunUniformUI())
        self.kernel_initializer_stack.addWidget(glorotNormalUI())
        self.kernel_initializer_stack.addWidget(heNormalUI())
        self.kernel_initializer_stack.addWidget(lecunNormalUI())
        self.kernel_initializer_stack.addWidget(heUniformUI())

        self.recurrent_initializer = QComboBox()
        self.recurrent_initializer.addItems([
            "Orthogonal",
            "glorot_uniform",
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.recurrent_initializer.currentIndexChanged[int].connect(lambda index: self.recurrent_initializer_stack.setCurrentIndex(index))
    
        
        self.recurrent_initializer_stack = QStackedWidget()
        self.recurrent_initializer_stack.addWidget(OrthogonalUI())
        self.recurrent_initializer_stack.addWidget(glorotUniformUI())
        self.recurrent_initializer_stack.addWidget(RandomUniformUI())
        self.recurrent_initializer_stack.addWidget(ZerosUI())
        self.recurrent_initializer_stack.addWidget(OnesUI())
        self.recurrent_initializer_stack.addWidget(ConstantUI())
        self.recurrent_initializer_stack.addWidget(RandomNormalUI())
        self.recurrent_initializer_stack.addWidget(TruncatedNormalUI())
        self.recurrent_initializer_stack.addWidget(VarianceScalingUI())
        self.recurrent_initializer_stack.addWidget(IdentityUI())
        self.recurrent_initializer_stack.addWidget(lecunUniformUI())
        self.recurrent_initializer_stack.addWidget(glorotNormalUI())
        self.recurrent_initializer_stack.addWidget(heNormalUI())
        self.recurrent_initializer_stack.addWidget(lecunNormalUI())
        self.recurrent_initializer_stack.addWidget(heUniformUI())

        self.bias_initializer = QComboBox()
        self.bias_initializer.addItems(["Zeros",
                                        "RandomUniform",
                                        "Ones",
                                        "Constant",
                                        "RandomNormal",
                                        "TruncatedNormal",
                                        "VarianceScaling",
                                        "Orthogonal",
                                        "Identity",
                                        "lecun_uniform",
                                        "glorot_normal",
                                        "glorot_uniform",
                                        "he_normal",
                                        "lecun_normal",
                                        "he_uniform"])
        self.bias_initializer.currentIndexChanged[int].connect(lambda index : self.bias_initializer_stack.setCurrentIndex(index))\

        self.bias_initializer_stack = QStackedWidget()
        self.bias_initializer_stack.addWidget(ZerosUI())
        self.bias_initializer_stack.addWidget(RandomUniformUI())
        self.bias_initializer_stack.addWidget(OnesUI())
        self.bias_initializer_stack.addWidget(ConstantUI())
        self.bias_initializer_stack.addWidget(RandomNormalUI())
        self.bias_initializer_stack.addWidget(TruncatedNormalUI())
        self.bias_initializer_stack.addWidget(VarianceScalingUI())
        self.bias_initializer_stack.addWidget(OrthogonalUI())
        self.bias_initializer_stack.addWidget(IdentityUI())
        self.bias_initializer_stack.addWidget(lecunUniformUI())
        self.bias_initializer_stack.addWidget(glorotNormalUI())
        self.bias_initializer_stack.addWidget(glorotUniformUI())
        self.bias_initializer_stack.addWidget(heNormalUI())
        self.bias_initializer_stack.addWidget(lecunNormalUI())
        self.bias_initializer_stack.addWidget(heUniformUI())

        self.unit_forget_bias = QComboBox()
        self.unit_forget_bias.addItems(["True","False"])

        self.kernel_regularizer = QComboBox()
        self.kernel_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.kernel_regularizer.currentIndexChanged[int].connect(lambda index : self.kernel_regularizer_stack.setCurrentIndex(index))

        self.kernel_regularizer_stack = QStackedWidget()
        self.kernel_regularizer_stack.addWidget(QLabel("None"))
        self.kernel_regularizer_stack.addWidget(l1UI())
        self.kernel_regularizer_stack.addWidget(l2UI())
        self.kernel_regularizer_stack.addWidget(l1_l2UI())

        self.bias_regularizer = QComboBox()
        self.bias_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.bias_regularizer.currentIndexChanged[int].connect(lambda index : self.bias_regularizer_stack.setCurrentIndex(index))

        self.bias_regularizer_stack = QStackedWidget()
        self.bias_regularizer_stack.addWidget(QLabel("None"))
        self.bias_regularizer_stack.addWidget(l1UI())
        self.bias_regularizer_stack.addWidget(l2UI())
        self.bias_regularizer_stack.addWidget(l1_l2UI())

        """
        activity_regularizer

        """
        self.activity_regularizer = QComboBox()
        self.activity_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.activity_regularizer.currentIndexChanged[int].connect(lambda index : self.activity_regularizer_stack.setCurrentIndex(index))

        self.activity_regularizer_stack = QStackedWidget()
        self.activity_regularizer_stack.addWidget(QLabel("None"))
        self.activity_regularizer_stack.addWidget(l1UI())
        self.activity_regularizer_stack.addWidget(l2UI())
        self.activity_regularizer_stack.addWidget(l1_l2UI())



        self.recurrent_regularizer = QComboBox()
        self.recurrent_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.recurrent_regularizer.currentIndexChanged[int].connect(lambda index : self.recurrent_regularizer_stack.setCurrentIndex(index))

        self.recurrent_regularizer_stack = QStackedWidget()
        self.recurrent_regularizer_stack.addWidget(QLabel("None"))
        self.recurrent_regularizer_stack.addWidget(l1UI())
        self.recurrent_regularizer_stack.addWidget(l2UI())
        self.recurrent_regularizer_stack.addWidget(l1_l2UI())

        self.kernel_constraint = QComboBox()
        self.kernel_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.kernel_constraint.currentIndexChanged[int].connect(lambda index : self.kernel_constraint_stack.setCurrentIndex(index))
        self.kernel_constraint_stack = QStackedWidget()
        self.kernel_constraint_stack.addWidget(QLabel("None"))
        self.kernel_constraint_stack.addWidget(MaxNormUI())
        self.kernel_constraint_stack.addWidget(NonNegUI())
        self.kernel_constraint_stack.addWidget(UnitNormUI())
        self.kernel_constraint_stack.addWidget(MinMaxNormUI())



        self.bias_constraint = QComboBox()
        self.bias_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.bias_constraint.currentIndexChanged[int].connect(lambda index : self.bias_constraint_stack.setCurrentIndex(index))

        self.bias_constraint_stack = QStackedWidget()
        self.bias_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.bias_constraint_stack.addWidget(MaxNormUI())
        self.bias_constraint_stack.addWidget(NonNegUI())
        self.bias_constraint_stack.addWidget(UnitNormUI())
        self.bias_constraint_stack.addWidget(MinMaxNormUI())

        self.recurrent_constraint = QComboBox()
        self.recurrent_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.recurrent_constraint.currentIndexChanged[int].connect(lambda index : self.recurrent_constraint_stack.setCurrentIndex(index))

        self.recurrent_constraint_stack = QStackedWidget()
        self.recurrent_constraint_stack.setContentsMargins(0, 0, 0, 0)
        self.recurrent_constraint_stack.addWidget(MaxNormUI())
        self.recurrent_constraint_stack.addWidget(NonNegUI())
        self.recurrent_constraint_stack.addWidget(UnitNormUI())
        self.recurrent_constraint_stack.addWidget(MinMaxNormUI())

        self.dropout = QLineEdit("0")
        self.recurrent_dropout = QLineEdit("0")

        self.return_sequences = QComboBox()
        self.return_sequences.addItems(["False","True"])

        self.go_backwards = QComboBox()
        self.go_backwards.addItems(["False","True"])

        self.stateful = QComboBox()
        self.stateful.addItems(["False","True"])
        self.init_GUI()

    def init_GUI(self):
        
        self.main_layout = QFormLayout()
        self.main_layout.addRow(QLabel("filters: "),self.filters)
        self.main_layout.addRow(QLabel("kernel_size: "),self.kernel_size)
        self.main_layout.addRow(QLabel("strides: "),self.strides)
        self.main_layout.addRow(QLabel("padding: "),self.padding)
        self.main_layout.addRow(QLabel("data_format: "),self.data_format)
        self.main_layout.addRow(QLabel("dilation_rate: "),self.dilation_rate)
        self.main_layout.addRow(QLabel("activation: "),self.activation)

        self.main_layout.addRow(QLabel("recurrent_activation: "),self.recurrent_activation)
        self.main_layout.addRow(QLabel("use_bias: "),self.use_bias)

        self.main_layout.addRow(QLabel("kernel_initializer: "),self.kernel_initializer)
        self.main_layout.addWidget(self.kernel_initializer_stack)

        self.main_layout.addRow(QLabel("recurrent_initializer: "),self.recurrent_initializer)
        self.main_layout.addWidget(self.recurrent_initializer_stack)

        self.main_layout.addRow(QLabel("bias_initializer: "),self.bias_initializer)
        self.main_layout.addWidget(self.bias_initializer_stack)

        self.main_layout.addRow(QLabel("unit_forget_bias: "),self.unit_forget_bias)

        self.main_layout.addRow(QLabel("kernel_regularizer: "),self.kernel_regularizer)
        self.main_layout.addWidget(self.kernel_regularizer_stack)

        self.main_layout.addRow(QLabel("recurrent_regularizer: "),self.recurrent_regularizer)
        self.main_layout.addWidget(self.recurrent_regularizer_stack)

        self.main_layout.addRow(QLabel("bias_regularizer: "),self.bias_regularizer)
        self.main_layout.addWidget(self.bias_regularizer_stack)

        self.main_layout.addRow(QLabel("activity_regularizer: "),self.activity_regularizer)
        self.main_layout.addWidget(self.activity_regularizer_stack)

        self.main_layout.addRow(QLabel("kernel_constraint: "),self.kernel_constraint)
        self.main_layout.addWidget(self.kernel_constraint_stack)

        self.main_layout.addRow(QLabel("recurrent_constraint: "),self.recurrent_constraint)
        self.main_layout.addWidget(self.recurrent_constraint_stack)

        self.main_layout.addRow(QLabel("bias_constraint: "),self.bias_constraint)
        self.main_layout.addWidget(self.bias_constraint_stack)

        self.main_layout.addRow(QLabel("return_sequences: "),self.return_sequences)
        self.main_layout.addRow(QLabel("go_backwards: "),self.go_backwards)

       
        self.main_layout.addRow(QLabel("stateful: "),self.stateful)

        self.main_layout.addRow(QLabel("dropout: "),self.dropout)
        self.main_layout.addRow(QLabel("recurrent_dropout: "),self.recurrent_dropout)

        self.setLayout(self.main_layout)

#############################################################################

######################## Preprocessing layers ############################### 
'''
DONE
'''
class TextVectorizationLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.max_tokens = QLineEdit("None")
        self.standardize = QComboBox()
        self.standardize.addItems(["lower_and_strip_punctuation","None","Callable"])
        self.split = QComboBox()
        self.split.addItems(["whitespace","None","Callable"])
        self.ngrams = QLineEdit("None")
        self.output_mode = QComboBox()
        self.output_mode.addItems(["int","binary","count","tf-idf"])
        self.output_sequence_length = QLineEdit("None")
        self.pad_to_max_tokens = QComboBox()
        self.pad_to_max_tokens.addItems(["True","False"])
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(QLabel("max_tokens"),0,0)
        self.main_layout.addWidget(self.max_tokens,0,1)
        self.main_layout.addWidget(QLabel("standardize"),1,0)
        self.main_layout.addWidget(self.standardize,1,1)
        self.main_layout.addWidget(QLabel("split"),2,0)
        self.main_layout.addWidget(self.split,2,1)
        self.main_layout.addWidget(QLabel("ngrams"),3,0)
        self.main_layout.addWidget(self.ngrams,3,1)
        self.main_layout.addWidget(QLabel("output_mode"),4,0)
        self.main_layout.addWidget(self.output_mode,4,1)
        self.main_layout.addWidget(QLabel("output_sequence_length"),5,0)
        self.main_layout.addWidget(self.output_sequence_length,5,1)
        self.main_layout.addWidget(QLabel("pad_to_max_tokens"),6,0)
        self.main_layout.addWidget(self.pad_to_max_tokens,6,1)

    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class NormalizationLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.axis = QLineEdit("-1")
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("Axis:"))
        self.main_layout.addWidget(self.axis)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
#############################################################################

######################## Normalization layers ############################### 
'''
DONE
'''
class BatchNormalizationLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.axis = QLineEdit("-1")
        self.momentum = QLineEdit("0.99")
        self.epsilon = 0.001
        self.center = QComboBox()
        self.center.addItems(["True", "False"])
        self.scale = QComboBox()
        self.scale.addItems(["True", "False"])
        self.beta_initializer = QComboBox()
        self.beta_initializer.addItems(["zeroes", "ones"])
        self.gamma_initializer = QComboBox()
        self.gamma_initializer.addItems(["ones", "zeroes"])
        self.moving_mean_initializer = QComboBox()
        self.moving_mean_initializer.addItems(["zeroes", "ones"])
        self.moving_variance_initializer= QComboBox()
        self.moving_variance_initializer.addItems(["ones", "zeroes"])
        """
        beta_regularizer
        """
        self.beta_regularizer = QComboBox()
        self.beta_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.beta_regularizer.currentIndexChanged[int].connect(lambda index : self.beta_regularizer_stack.setCurrentIndex(index))

        self.beta_regularizer_stack = QStackedWidget()
        self.beta_regularizer_stack.addWidget(QLabel("None"))
        self.beta_regularizer_stack.addWidget(l1UI())
        self.beta_regularizer_stack.addWidget(l2UI())
        self.beta_regularizer_stack.addWidget(l1_l2UI())        

        """
        gamma_regularizer
        """
        self.gamma_regularizer = QComboBox()
        self.gamma_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.gamma_regularizer.currentIndexChanged[int].connect(lambda index : self.gamma_regularizer_stack.setCurrentIndex(index))

        self.gamma_regularizer_stack = QStackedWidget()
        self.gamma_regularizer_stack.addWidget(QLabel("None"))
        self.gamma_regularizer_stack.addWidget(l1UI())
        self.gamma_regularizer_stack.addWidget(l2UI())
        self.gamma_regularizer_stack.addWidget(l1_l2UI()) 

        """
        beta_constraint
        """
        self.beta_constraint = QComboBox()
        self.beta_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.beta_constraint.currentIndexChanged[int].connect(lambda index : self.beta_constraint_stack.setCurrentIndex(index))
        self.beta_constraint_stack = QStackedWidget()
        self.beta_constraint_stack.addWidget(QLabel("None"))
        self.beta_constraint_stack.addWidget(MaxNormUI())
        self.beta_constraint_stack.addWidget(NonNegUI())
        self.beta_constraint_stack.addWidget(UnitNormUI())
        self.beta_constraint_stack.addWidget(MinMaxNormUI())

        """
        gamma constraint
        """
        self.gamma_constraint = QComboBox()
        self.gamma_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.gamma_constraint.currentIndexChanged[int].connect(lambda index : self.gamma_constraint_stack.setCurrentIndex(index))
        self.gamma_constraint_stack = QStackedWidget()
        self.gamma_constraint_stack.addWidget(QLabel("None"))
        self.gamma_constraint_stack.addWidget(MaxNormUI())
        self.gamma_constraint_stack.addWidget(NonNegUI())
        self.gamma_constraint_stack.addWidget(UnitNormUI())
        self.gamma_constraint_stack.addWidget(MinMaxNormUI())  
        
        self.renorm = QComboBox()
        self.renorm.addItems(["False", "True"])
        self.renorm_clipping = QLineEdit("None")
        self.fused = QComboBox()
        self.renorm_momentum = QLineEdit("0.99")
        self.fused.addItems(["None", "True", "False"])
        self.trainable = QComboBox()
        self.trainable.addItems(["True", "False"])
        self.virtual_batch_size = QLineEdit("None")
        self.adjustment = QLineEdit("None")
        self.init_GUI()

    def init_GUI(self):
        '''
        Gearing up main layout
        '''
        self.main_layout.addWidget(QLabel("axis:"), 0 ,0)
        self.main_layout.addWidget(self.axis,0 , 1)
        self.main_layout.addWidget(QLabel("momentum:"), 1, 0)
        self.main_layout.addWidget(self.momentum, 1, 1)
        self.main_layout.addWidget(QLabel("Center:"),2 ,0)
        self.main_layout.addWidget(self.center, 2, 1)
        self.main_layout.addWidget(QLabel("Scale:"), 3, 0)
        self.main_layout.addWidget(self.scale, 3, 1)
        self.main_layout.addWidget(QLabel("beta_initializer"), 4, 0)
        self.main_layout.addWidget(self.beta_initializer, 4, 1)
        self.main_layout.addWidget(QLabel("gamma_initializer"), 5, 0)
        self.main_layout.addWidget(self.gamma_initializer, 5, 1)
        self.main_layout.addWidget(QLabel("moving_mean_initializer"), 6, 0)
        self.main_layout.addWidget(self.moving_mean_initializer, 6 , 1)
        self.main_layout.addWidget(QLabel("moving_variance_initializer"), 7, 0)
        self.main_layout.addWidget(self.moving_variance_initializer, 7 , 1)
        self.main_layout.addWidget(QLabel("beta_regularizer:"), 8 , 0)
        self.main_layout.addWidget(self.beta_regularizer, 8 , 1)
        self.main_layout.addWidget(self.beta_regularizer_stack, 9 , 1)
        self.main_layout.addWidget(QLabel("gamma_regularizer:"),10 , 0)
        self.main_layout.addWidget(self.gamma_regularizer, 10, 1)
        self.main_layout.addWidget(self.gamma_regularizer_stack, 11, 1)
        self.main_layout.addWidget(QLabel("beta_constraint:"), 12, 0)
        self.main_layout.addWidget(self.beta_constraint, 12 ,1)
        self.main_layout.addWidget(self.beta_constraint_stack, 13, 1)
        self.main_layout.addWidget(QLabel("gamma_constratint"), 13, 0)
        self.main_layout.addWidget(self.gamma_constraint, 13, 1)
        self.main_layout.addWidget(self.gamma_constraint_stack, 14 ,1)
        self.main_layout.addWidget(QLabel("renorm:"), 15, 0)
        self.main_layout.addWidget(self.renorm, 15 ,1)
        self.main_layout.addWidget(QLabel("renorm_clipping"), 16, 0)
        self.main_layout.addWidget(self.renorm_clipping, 16 , 1)
        self.main_layout.addWidget(QLabel("renorm_momentum"), 17, 0)
        self.main_layout.addWidget(self.renorm_momentum, 17,1)
        self.main_layout.addWidget(QLabel("Fused:"), 18, 0)
        self.main_layout.addWidget(self.fused, 18 , 1)
        self.main_layout.addWidget(QLabel("Trainable:"), 19, 0)
        self.main_layout.addWidget(self.trainable, 19 , 1)
        self.main_layout.addWidget(QLabel("virtual_batch_size:"), 20, 0)
        self.main_layout.addWidget(self.virtual_batch_size, 20, 1)
        self.main_layout.addWidget(QLabel("Adjustment:"), 21, 0)
        self.main_layout.addWidget(self.adjustment, 21, 1)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass
        
class LayerNormalizationLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.axis = QLineEdit("-1")
        self.epsilon = QLineEdit("0.01")
        self.center = QComboBox()
        self.center.addItems(["True","False"])
        self.scale = QComboBox()
        self.scale.addItems(["True","False"])

        self.beta_initializer = QComboBox()
        self.beta_initializer.addItems([
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Orthogonal",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "glorot_uniform",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.beta_initializer.currentIndexChanged[int].connect(lambda index: self.beta_stack.setCurrentIndex(index))
    

        self.beta_stack = QStackedWidget()
        self.beta_stack.addWidget(RandomUniformUI())
        self.beta_stack.addWidget(ZerosUI())
        self.beta_stack.addWidget(OnesUI())
        self.beta_stack.addWidget(ConstantUI())
        self.beta_stack.addWidget(RandomNormalUI())
        self.beta_stack.addWidget(TruncatedNormalUI())
        self.beta_stack.addWidget(VarianceScalingUI())
        self.beta_stack.addWidget(OrthogonalUI())
        self.beta_stack.addWidget(IdentityUI())
        self.beta_stack.addWidget(lecunUniformUI())
        self.beta_stack.addWidget(glorotNormalUI())
        self.beta_stack.addWidget(glorotUniformUI())
        self.beta_stack.addWidget(heNormalUI())
        self.beta_stack.addWidget(lecunNormalUI())
        self.beta_stack.addWidget(heUniformUI())
        """
        gamma_initializer
        """
        self.gamma_initializer = QComboBox()
        self.gamma_initializer.addItems([
            "RandomUniform",
            "Zeros",
            "Ones",
            "Constant",
            "RandomNormal",
            "TruncatedNormal",
            "VarianceScaling",
            "Orthogonal",
            "Identity",
            "lecun_uniform",
            "glorot_normal",
            "glorot_uniform",
            "he_normal",
            "lecun_normal",
            "he_uniform",
            "CUSTOM_my1"])
        self.gamma_initializer.currentIndexChanged[int].connect(lambda index: self.gamma_stack.setCurrentIndex(index))
    

        self.gamma_stack = QStackedWidget()
        self.gamma_stack.addWidget(RandomUniformUI())
        self.gamma_stack.addWidget(ZerosUI())
        self.gamma_stack.addWidget(OnesUI())
        self.gamma_stack.addWidget(ConstantUI())
        self.gamma_stack.addWidget(RandomNormalUI())
        self.gamma_stack.addWidget(TruncatedNormalUI())
        self.gamma_stack.addWidget(VarianceScalingUI())
        self.gamma_stack.addWidget(OrthogonalUI())
        self.gamma_stack.addWidget(IdentityUI())
        self.gamma_stack.addWidget(lecunUniformUI())
        self.gamma_stack.addWidget(glorotNormalUI())
        self.gamma_stack.addWidget(glorotUniformUI())
        self.gamma_stack.addWidget(heNormalUI())
        self.gamma_stack.addWidget(lecunNormalUI())
        self.gamma_stack.addWidget(heUniformUI())

        """
        beta_regularizer
        """
        self.beta_regularizer = QComboBox()
        self.beta_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.beta_regularizer.currentIndexChanged[int].connect(lambda index : self.beta_regularizer_stack.setCurrentIndex(index))

        self.beta_regularizer_stack = QStackedWidget()
        self.beta_regularizer_stack.addWidget(QLabel("None"))
        self.beta_regularizer_stack.addWidget(l1UI())
        self.beta_regularizer_stack.addWidget(l2UI())
        self.beta_regularizer_stack.addWidget(l1_l2UI())        

        """
        gamma_regularizer
        """
        self.gamma_regularizer = QComboBox()
        self.gamma_regularizer.addItems(["None","l1","l2","l1_l2"])
        self.gamma_regularizer.currentIndexChanged[int].connect(lambda index : self.gamma_regularizer_stack.setCurrentIndex(index))

        self.gamma_regularizer_stack = QStackedWidget()
        self.gamma_regularizer_stack.addWidget(QLabel("None"))
        self.gamma_regularizer_stack.addWidget(l1UI())
        self.gamma_regularizer_stack.addWidget(l2UI())
        self.gamma_regularizer_stack.addWidget(l1_l2UI()) 

        """
        beta_constraint
        """
        self.beta_constraint = QComboBox()
        self.beta_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.beta_constraint.currentIndexChanged[int].connect(lambda index : self.beta_constraint_stack.setCurrentIndex(index))
        self.beta_constraint_stack = QStackedWidget()
        self.beta_constraint_stack.addWidget(QLabel("None"))
        self.beta_constraint_stack.addWidget(MaxNormUI())
        self.beta_constraint_stack.addWidget(NonNegUI())
        self.beta_constraint_stack.addWidget(UnitNormUI())
        self.beta_constraint_stack.addWidget(MinMaxNormUI())

        """
        gamma constraint
        """
        self.gamma_constraint = QComboBox()
        self.gamma_constraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.gamma_constraint.currentIndexChanged[int].connect(lambda index : self.gamma_constraint_stack.setCurrentIndex(index))
        self.gamma_constraint_stack = QStackedWidget()
        self.gamma_constraint_stack.addWidget(QLabel("None"))
        self.gamma_constraint_stack.addWidget(MaxNormUI())
        self.gamma_constraint_stack.addWidget(NonNegUI())
        self.gamma_constraint_stack.addWidget(UnitNormUI())
        self.gamma_constraint_stack.addWidget(MinMaxNormUI())

        """
        trainable
        """
        self.trainable = QComboBox()
        self.trainable.addItems(["True","False"])
        self.init_GUI()
        

    def init_GUI(self):
        """
        main_layout

        """
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(QLabel("axis:"),0,0)
        self.main_layout.addWidget(self.axis,0,1)

        self.main_layout.addWidget(QLabel("epsilon:"),1,0)
        self.main_layout.addWidget(self.epsilon,1,1)

        self.main_layout.addWidget(QLabel("center:"),2,0)
        self.main_layout.addWidget(self.center,2,1)

        self.main_layout.addWidget(QLabel("scale:"),3,0)
        self.main_layout.addWidget(self.scale,3,1)

        self.main_layout.addWidget(QLabel("beta_initializer:"),4,0)
        self.main_layout.addWidget(self.beta_initializer,4,1)
        self.main_layout.addWidget(self.beta_stack,5,1)

        self.main_layout.addWidget(QLabel("gamma_initializer:"),6,0)
        self.main_layout.addWidget(self.gamma_initializer,6,1)
        self.main_layout.addWidget(self.gamma_stack,7,1)

        self.main_layout.addWidget(QLabel("beta_regularizer"),8,0)
        self.main_layout.addWidget(self.beta_regularizer,8,1)
        self.main_layout.addWidget(self.beta_regularizer_stack,9,1)

        self.main_layout.addWidget(QLabel("gamma_regularizer"),10,0)
        self.main_layout.addWidget(self.gamma_regularizer,10,1)
        self.main_layout.addWidget(self.gamma_regularizer_stack,11,1)

        self.main_layout.addWidget(QLabel("beta_constraint"),12,0)
        self.main_layout.addWidget(self.beta_constraint,12,1)
        self.main_layout.addWidget(self.beta_constraint_stack,13,1)

        self.main_layout.addWidget(QLabel("gamma_constraint"),14,0)
        self.main_layout.addWidget(self.gamma_constraint,14,1)
        self.main_layout.addWidget(self.gamma_constraint_stack,15,1)

        self.main_layout.addWidget(QLabel("trainable:"),16,0)
        self.main_layout.addWidget(self.trainable,16,1)

        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")

    def parse_arguments(self):
        pass
    
##############################################################################

######################## Regularization layers ###############################   
'''
DONE
'''
class DropoutLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.rate = QLineEdit("0")
        self.seed = QLineEdit("0")
        self.rate.setValidator(QDoubleValidator(0.,1.,2))
        self.init_GUI()

    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(QLabel("rate"), 0, 0)
        self.main_layout.addWidget(self.rate, 0, 1)
        
        self.main_layout.addWidget(QLabel("seed"), 1, 0)
        self.main_layout.addWidget(self.seed, 1, 1)
        self.setLayout(self.main_layout)
        self.set_styling()        
    
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass

class SpatialDropout1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.rate = QLineEdit("0.0")
        self.init_GUI()
    
    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(QLabel("Rate:"), 0, 0)
        self.main_layout.addWidget(self.rate, 0 ,1)
        self.setLayout(self.main_layout)
        self.set_styling()
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
        
class SpatialDropout2DLayerControlWidget(SpatialDropout1DLayerControlWidget):
    def __init__(self):
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last", "channels_first"])
        super().__init__()
    
    def init_GUI(self):
        super().init_GUI()
        self.main_layout.addWidget(QLabel("data_format:"), 1, 0)
        self.main_layout.addWidget(self.data_format, 1 ,1)
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class SpatialDropout3DLayerControlWidget(SpatialDropout2DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class GaussianDropoutLayerControlWidget(SpatialDropout1DLayerControlWidget):
    def __init__(self):
        super().__init__()

    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
            
class GaussianNoiseLayerControlWidget(QWidget):
    def __init__(self):
        self.stddev = QLineEdit("0.0")
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("stddev:"))
        self.main_layout.addWidget(self.stddev)
        self.setLayout(self.main_layout)
        self.set_styling()
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class ActivityRegularizationLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.l1 = QLineEdit("0.0")
        self.l2 = QLineEdit("0.0")
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(QLabel("l1"), 0, 0)
        self.main_layout.addWidget(self.l1, 0, 1)
        self.main_layout.addWidget(QLabel("l2"), 1, 0)
        self.main_layout.addWidget(self.l2, 1, 1)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
            
class AlphaDropoutLayerControlWidget(QWidget):
    def __init__(self):
        self.rate = QLineEdit("0.0")
        self.rate.setValidator(QDoubleValidator(0. , 1e6, 3))
        self.seed = QLineEdit("0")
        self.init_GUI()

    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(QLabel("Rate:"), 0, 0)
        self.main_layout.addWidget(self.rate, 0, 1)
        self.main_layout.addWidget(QLabel("Seed:"), 1, 0)
        self.main_layout.addWidget(self.seed, 1, 1)
        self.setLayout(self.main_layout)
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass        
    
#############################################################################

######################## Attention layers ################################### 

class AttentionLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.use_scale = QComboBox()
        self.use_scale.addItems(["False","True"])
        self.casual = QComboBox()
        self.casual.addItems(["True","False"])
        self.dropout = QLineEdit("0.")
        self.init_GUI()
    def init_GUI(self):

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(QLabel("use_scale: "),0,0)
        self.main_layout.addWidget(self.use_scale,0,1)
        self.main_layout.addWidget(QLabel("casual: "),1,0)
        self.main_layout.addWidget(self.casual,1,1)
        self.main_layout.addWidget(QLabel("dropout: "),2,0)
        self.main_layout.addWidget(self.dropout,2,1)
        self.setLayout(self.main_layout)

class AdditiveAttentionLayerControlWidget(AttentionLayerControlWidget):
    def __init__(self):
        super().__init__()

#############################################################################

######################## Reshaping layers ################################### 
'''
DONE
'''
class ReshapeLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.target_shape = QLineEdit("(0,0)")
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QFormLayout()
        self.main_layout.addRow(QLabel("target_shape"),self.target_shape)
        self.setLayout(self.main_layout)
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass

class FlattenLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last","channels_first"])
        self.init_GUI()

    def init_GUI(self):
        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addRow(QLabel("data_format"),self.data_format)
        self.setLayout(self.main_layout)
        self.set_styling()        

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
        
    def parse_arguments(self):
        pass

class RepeatVectorLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.n = QLineEdit("1")
        self.init_GUI()

    def init_GUI(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("n : "))
        self.main_layout.addWidget(self.n)
        self.set_styling(self)
        self.setLayout(self.main_layout)
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class PermuteLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.permute = QLineEdit("1")
        self.init_GUI()

    def init_GUI(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("Pattern: "))
        self.main_layout.addWidget(self.permute)
        self.set_styling(self)
        self.setLayout(self.main_layout)
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
    
class Cropping1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.cropping = QLineEdit("(1, 1)")
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(QLabel("Cropping:"),0 , 0)
        self.main_layout.addWidget(self.cropping, 0 ,1)
        self.setLayout(self.main_layout)
        self.set_styling()

    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass    

class Cropping2DLayerControlWidget(Cropping1DLayerControlWidget):
    def __init__(self):
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last", "channels_first"])
        super().__init__()

        
    def init_GUI(self):
        super().init_GUI()
        self.main_layout.addWidget(QLabel("data_format:"),1 , 0)
        self.main_layout.addWidget(self.data_format, 1 ,1)
        self.setLayout(self.main_layout)
        self.set_styling()

    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass
        
class Cropping3DLayerControlWidget(Cropping2DLayerControlWidget):
    def __init__(self):
        super().__init__()

    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass    
    
class ZeroPadding1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.padding = QLineEdit("1")
        self.init_GUI()
    def init_GUI(self):
        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addRow(QLabel("padding: "),self.padding)
        self.setLayout(self.main_layout)

class ZeroPadding2DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.padding = QLineEdit("1")
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last","channels_first"])
        self.init_GUI()

    def init_GUI(self):
        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addRow(QLabel("padding: "),self.padding)
        self.main_layout.addRow(QLabel("data_format"),self.data_format)
        self.setLayout(self.main_layout)
    
class ZeroPadding3DLayerControlWidget(ZeroPadding2DLayerControlWidget):
    def __init__(self):
        super().__init__()
        self.padding.setText("(2,2,2)")

class UpSampling1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.size = QLineEdit("2")
        self.init_GUI()
    def init_GUI(self):
        
        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addRow(QLabel("size: "),self.size)
        self.setLayout(self.main_layout)

class UpSampling2DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.size = QLineEdit("(2,2)")

        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last","channels_first"])

        self.interpolation = QComboBox()
        self.interpolation.addItems(["nearest","bilinear"])
        self.init_GUI()
    def init_GUI(self):
        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addRow(QLabel("size: "),self.size)
        self.main_layout.addRow(QLabel("data_format: "),self.data_format)
        self.main_layout.addRow(QLabel("interpolation: "),self.interpolation)
        self.setLayout(self.main_layout)

class UpSampling3DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.size = QLineEdit("(2,2,2)")

        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last","channels_first"])
        self.init_GUI()

    def init_GUI(self):
        self.main_layout = QFormLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addRow(QLabel("size: "),self.size)
        self.main_layout.addRow(QLabel("data_format: "),self.data_format)
        self.setLayout(self.main_layout)
        
class ZeroPadding1DLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.padding = QLineEdit("1")
        self.init_GUI()
        
    def init_GUI(self):
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("Padding:"))
        self.main_layout.addWidget(self.padding)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass

class ZeroPadding2DLayerControlWidget(ZeroPadding1DLayerControlWidget):
    def __init__(self):
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_first", "channels_last"])
        super().__init__()
        
    def init_GUI(self):
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(QLabel("Padding:"), 0, 0)
        self.main_layout.addWidget(self.padding, 0, 1)
        self.main_layout.addWidget(QLabel("data_format:"), 1, 0)
        self.main_layout.addWidget(self.data_format, 1, 1)
        self.setLayout(self.main_layout)
        self.set_styling()        
    
    def parse_arguments(self):
        pass

class ZeroPadding3DLayerControlWidget(ZeroPadding2DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def parse_arguments(self):
        pass

#############################################################################

######################## Merging layers #################################### 
'''
I think no need to make layer control for mergings.
Can be supported inbuilt in drag and drop
'''
#############################################################################

######################## Locally-connected layers ########################### 
'''
DONE
'''
class LocallyConnected1DLayerControlWidget(Conv1DLayerControlWidget):
    def __init__(self):
        self.implementation = QComboBox()
        self.implementation.addItems(["1", "2", "3"])  
        super().__init__()
    
    def init_GUI(self):
        """
        Gearup main layout
        """
        self.main_layout.addWidget(QLabel("Filters:"), 0, 0)
        self.main_layout.addWidget(self.filters, 0 , 1)
        self.main_layout.addWidget(QLabel("Kernal Size:"), 1, 0)
        self.main_layout.addWidget(self.kernal_size, 1, 1)
        self.main_layout.addWidget(QLabel("Strides:"), 2, 0)
        self.main_layout.addWidget(self.strides, 2 ,1)
        self.main_layout.addWidget(QLabel("Padding:"), 3, 0)
        self.main_layout.addWidget(self.padding, 3, 1)
        self.main_layout.addWidget(QLabel("Data Format:"), 4, 0)
        self.main_layout.addWidget(self.data_format, 4 ,1)
        self.main_layout.addWidget(QLabel("implementation:"), 5, 0)
        self.main_layout.addWidget(self.implementation, 5, 1)
        self.main_layout.addWidget(QLabel("Activation"), 6, 0)
        self.main_layout.addWidget(self.activation, 6 ,1)
        self.main_layout.addWidget(QLabel("Use Bias:"), 7 , 0)
        self.main_layout.addWidget(self.use_bias, 7, 1)
        
        self.main_layout.addWidget(QLabel("kernelInitializer"),8,0)
        self.main_layout.addWidget(self.kernel_initializer,8,1)
        self.main_layout.addWidget(self.kernel_initializer_stack,9,1)

        self.main_layout.addWidget(QLabel("Bias Initializer"),9,0)
        self.main_layout.addWidget(self.bias_initializer,9,1)
        self.main_layout.addWidget(self.bias_initializer_stack,10,1)

        self.main_layout.addWidget(QLabel("kernel_regularizer"),11,0)
        self.main_layout.addWidget(self.kernel_regularizer,11,1)
        self.main_layout.addLayout(self.kernel_regularizer_stack,12,1)

        self.main_layout.addWidget(QLabel("bias_regularizer"),13,0)
        self.main_layout.addWidget(self.bias_regularizer,13,1)
        self.main_layout.addLayout(self.bias_regularizer_stack,14,1)

        self.main_layout.addWidget(QLabel("activity_regularizer"),15,0)
        self.main_layout.addWidget(self.activity_regularizer,15,1)
        self.main_layout.addLayout(self.activity_regularizer_stack,16,1)

        self.main_layout.addWidget(QLabel("kernel_constraint"),17,0)
        self.main_layout.addWidget(self.kernel_constraint,17,1)
        self.main_layout.addWidget(self.kernel_constraint_stack,18,1)

        self.main_layout.addWidget(QLabel("bias_constraint"),19,0)
        self.main_layout.addWidget(self.bias_constraint,19,1)
        self.main_layout.addWidget(self.bias_constraint_stack,20,1)
        
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass 
    
class LocallyConnected2DLayerControlWidget(LocallyConnected1DLayerControlWidget):
    def __init__(self):
        super().__init__()
    
    def set_styling(self):
        pass
    
    def parse_arguments(self):
        pass               
        
#############################################################################


class RandomUniformUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.minval = QLineEdit("-0.05")
        self.maxval = QLineEdit("0.05")
        self.seed = QLineEdit("None")        
        
        self.main_layout.addWidget(QLabel("Minval"),0,0)
        self.main_layout.addWidget(self.minval,0,1)
        self.main_layout.addWidget(QLabel("Maxval"),1,0)
        self.main_layout.addWidget(self.maxval,1,1)
        self.main_layout.addWidget(QLabel("Seed"),2,0)
        self.main_layout.addWidget(self.seed,2,1)
        self.setLayout(self.main_layout)
        
    def get_initializer(self):
        return None
            
"""
Zeros class provide UI of zeros

"""

class ZerosUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("Initializer that generates tensors initialized to 0."))
        self.setLayout(self.main_layout)

    def get_initializer(self):
        return None
"""
class of ones which provide UI ones
"""
class OnesUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("Initializer that generates tensors initialized to 1."))
        self.setLayout(self.main_layout)

    def get_initializer(self):
        return None
"""
class of constant which provide UI of Constant
"""

class ConstantUI(QWidget):
    def __init__(self):
        super().__init__()
        self.const_value = QLineEdit("0")
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(QLabel("value:"), 0, 0)
        self.main_layout.addWidget(self.const_value, 0, 1)
        self.setLayout(self.main_layout)
    
    def get_initializer(self):
        return None
    
"""
class of random normal which provide UI of random normal
"""
class RandomNormalUI(QWidget):
    def __init__(self):
        super().__init__()
        self.mean = QLineEdit("0.0")
        self.stddev = QLineEdit("0.05")
        self.seed = QLineEdit("None")
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("mean"),0,0)
        self.main_layout.addWidget(self.mean,0,1)
        self.main_layout.addWidget(QLabel("stddev"),1,0)
        self.main_layout.addWidget(self.stddev,1,1)
        self.main_layout.addWidget(QLabel("seed"),2,0)
        self.main_layout.addWidget(self.seed,2,1)
        self.setLayout(self.main_layout)
        
    def get_initializer(self):
        return None

"""
class of Truncated normal which provide UI of truncated_normal
"""
class TruncatedNormalUI(QWidget):
    def __init__(self):
        super().__init__()
        self.TruncatedNormal_mean = QLineEdit("0.0")
        self.TruncatedNormal_stddev = QLineEdit("0.05")
        self.TruncatedNormal_seed = QLineEdit("None")
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("mean"),0,0)
        self.main_layout.addWidget(self.TruncatedNormal_mean,0,1)
        self.main_layout.addWidget(QLabel("stddev"),1,0)
        self.main_layout.addWidget(self.TruncatedNormal_stddev,1,1)
        self.main_layout.addWidget(QLabel("seed"),2,0)
        self.main_layout.addWidget(self.TruncatedNormal_seed,2,1)
        self.setLayout(self.main_layout)
        
    def get_initializer(self):
        return None

"""
class of Variance Scaling which provide UI of variance_scaling
"""

class VarianceScalingUI(QWidget):
    def __init__(self):
        super().__init__()
        self.scale = QLineEdit("1.0")
        self.mode = QComboBox()
        self.mode.addItems(["fan_in","fan_out","fan_avg"])
        self.distribution = QComboBox()
        self.distribution.addItems(["normal","uniform"])
        self.seed = QLineEdit("None")
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("scale"),0,0)
        self.main_layout.addWidget(self.scale,0,1)
        self.main_layout.addWidget(QLabel("mode"),1,0)
        self.main_layout.addWidget(self.mode,1,1)
        self.main_layout.addWidget(QLabel("distribution"),2,0)
        self.main_layout.addWidget(self.distribution,2,1)
        self.main_layout.addWidget(QLabel("seed"),3,0)
        self.main_layout.addWidget(self.seed,3,1)
        self.setLayout(self.main_layout)
        
    def get_initializer(self):
        return None
"""
class of orthogonal which provide UI of orthogonal
"""

class OrthogonalUI(QWidget):
    def __init__(self):
        super().__init__()
        self.gain = QLineEdit("1.0")
        self.seed = QLineEdit("None")
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("gain"),0,0)
        self.main_layout.addWidget(self.gain,0,1)
        self.main_layout.addWidget(QLabel("seed"),1,0)
        self.main_layout.addWidget(self.seed,1,1)
        self.setLayout(self.main_layout)
        
    def get_initializer(self):
        return None
"""
class of identity which provide UI of Identity
"""
class IdentityUI(QWidget):
    def __init__(self):
        super().__init__()
        self.gain = QLineEdit("1.0")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("gain"), 0, 0)
        self.main_layout.addWidget(self.gain,0,1)
        self.setLayout(self.main_layout)
    
    def get_initializer(self):
        return None
"""
class of lecun uniform which provide UI of lecun_uniform
"""

class lecunUniformUI(QWidget):
    def __init__(self):
        super().__init__()
        self.seed = QLineEdit("None")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("seed"),0,0)
        self.main_layout.addWidget(self.seed,0,1)
        self.setLayout(self.main_layout)
        
    def get_initializer(self):
        return None
"""
class of glorot normal which provide UI of glorot_normal
"""
class glorotNormalUI(QWidget):
    def __init__(self):
        super().__init__()
        self.seed = QLineEdit("None")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("seed"),0,0)
        self.main_layout.addWidget(self.seed,0,1)
        self.setLayout(self.main_layout)
       
    def get_initializer(self):
        return None
"""
class of glorot uniform which provide UI of glorot uniform
"""

class glorotUniformUI(QWidget):
    def __init__(self):
        super().__init__()
        self.seed = QLineEdit("None")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("seed"),0,0)
        self.main_layout.addWidget(self.seed,0,1)
        self.setLayout(self.main_layout)
        
    def get_initializer(self):
        return None
"""
class of henormal which provide UI of he_normal
"""
    
class heNormalUI(QWidget):
    def __init__(self):
        super().__init__()
        self.seed = QLineEdit("None")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("seed"),0,0)
        self.main_layout.addWidget(self.seed,0,1)
        self.setLayout(self.main_layout)

    def get_initializer(self):
        return None
    
"""
class of lecun normal which provide UI of lecun_normal
"""
class lecunNormalUI(QWidget):
    def __init__(self):
        super().__init__()
        self.lecun_normal_seed = QLineEdit("None")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("seed"),0,0)
        self.main_layout.addWidget(self.lecun_normal_seed,0,1)
        self.setLayout(self.main_layout)
        
    def get_initializer(self):
        return None
"""
class of he uniform which provide UI of he_uniform
"""

class heUniformUI(QWidget):
    def __init__(self):
        super().__init__()
        self.he_uniform_seed = QLineEdit("None")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("seed"),0,0)
        self.main_layout.addWidget(self.he_uniform_seed,0,1)
        self.setLayout(self.main_layout)

    def get_initializer(self):
        return None
"""
class of l1 which provide UI of l1
"""

class l1UI(QWidget):
    def __init__(self):
        super().__init__()
        self.l1 = QLineEdit("0.")
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("value"),0,0)
        self.main_layout.addWidget(self.l1,0,1)
        self.setLayout(self.main_layout)
        
    def get_regularizer(self):
        return None
"""
class of l2 which provide UI of l2
"""
class l2UI(QWidget):
    def __init__(self):
        super().__init__()
        self.l2 = QLineEdit("0.")
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("value"),0,0)
        self.main_layout.addWidget(self.l2,0,1)
        self.setLayout(self.main_layout)
        
    def get_regularizer(self):
        return None
"""
class of l1_l2 which provide UI of l1_l2
"""
class l1_l2UI(QWidget):
    def __init__(self):
        super().__init__()
        self.l1 = QLineEdit("0.01")
        self.l2 = QLineEdit("0.01")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("l1"),0,0)
        self.main_layout.addWidget(self.l1,0,1)
        self.main_layout.addWidget(QLabel("l2"),1,0)
        self.main_layout.addWidget(self.l2,1,1)
        self.setLayout(self.main_layout)
        
    def get_regularizer(self):
        return None
"""
class of max norm which provide UI of max_morm
"""

class MaxNormUI(QWidget):
    def __init__(self):
        super().__init__()
        self.max_value = QLineEdit("2")
        self.axis = QLineEdit("0")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("max_value"),0,0)
        self.main_layout.addWidget(self.max_value,0,1)
        self.main_layout.addWidget(QLabel("axis"),1,0)
        self.main_layout.addWidget(self.axis,1,1)
        self.setLayout(self.main_layout)
        
    def get_regularizer(self):
        return None
"""
class of non neg which provide UI of non_neg
"""
class NonNegUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(QLabel("Constrains the weights to be non-negative."))
        self.setLayout(self.main_layout)
        
    def get_regularizer(self):
        return None
"""
class of unit norm which provide UI of unit_norm
"""
class UnitNormUI(QWidget):
    def __init__(self):
        super().__init__()
        self.axis_UnitNorm = QLineEdit("0")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("axis"),0,0)
        self.main_layout.addWidget(self.axis_UnitNorm,0,1)
        self.setLayout(self.main_layout)
        
    def get_regularizer(self):
        return None
"""
class of min max norm which provide UI of max_norm
"""
class MinMaxNormUI(QWidget):
    def __init__(self):
        super().__init__()
        self.min_vale = QLineEdit("0.0")
        self.max_value = QLineEdit("1.0")
        self.rate = QLineEdit("1.0")
        self.axis = QLineEdit("0")

        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(QLabel("min_value"),0,0)
        self.main_layout.addWidget(self.min_vale,0,1)
        self.main_layout.addWidget(QLabel("max_value"),1,0)
        self.main_layout.addWidget(self.max_value,1,1)
        self.main_layout.addWidget(QLabel("rate"),2,0)
        self.main_layout.addWidget(self.rate,2,1)
        self.main_layout.addWidget(QLabel("axis"),3,0)
        self.main_layout.addWidget(self.axis,3,1)
        self.setLayout(self.main_layout)
        
    def get_regularizer(self):  
        return None
