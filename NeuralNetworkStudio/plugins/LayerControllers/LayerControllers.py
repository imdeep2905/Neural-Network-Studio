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
        self.kernel_initializer.currentIndexChanged[int].connect(lambda index: self.kernal_stack.setCurrentIndex(index))
    

        self.kernal_stack = QStackedWidget()
        self.kernal_stack.addWidget(RandomUniformUI())
        self.kernal_stack.addWidget(ZerosUI())
        self.kernal_stack.addWidget(OnesUI())
        self.kernal_stack.addWidget(ConstantUI())
        self.kernal_stack.addWidget(RandomNormalUI())
        self.kernal_stack.addWidget(TruncatedNormalUI())
        self.kernal_stack.addWidget(VarianceScalingUI())
        self.kernal_stack.addWidget(OrthogonalUI())
        self.kernal_stack.addWidget(IdentityUI())
        self.kernal_stack.addWidget(lecunUniformUI())
        self.kernal_stack.addWidget(glorotNormalUI())
        self.kernal_stack.addWidget(glorotUniformUI())
        self.kernal_stack.addWidget(heNormalUI())
        self.kernal_stack.addWidget(lecunNormalUI())
        self.kernal_stack.addWidget(heUniformUI())

        """
        Batch Initializer

        """
        self.batch_initializer = QComboBox()
        self.batch_initializer.addItems(["RandomUniform",
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
        self.batch_initializer.currentIndexChanged[int].connect(lambda index : self.batch_initializer_stack.setCurrentIndex(index))
        self.batch_initializer_stack = QStackedWidget()
        self.batch_initializer_stack.addWidget(RandomUniformUI())
        self.batch_initializer_stack.addWidget(ZerosUI())
        self.batch_initializer_stack.addWidget(OnesUI())
        self.batch_initializer_stack.addWidget(ConstantUI())
        self.batch_initializer_stack.addWidget(RandomNormalUI())
        self.batch_initializer_stack.addWidget(TruncatedNormalUI())
        self.batch_initializer_stack.addWidget(VarianceScalingUI())
        self.batch_initializer_stack.addWidget(OrthogonalUI())
        self.batch_initializer_stack.addWidget(IdentityUI())
        self.batch_initializer_stack.addWidget(lecunUniformUI())
        self.batch_initializer_stack.addWidget(glorotNormalUI())
        self.batch_initializer_stack.addWidget(glorotUniformUI())
        self.batch_initializer_stack.addWidget(heNormalUI())
        self.batch_initializer_stack.addWidget(lecunNormalUI())
        self.batch_initializer_stack.addWidget(heUniformUI())
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
        self.main_layout.addWidget(self.kernal_stack,4,1)

        self.main_layout.addWidget(QLabel("Batch Initializer"),5,0)
        self.main_layout.addWidget(self.batch_initializer,5,1)
        self.main_layout.addWidget(self.batch_initializer_stack,6,1)

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

class DropoutLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
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

class FlattenLayerControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.data_format = QComboBox()
        self.data_format.addItems(["channels_last","channels_first"])
        self.main_layout = QFormLayout()
        self.main_layout.addRow(QLabel("data_format"),self.data_format)
        self.setLayout(self.main_layout)
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
        
    def parse_arguments(self):
        pass

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