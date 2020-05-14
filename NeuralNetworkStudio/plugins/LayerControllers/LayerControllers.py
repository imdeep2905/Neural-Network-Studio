'''
TODO
# Add proper scaling, arrangement, styling
# optimize code
'''
#from tensorflow import keras
#from keras import layers, Sequential
from PySide2.QtCore import *
from PySide2.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QApplication, QLineEdit, QGridLayout, QLabel, QPushButton, QComboBox, QHBoxLayout, QStackedWidget,QStackedLayout,QStackedWidget,  QScrollBar, QScrollArea, QVBoxLayout
from PySide2.QtGui import *
import sys
"""
Random uniform class provide UI of random Uniform

"""
class DenseLayerControlWidget(QWidget):
    def __init__(self, parent=None):
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
            "softplus"])
        
        self.useBias = QComboBox()
        self.useBias.addItems(["True","False"])

        """
        Kernel Initializer

        """
        self.RandomUniform = RandomUniformUI()
        self.Zeros = ZerosUI()
        self.Ones = OnesUI()
        self.Constant = ConstantUI()
        self.RandomNormal = RandomNormalUI()
        self.TruncatedNormal = TruncatedNormalUI()
        self.VarianceScaling = VarianceScalingUI()
        self.Orthogonal = OrthogonalUI()
        self.Identity = IdentityUI()
        self.lecun_uniform = lecunUniformUI()
        self.glorot_normal = glorotNormalUI()
        self.glorot_uniform = glorotUniformUI()
        self.he_normal = heNormalUI()
        self.lecun_normal = lecunNormalUI()
        self.he_uniform = heUniformUI()

        self.kernelInitializer = QComboBox()
        self.kernelInitializer.addItems(["RandomUniform","Zeros","Ones","Constant","RandomNormal","TruncatedNormal","VarianceScaling","Orthogonal","Identity","lecun_uniform","glorot_normal","glorot_uniform","he_normal","lecun_normal","he_uniform"])
        self.kernelInitializer.currentIndexChanged[int].connect(lambda index: self.stack.setCurrentIndex(index))

        self.RandomUniformArg = QWidget()
        self.ZerosArg = QWidget()
        self.OnesArg = QWidget()
        self.ConstantArg = QWidget()
        self.RandomNormalArg = QWidget()
        self.TruncatedNormalArg = QWidget()
        self.VarianceScalingArg = QWidget()
        self.OrthogonalArg = QWidget()
        self.IdentityArg = QWidget()
        self.lecun_uniformArg =QWidget()
        self.glorot_normalArg = QWidget()
        self.glorot_uniformArg = QWidget()
        self.he_normalArg = QWidget()
        self.lecun_normalArg = QWidget()
        self.he_uniformArg = QWidget()



        self.RandomUniformArg.setLayout(self.RandomUniform.layout())
        self.ZerosArg.setLayout(self.Zeros.layout())
        self.OnesArg.setLayout(self.Ones.layout())
        self.ConstantArg.setLayout(self.Constant.layout())
        self.RandomNormalArg.setLayout(self.RandomNormal.layout())
        self.TruncatedNormalArg.setLayout(self.TruncatedNormal.layout())
        self.VarianceScalingArg.setLayout(self.VarianceScaling.layout())
        self.OrthogonalArg.setLayout(self.Orthogonal.layout())
        self.IdentityArg.setLayout(self.Identity.layout())
        self.lecun_uniformArg.setLayout(self.lecun_uniform.layout())
        self.glorot_normalArg.setLayout(self.glorot_normal.layout())
        self.glorot_uniformArg.setLayout(self.glorot_uniform.layout())
        self.he_normalArg.setLayout(self.he_normal.layout())
        self.lecun_normalArg.setLayout(self.lecun_normal.layout())
        self.he_uniformArg.setLayout(self.he_uniform.layout())

    

        self.stack = QStackedWidget()
        self.stack.addWidget(self.RandomUniformArg)
        self.stack.addWidget(self.ZerosArg)
        self.stack.addWidget(self.OnesArg)
        self.stack.addWidget(self.ConstantArg)
        self.stack.addWidget(self.RandomNormalArg)
        self.stack.addWidget(self.TruncatedNormalArg)
        self.stack.addWidget(self.VarianceScalingArg)
        self.stack.addWidget(self.OrthogonalArg)
        self.stack.addWidget(self.IdentityArg)
        self.stack.addWidget(self.lecun_uniformArg)
        self.stack.addWidget(self.glorot_normalArg)
        self.stack.addWidget(self.glorot_uniformArg)
        self.stack.addWidget(self.he_normalArg)
        self.stack.addWidget(self.lecun_normalArg)
        self.stack.addWidget(self.he_uniformArg)

        """
        Batch Initializer

        """
        self.RandomUniform_batch = RandomUniformUI()
        self.Zeros_batch = ZerosUI()
        self.Ones_batch = OnesUI()
        self.Constant_batch = ConstantUI()
        self.RandomNormal_batch = RandomNormalUI()
        self.TruncatedNormal_batch = TruncatedNormalUI()
        self.VarianceScaling_batch = VarianceScalingUI()
        self.Orthogonal_batch = OrthogonalUI()
        self.Identity_batch = IdentityUI()
        self.lecun_uniform_batch = lecunUniformUI()
        self.glorot_normal_batch = glorotNormalUI()
        self.glorot_uniform_batch = glorotUniformUI()
        self.he_normal_batch = heNormalUI()
        self.lecun_normal_batch = lecunNormalUI()
        self.he_uniform_batch = heUniformUI()

        self.BatchInitializer = QComboBox()
        self.BatchInitializer.addItems(["RandomUniform","Zeros","Ones","Constant","RandomNormal","TruncatedNormal","VarianceScaling","Orthogonal","Identity","lecun_uniform","glorot_normal","glorot_uniform","he_normal","lecun_normal","he_uniform"])
        self.BatchInitializer.currentIndexChanged[int].connect(lambda index : self.stack_batch.setCurrentIndex(index))

        self.RandomUniformArg_batch = QWidget()
        self.ZerosArg_batch = QWidget()
        self.OnesArg_batch = QWidget()
        self.ConstantArg_batch = QWidget()
        self.RandomNormalArg_batch = QWidget()
        self.TruncatedNormalArg_batch = QWidget()
        self.VarianceScalingArg_batch = QWidget()
        self.OrthogonalArg_batch = QWidget()
        self.IdentityArg_batch = QWidget()
        self.lecun_uniformArg_batch =QWidget()
        self.glorot_normalArg_batch = QWidget()
        self.glorot_uniformArg_batch = QWidget()
        self.he_normalArg_batch = QWidget()
        self.lecun_normalArg_batch = QWidget()
        self.he_uniformArg_batch = QWidget()


        self.RandomUniformArg_batch.setLayout(self.RandomUniform_batch.layout())
        self.ZerosArg_batch.setLayout(self.Zeros_batch.layout())
        self.OnesArg_batch.setLayout(self.Ones_batch.layout())
        self.ConstantArg_batch.setLayout(self.Constant_batch.layout())
        self.RandomNormalArg_batch.setLayout(self.RandomNormal_batch.layout())
        self.TruncatedNormalArg_batch.setLayout(self.TruncatedNormal_batch.layout())
        self.VarianceScalingArg_batch.setLayout(self.VarianceScaling_batch.layout())
        self.OrthogonalArg_batch.setLayout(self.Orthogonal_batch.layout())
        self.IdentityArg_batch.setLayout(self.Identity_batch.layout())
        self.lecun_uniformArg_batch.setLayout(self.lecun_uniform_batch.layout())
        self.glorot_normalArg_batch.setLayout(self.glorot_normal_batch.layout())
        self.glorot_uniformArg_batch.setLayout(self.glorot_uniform_batch.layout())
        self.he_normalArg_batch.setLayout(self.he_normal_batch.layout())
        self.lecun_normalArg_batch.setLayout(self.lecun_normal_batch.layout())
        self.he_uniformArg_batch.setLayout(self.he_uniform_batch.layout())

        self.stack_batch = QStackedWidget()
        self.stack_batch.addWidget(self.RandomUniformArg_batch)
        self.stack_batch.addWidget(self.ZerosArg_batch)
        self.stack_batch.addWidget(self.OnesArg_batch)
        self.stack_batch.addWidget(self.ConstantArg_batch)
        self.stack_batch.addWidget(self.RandomNormalArg_batch)
        self.stack_batch.addWidget(self.TruncatedNormalArg_batch)
        self.stack_batch.addWidget(self.VarianceScalingArg_batch)
        self.stack_batch.addWidget(self.OrthogonalArg_batch)
        self.stack_batch.addWidget(self.IdentityArg_batch)
        self.stack_batch.addWidget(self.lecun_uniformArg_batch)
        self.stack_batch.addWidget(self.glorot_normalArg_batch)
        self.stack_batch.addWidget(self.glorot_uniformArg_batch)
        self.stack_batch.addWidget(self.he_normalArg_batch)
        self.stack_batch.addWidget(self.lecun_normalArg_batch)
        self.stack_batch.addWidget(self.he_uniformArg_batch)
        """
        Kernal regularizer

        """
        self.l1_kernelRegularizer = l1UI()
        self.l2_kernelRegularizer = l2UI()
        self.l1_l2_kernelRegularizer = l1_l2UI()

        self.kernelRegularizer = QComboBox()
        self.kernelRegularizer.addItems(["None","l1","l2","l1_l2"])
        self.kernelRegularizer.currentIndexChanged[int].connect(lambda index : self.stack_kernelRegularizer.setCurrentIndex(index))

        self.stack_kernelRegularizer = QStackedLayout()
        self.l1 = QWidget()
        self.l2 = QWidget()
        self.l1_l2 = QWidget()

        self.l1.setLayout(self.l1_kernelRegularizer.layout())
        self.l2.setLayout(self.l2_kernelRegularizer.layout())
        self.l1_l2.setLayout(self.l1_l2_kernelRegularizer.layout())

        self.stack_kernelRegularizer.addWidget(QLabel("None"))
        self.stack_kernelRegularizer.addWidget(self.l1)
        self.stack_kernelRegularizer.addWidget(self.l2)
        self.stack_kernelRegularizer.addWidget(self.l1_l2)

        """
        Bias regularizer

        """
        self.l1_biasRegularizer = l1UI()
        self.l2_biasRegularizer = l2UI()
        self.l1_l2_biasRegularizer = l1_l2UI()

        self.biasRegularizer = QComboBox()
        self.biasRegularizer.addItems(["None","l1","l2","l1_l2"])
        self.biasRegularizer.currentIndexChanged[int].connect(lambda index : self.stack_biasRegularizer.setCurrentIndex(index))

        self.stack_biasRegularizer = QStackedLayout()
        self.l1_bias = QWidget()
        self.l2_bias = QWidget()
        self.l1_l2_bias = QWidget()

        self.l1_bias.setLayout(self.l1_biasRegularizer.layout())
        self.l2_bias.setLayout(self.l2_biasRegularizer.layout())
        self.l1_l2_bias.setLayout(self.l1_l2_kernelRegularizer.layout())

        self.stack_biasRegularizer.addWidget(QLabel("None"))
        self.stack_biasRegularizer.addWidget(self.l1_bias)
        self.stack_biasRegularizer.addWidget(self.l2_bias)
        self.stack_biasRegularizer.addWidget(self.l1_l2_bias)

        """
        activity_regularizer

        """
        self.l1_activityRegularizer = l1UI()
        self.l2_activityRegularizer = l2UI()
        self.l1_l2_activityRegularizer = l1_l2UI()

        self.activityRegularizer = QComboBox()
        self.activityRegularizer.addItems(["None","l1","l2","l1_l2"])
        self.activityRegularizer.currentIndexChanged[int].connect(lambda index : self.stack_activityRegularizer.setCurrentIndex(index))

        self.stack_activityRegularizer = QStackedLayout()
        self.l1_activity = QWidget()
        self.l2_activity = QWidget()
        self.l1_l2_activity = QWidget()

        self.l1_activity.setLayout(self.l1_biasRegularizer.layout())
        self.l2_activity.setLayout(self.l2_biasRegularizer.layout())
        self.l1_l2_activity.setLayout(self.l1_l2_kernelRegularizer.layout())
        
        self.stack_activityRegularizer.addWidget(QLabel("None"))
        self.stack_activityRegularizer.addWidget(self.l1_activity)
        self.stack_activityRegularizer.addWidget(self.l2_activity)
        self.stack_activityRegularizer.addWidget(self.l1_l2_activity)

        """
        kernel_constraint

        """
        self.MaxNorm_kernelConstraint = MaxNormUI()
        self.NonNeg_kernelConstraint = NonNegUI()
        self.UnitNorm_kernelConstraint = UnitNormUI()
        self.MinMaxNorm_kernelConstraint = MinMaxNormUI()

        self.kernelConstraint = QComboBox()
        self.kernelConstraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.kernelConstraint.currentIndexChanged[int].connect(lambda index : self.stack_kernelConstraint.setCurrentIndex(index))

        self.stack_kernelConstraint = QStackedWidget()

        self.MaxNorm_kernel = QWidget()
        self.NonNeg_kernel = QWidget()
        self.UnitNorm_kernel = QWidget()
        self.MinMaxNorm_kernel = QWidget()

        self.MaxNorm_kernel.setLayout(self.MaxNorm_kernelConstraint.layout())
        self.NonNeg_kernel.setLayout(self.NonNeg_kernelConstraint.layout())
        self.UnitNorm_kernel.setLayout(self.UnitNorm_kernelConstraint.layout())
        self.MinMaxNorm_kernel.setLayout(self.MinMaxNorm_kernelConstraint.layout())

        self.stack_kernelConstraint.addWidget(QLabel("None"))
        self.stack_kernelConstraint.addWidget(self.MaxNorm_kernel)
        self.stack_kernelConstraint.addWidget(self.NonNeg_kernel)
        self.stack_kernelConstraint.addWidget(self.UnitNorm_kernel)
        self.stack_kernelConstraint.addWidget(self.MinMaxNorm_kernel)

        """
        bias_constraint

        """
        self.MaxNorm_biasConstraint = MaxNormUI()
        self.NonNeg_biasConstraint = NonNegUI()
        self.UnitNorm_biasConstraint = UnitNormUI()
        self.MinMaxNorm_biasConstraint = MinMaxNormUI()

        self.biasConstraint = QComboBox()
        self.biasConstraint.addItems(["None","MaxNorm","NonNeg","UnitNorm","MinMaxNorm"])
        self.biasConstraint.currentIndexChanged[int].connect(lambda index : self.stack_biasConstraint.setCurrentIndex(index))

        self.stack_biasConstraint = QStackedWidget()

        self.MaxNorm_bias = QWidget()
        self.NonNeg_bias = QWidget()
        self.UnitNorm_bias = QWidget()
        self.MinMaxNorm_bias = QWidget()

        self.MaxNorm_bias.setLayout(self.MaxNorm_biasConstraint.layout())
        self.NonNeg_bias.setLayout(self.NonNeg_biasConstraint.layout())
        self.UnitNorm_bias.setLayout(self.UnitNorm_biasConstraint.layout())
        self.MinMaxNorm_bias.setLayout(self.MinMaxNorm_biasConstraint.layout())

        self.stack_biasConstraint.addWidget(QLabel("None"))
        self.stack_biasConstraint.addWidget(self.MaxNorm_bias)
        self.stack_biasConstraint.addWidget(self.NonNeg_bias)
        self.stack_biasConstraint.addWidget(self.UnitNorm_bias)
        self.stack_biasConstraint.addWidget(self.MinMaxNorm_bias)

        
        """
        Button

        """

        self.passValue = QPushButton("Done")
        """
        Layout

        """
        layout = QGridLayout()
        layout.addWidget(QLabel('Neurons:'),0,0)
        layout.addWidget(self.neuron,0,1)

        layout.addWidget(QLabel("Activation:"),1,0)
        layout.addWidget(self.activation,1,1)

        layout.addWidget(QLabel("Use Bias:"),2,0)
        layout.addWidget(self.useBias,2,1)

        layout.addWidget(QLabel("kernelInitializer"),3,0)
        layout.addWidget(self.kernelInitializer,3,1)
        layout.addWidget(self.stack,4,1)

        layout.addWidget(QLabel("Batch Initializer"),5,0)
        layout.addWidget(self.BatchInitializer,5,1)
        layout.addWidget(self.stack_batch,6,1)

        layout.addWidget(QLabel("kernel_regularizer"),7,0)
        layout.addWidget(self.kernelRegularizer,7,1)
        layout.addLayout(self.stack_kernelRegularizer,8,1)

        layout.addWidget(QLabel("bias_regularizer"),9,0)
        layout.addWidget(self.biasRegularizer,9,1)
        layout.addLayout(self.stack_biasRegularizer,10,1)

        layout.addWidget(QLabel("activity_regularizer"),11,0)
        layout.addWidget(self.activityRegularizer,11,1)
        layout.addLayout(self.stack_activityRegularizer,12,1)

        layout.addWidget(QLabel("kernel_constraint"),13,0)
        layout.addWidget(self.kernelConstraint,13,1)
        layout.addWidget(self.stack_kernelConstraint,14,1)

        layout.addWidget(QLabel("bias_constraint"),15,0)
        layout.addWidget(self.biasConstraint,15,1)
        layout.addWidget(self.stack_biasConstraint,16,1)
    
        layout.addWidget(self.passValue,17,1)
        
       
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
        
    
        self.passValue.clicked.connect(self.parse_arguments())
        self.scroll_panel_layout.addLayout(layout,0,0)
        self.set_styling()

    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")

    def parse_arguments(self):
        '''
        Should be changed to parse arguments
        '''
        Units = int(self.neuron.text())
        print(self.activation.currentText())
        print(self.useBias.currentText())
        print(self.kernelInitializer.currentText())
        
class RandomUniformUI(QWidget):
    def __init__(self):
        super().__init__()
        
    def layout(self):
        RandomUniformLayout = QGridLayout()
        self.minval = QLineEdit("-0.05")
        self.maxval = QLineEdit("0.05")
        self.seed = QLineEdit("None")

        RandomUniformLayout.addWidget(QLabel("Arguments"),0,1)
        RandomUniformLayout.addWidget(QLabel("Minval"),1,0)
        RandomUniformLayout.addWidget(self.minval,1,1)

        RandomUniformLayout.addWidget(QLabel("Maxval"),2,0)
        RandomUniformLayout.addWidget(self.maxval,2,1)

        RandomUniformLayout.addWidget(QLabel("Seed"),3,0)
        RandomUniformLayout.addWidget(self.seed,3,1)

        return RandomUniformLayout
"""
Zeros class provide UI of zeros

"""

class ZerosUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):

        ZerosLayout = QHBoxLayout()
        ZerosLayout.addWidget(QLabel("Initializer that generates tensors initialized to 0."))

        return ZerosLayout
"""
class of ones which provide UI ones
"""
class OnesUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):

        ZerosLayout = QHBoxLayout()
        ZerosLayout.addWidget(QLabel("Initializer that generates tensors initialized to 1."))

        return ZerosLayout
"""
class of constant which provide UI of Constant
"""

class ConstantUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.value = QLineEdit("0")

        ConstantLayout = QGridLayout()
        ConstantLayout.addWidget(QLabel("Arguments"),0,1)
        ConstantLayout.addWidget(QLabel("value"))
        ConstantLayout.addWidget(self.value)
        return ConstantLayout
"""
class of random normal which provide UI of random normal
"""

class RandomNormalUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):

        self.mean = QLineEdit("0.0")
        self.stddev = QLineEdit("0.05")
        self.seed = QLineEdit("None")

        RandomNormalLayout = QGridLayout()
        RandomNormalLayout.addWidget(QLabel("Arguments"),0,1)
        RandomNormalLayout.addWidget(QLabel("mean"),1,0)
        RandomNormalLayout.addWidget(self.mean,1,1)

        RandomNormalLayout.addWidget(QLabel("stddev"),2,0)
        RandomNormalLayout.addWidget(self.stddev,2,1)

        RandomNormalLayout.addWidget(QLabel("seed"),3,0)
        RandomNormalLayout.addWidget(self.seed,3,1)

        return RandomNormalLayout
"""
class of Truncated normal which provide UI of truncated_normal
"""


class TruncatedNormalUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.TruncatedNormal_mean = QLineEdit("0.0")
        self.TruncatedNormal_stddev = QLineEdit("0.05")
        self.TruncatedNormal_seed = QLineEdit("None")

        TruncatedNormalLayout = QGridLayout()
        TruncatedNormalLayout.addWidget(QLabel("Arguments"),0,1)
        TruncatedNormalLayout.addWidget(QLabel("mean"),1,0)
        TruncatedNormalLayout.addWidget(self.TruncatedNormal_mean,1,1)

        TruncatedNormalLayout.addWidget(QLabel("stddev"),2,0)
        TruncatedNormalLayout.addWidget(self.TruncatedNormal_stddev,2,1)

        TruncatedNormalLayout.addWidget(QLabel("seed"),3,0)
        TruncatedNormalLayout.addWidget(self.TruncatedNormal_seed,3,1)

        return TruncatedNormalLayout

"""
class of Variance Scaling which provide UI of variance_scaling
"""

class VarianceScalingUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.scale = QLineEdit("1.0")
        self.mode = QComboBox()
        self.mode.addItems(["fan_in","fan_out","fan_avg"])
        self.distribution = QComboBox()
        self.distribution.addItems(["normal","uniform"])
        self.seed = QLineEdit("None")

        VarianceScalingLayout = QGridLayout()
        VarianceScalingLayout.addWidget(QLabel("Arguments"),0,1)
        VarianceScalingLayout.addWidget(QLabel("scale"),1,0)
        VarianceScalingLayout.addWidget(self.scale,1,1)
        VarianceScalingLayout.addWidget(QLabel("mode"),2,0)
        VarianceScalingLayout.addWidget(self.mode,2,1)
        VarianceScalingLayout.addWidget(QLabel("distribution"),3,0)
        VarianceScalingLayout.addWidget(self.distribution,3,1)
        VarianceScalingLayout.addWidget(QLabel("seed"),4,0)
        VarianceScalingLayout.addWidget(self.seed,4,1)

        return VarianceScalingLayout
"""
class of orthogonal which provide UI of orthogonal
"""

class OrthogonalUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.gain = QLineEdit("1.0")
        self.seed = QLineEdit("None")

        OrthogonalLayout = QGridLayout()
        OrthogonalLayout.addWidget(QLabel("Arguments"),0,1)
        OrthogonalLayout.addWidget(QLabel("gain"),1,0)
        OrthogonalLayout.addWidget(self.gain,1,1)
        OrthogonalLayout.addWidget(QLabel("seed"),2,0)
        OrthogonalLayout.addWidget(self.seed,2,1)

        return OrthogonalLayout
"""
class of identity which provide UI of Identity
"""
class IdentityUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.gain = QLineEdit("1.0")

        IdentityLayout = QGridLayout()
        IdentityLayout.addWidget(QLabel("Arguments"),0,1)
        IdentityLayout.addWidget(QLabel("gain"))
        IdentityLayout.addWidget(self.gain,1,1)

        return IdentityLayout
"""
class of lecun uniform which provide UI of lecun_uniform
"""

class lecunUniformUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.seed = QLineEdit("None")

        lecun_uniformLayout = QGridLayout()
        lecun_uniformLayout.addWidget(QLabel("Arguments"),0,1)
        lecun_uniformLayout.addWidget(QLabel("seed"),1,0)
        lecun_uniformLayout.addWidget(self.seed,1,1)

        return lecun_uniformLayout
"""
class of glorot normal which provide UI of glorot_normal
"""
class glorotNormalUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.seed = QLineEdit("None")

        glorot_normalLayout = QGridLayout()
        glorot_normalLayout.addWidget(QLabel("Arguments"),0,1)
        glorot_normalLayout.addWidget(QLabel("seed"),1,0)
        glorot_normalLayout.addWidget(self.seed,1,1)

        return glorot_normalLayout
"""
class of glorot uniform which provide UI of glorot uniform
"""

class glorotUniformUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.seed = QLineEdit("None")

        glorot_uniformLayout = QGridLayout()
        glorot_uniformLayout.addWidget(QLabel("Arguments"),0,1)
        glorot_uniformLayout.addWidget(QLabel("seed"),1,0)
        glorot_uniformLayout.addWidget(self.seed,1,1)

        return glorot_uniformLayout
"""
class of henormal which provide UI of he_normal
"""
    
class heNormalUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):

        self.seed = QLineEdit("None")

        he_normalLayout = QGridLayout()
        he_normalLayout.addWidget(QLabel("Arguments"),0,1)
        he_normalLayout.addWidget(QLabel("seed"),1,0)
        he_normalLayout.addWidget(self.seed,1,1)

        return he_normalLayout
"""
class of lecun normal which provide UI of lecun_normal
"""
class lecunNormalUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.lecun_normal_seed = QLineEdit("None")

        lecun_normalLayout = QGridLayout()
        lecun_normalLayout.addWidget(QLabel("Arguments"),0,1)
        lecun_normalLayout.addWidget(QLabel("seed"),1,0)
        lecun_normalLayout.addWidget(self.lecun_normal_seed,1,1)

        return lecun_normalLayout
"""
class of he uniform which provide UI of he_uniform
"""

class heUniformUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.he_uniform_seed = QLineEdit("None")

        he_uniformLayout = QGridLayout()
        he_uniformLayout.addWidget(QLabel("Arguments"),0,1)
        he_uniformLayout.addWidget(QLabel("seed"),1,0)
        he_uniformLayout.addWidget(self.he_uniform_seed,1,1)

        return he_uniformLayout
"""
class of l1 which provide UI of l1
"""

class l1UI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.l1 = QLineEdit("0.")
        l1Layout = QGridLayout()
        l1Layout.addWidget(QLabel("Arguments"),0,1)
        l1Layout.addWidget(QLabel("value"),1,0)
        l1Layout.addWidget(self.l1,1,1)

        return l1Layout
"""
class of l2 which provide UI of l2
"""
class l2UI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.l2 = QLineEdit("0.")
        l2Layout = QGridLayout()
        l2Layout.addWidget(QLabel("Arguments"),0,1)
        l2Layout.addWidget(QLabel("value"),1,0)
        l2Layout.addWidget(self.l2,1,1)

        return l2Layout
"""
class of l1_l2 which provide UI of l1_l2
"""
class l1_l2UI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.l1 = QLineEdit("0.01")
        self.l2 = QLineEdit("0.01")

        l1_l2Layout = QGridLayout()
        l1_l2Layout.addWidget(QLabel("Arguments"),0,1)
        l1_l2Layout.addWidget(QLabel("l1"),1,0)
        l1_l2Layout.addWidget(self.l1,1,1)
        l1_l2Layout.addWidget(QLabel("l2"),2,0)
        l1_l2Layout.addWidget(self.l2,2,1)

        return l1_l2Layout
"""
class of max norm which provide UI of max_morm
"""

class MaxNormUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.max_value = QLineEdit("2")
        self.axis = QLineEdit("0")

        MaxNormLayout = QGridLayout()
        MaxNormLayout.addWidget(QLabel("Arguments"),0,1)
        MaxNormLayout.addWidget(QLabel("max_value"),1,0)
        MaxNormLayout.addWidget(self.max_value,1,1)
        MaxNormLayout.addWidget(QLabel("axis"),2,0)
        MaxNormLayout.addWidget(self.axis,2,1)

        return MaxNormLayout
"""
class of non neg which provide UI of non_neg
"""
class NonNegUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        NonNegLayout = QHBoxLayout()
        NonNegLayout.addWidget(QLabel("Constrains the weights to be non-negative."))
        return NonNegLayout
"""
class of unit norm which provide UI of unit_norm
"""
class UnitNormUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.axis_UnitNorm = QLineEdit("0")

        UnitNormLayout = QGridLayout()
        UnitNormLayout.addWidget(QLabel("Arguments"),0,1)
        UnitNormLayout.addWidget(QLabel("axis"),1,0)
        UnitNormLayout.addWidget(self.axis_UnitNorm,1,1)

        return UnitNormLayout
"""
class of min max norm which provide UI of max_norm
"""
class MinMaxNormUI(QWidget):
    def __init__(self):
        super().__init__()

    def layout(self):
        self.min_vale = QLineEdit("0.0")
        self.max_value = QLineEdit("1.0")
        self.rate = QLineEdit("1.0")
        self.axis = QLineEdit("0")

        MinMaxNormLayout = QGridLayout()
        MinMaxNormLayout.addWidget(QLabel("Arguments"),0,1)
        MinMaxNormLayout.addWidget(QLabel("min_value"),1,0)
        MinMaxNormLayout.addWidget(self.min_vale,1,1)
        MinMaxNormLayout.addWidget(QLabel("max_value"),2,0)
        MinMaxNormLayout.addWidget(self.max_value,2,1)
        MinMaxNormLayout.addWidget(QLabel("rate"),3,0)
        MinMaxNormLayout.addWidget(self.rate,3,1)
        MinMaxNormLayout.addWidget(QLabel("axis"),4,0)
        MinMaxNormLayout.addWidget(self.axis,4,1)

        return MinMaxNormLayout