'''
TODO
# Add proper scaling, arrangement, styling
# optimize code
'''
#from tensorflow import keras
#from keras import layers, Sequential
from PySide2.QtCore import *
from PySide2.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QApplication, QLineEdit, QGridLayout, QLabel, QPushButton, QComboBox, QHBoxLayout, QStackedWidget,QStackedLayout,QStackedWidget,  QScrollBar, QScrollArea, QVBoxLayout, QFormLayout
from PySide2.QtGui import *
import sys
"""
Random uniform class provide UI of random Uniform

"""
######################## Core layers ############################### 

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
        '''
        self.scroll_panel = QWidget()
        self.scroll_panel_layout = QGridLayout(self.scroll_panel)
        self.scroll_panel_layout.setContentsMargins(0,0,0,0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.scroll_panel)

        self.vbox = QVBoxLayout(self)
        self.vbox.setContentsMargins(5,5,5,5)
        self.vbox.addWidget(self.scroll_area)
        self.scroll_panel_layout.addLayout(self.main_layout,0,0)
        self.set_styling()
        '''

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

#############################################################################

######################## Convolution layers #################################   
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
       
class Conv2DTransposeLayerControlWidget(Conv1DLayerControlWidget):
    def __init__(self):
        super().__init__()
        self.output_padding = QLineEdit("None")
        self.main_layout.addWidget(QLabel("Output Padding"), 21, 0)
        self.main_layout.addWidget(self.output_padding, 21, 1)
    
    def parse_arguments(self):
        pass    

class Conv3DTransposeLayerControlWidget(Conv2DTransposeLayerControlWidget):
    def __init__(self):
        super().__init__()
    
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

        """
        name
        """
        self.name = QLineEdit("None")

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

        self.main_layout.addWidget(QLabel("Name:"),17,0)
        self.main_layout.addWidget(self.name,17,1)


        self.setLayout(self.main_layout)

        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
##############################################################################

######################## Regularization layers ###############################   
class DropoutLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.rate = QLineEdit("0")
        self.rate.setValidator(QDoubleValidator(0.,1.,2))
        self.main_layout.addWidget(QLabel("rate"), 0, 0)
        self.main_layout.addWidget(self.rate, 0, 1)
        self.seed = QLineEdit("0")
        self.main_layout.addWidget(QLabel("seed"), 1, 0)
        self.main_layout.addWidget(self.seed, 1, 1)
        self.setLayout(self.main_layout)
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
    
    def parse_arguments(self):
        pass
    
#############################################################################

######################## Reshaping layers ################################### 

class ReshapeLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.target_shape = QLineEdit("(0,0)")
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