'''
TODO
# Add proper scaling, arrangement, styling
# optimize code
'''
from PySide2.QtWidgets import QWidget, QPushButton, QTabWidget ,QFormLayout, QLabel,QStyledItemDelegate, QVBoxLayout, QHBoxLayout,QAbstractItemView, QGridLayout,QListWidget, QComboBox, QStackedLayout, QLineEdit
from PySide2.QtGui import QDoubleValidator, QStandardItem, QFontMetrics, QPalette 
from PySide2.QtCore import Qt, QEvent 

class NetworkController(QWidget):   
    def __init__(self):
        super().__init__() 
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(QLabel("Optimizer :"), 0, 0)
        self.optimizer_selector = QComboBox()
        self.optimizer_selector.addItems(["SGD", "RMSprop", "Adam", "Adadelta", "Adagrad", "Adamax", "Nadam", "Ftrl", "Custom"])
        self.optimizer_stack = QStackedLayout()
        self.optimizer_stack.addWidget(SGDUI())
        self.optimizer_stack.addWidget(RMSpropUI())
        self.optimizer_stack.addWidget(AdamUI())
        self.optimizer_stack.addWidget(AdadeltaUI())
        self.optimizer_stack.addWidget(AdagradUI())
        self.optimizer_stack.addWidget(AdamaxUI())
        self.optimizer_stack.addWidget(NadamUI())
        self.optimizer_stack.addWidget(FtrlUI())
        self.loss_selector = QComboBox()
        self.loss_selector.addItems([
            "BinaryCrossentropy", 
            "CategoricalCrossentropy", 
            "SparseCategoricalCrossentropy", 
            "Poisson",
            "binary_crossentropy function",
            "categorical_crossentropy function",
            "sparse_categorical_crossentropy function",
            "poisson function",
            "KLDivergence",
            "kl_divergence function",
            "MeanSquaredError", 
            "MeanAbsoluteError", 
            "MeanAbsolutePercentageError", 
            "MeanSquaredLogarithmicError", 
            "CosineSimilarity", 
            "mean_squared_error function",
            "mean_absolute_error function",
            "mean_absolute_percentage_error function",
            "mean_squared_logarithmic_error function",
            "cosine_similarity function",
            "Huber", 
            "huber function",
            "LogCosh",
            "log_cosh function",
            "Hinge",
            "SquaredHinge", 
            "CategoricalHinge", 
            "hinge function",
            "squared_hinge function",
            "categorical_hinge function",
            "CUSTOM_my1"])
        self.metrics_selector = CheckableComboBox()
        self.metrics_selector.addItems([
            "Accuracy",
            "BinaryAccuracy", 
            "CategoricalAccuracy", 
            "TopKCategoricalAccuracy", 
            "SparseTopKCategoricalAccuracy", 
            "BinaryCrossentropy", 
            "CategoricalCrossentropy", 
            "SparseCategoricalCrossentropy", 
            "KLDivergence", 
            "Poisson", 
            "MeanSquaredError", 
            "RootMeanSquaredError", 
            "MeanAbsoluteError", 
            "MeanAbsolutePercentageError", 
            "MeanSquaredLogarithmicError", 
            "CosineSimilarity", 
            "LogCoshError", 
            "MeanIoU", 
            "AUC", 
            "Precision", 
            "Hinge", 
            "SquaredHinge", 
            "CategoricalHinge", 
            "Recall", 
            "TruePositives", 
            "TrueNegatives", 
            "FalsePositives", 
            "FalseNegatives", 
            "PrecisionAtRecall", 
            "SensitivityAtSpecificity", 
            "SpecificityAtSensitivity",
            "CUSTOM_my1"
        ])
        self.optimizer_selector.currentIndexChanged[int].connect(lambda index: self.optimizer_stack.setCurrentIndex(index))
        tmp = QWidget()
        tmp.setLayout(self.optimizer_stack)
        self.run_eagerly = QComboBox()
        self.run_eagerly.addItems(["True", "False"])
        self.main_layout.addWidget(QLabel("Loss Function:"), 0, 0)
        self.main_layout.addWidget(self.loss_selector, 0, 1)   
        self.main_layout.addWidget(QLabel("Metrics:"),1, 0)
        self.main_layout.addWidget(self.metrics_selector, 1, 1)
        self.main_layout.addWidget(QLabel("run_eagerly:"), 2, 0)
        self.main_layout.addWidget(self.run_eagerly, 2, 1)
        self.main_layout.addWidget(QLabel("Optimizer:"), 3, 0)
        self.main_layout.addWidget(self.optimizer_selector, 3 , 1)
        self.main_layout.addWidget(tmp,4, 0 , 1, 2)
        self.setLayout(self.main_layout)
        self.set_styling()
        
    def set_styling(self):
        self.setStyleSheet("background-color:aliceblue;")
        
class SGDUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.learning_rate = QLineEdit("0.01")
        self.learning_rate.setValidator(QDoubleValidator(0., 1., 5))
        self.momentum = QLineEdit("0.00")
        self.momentum.setValidator(QDoubleValidator(0., 1e5, 2))        
        self.nestrov = QComboBox()
        self.nestrov.addItems(["True", "False"])
        self.main_layout.addWidget(QLabel("Learning rate:"), 0, 0)
        self.main_layout.addWidget(self.learning_rate, 0, 1)
        self.main_layout.addWidget(QLabel("Momentum:"), 1, 0)
        self.main_layout.addWidget(self.momentum,1, 1)
        self.main_layout.addWidget(QLabel("Nestrov:"), 2, 0)
        self.main_layout.addWidget(self.nestrov)
        self.setLayout(self.main_layout)
    
    def get_optimizer(self):
        return None
        
class RMSpropUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.learning_rate = QLineEdit("0.01")
        self.learning_rate.setValidator(QDoubleValidator(0., 1., 5))
        self.momentum = QLineEdit("0.00")
        self.momentum.setValidator(QDoubleValidator(0., 1e5, 2))        
        self.rho = QLineEdit("0.9")
        self.rho.setValidator(QDoubleValidator(0., 1e5, 10))
        self.epsilon = QLineEdit("1e-07")
        self.epsilon.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.centered = QComboBox()
        self.centered.addItems(["True", "False"])
        self.main_layout.addWidget(QLabel("Learning rate:"), 0, 0)
        self.main_layout.addWidget(self.learning_rate, 0, 1)
        self.main_layout.addWidget(QLabel("Momentum:"), 1, 0)
        self.main_layout.addWidget(self.momentum,1, 1)
        self.main_layout.addWidget(QLabel("rho:"), 2, 0)
        self.main_layout.addWidget(self.rho,2 , 1)
        self.main_layout.addWidget(QLabel("epsilon:"),3 ,0)
        self.main_layout.addWidget(self.epsilon,3, 1)
        self.main_layout.addWidget(QLabel("centered:"), 4, 0)
        self.main_layout.addWidget(self.centered, 4, 1)
        self.setLayout(self.main_layout)

    def get_optimizer(self):
        return None

class AdamUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.learning_rate = QLineEdit("0.001")
        self.learning_rate.setValidator(QDoubleValidator(0., 1., 5))
        self.epsilon = QLineEdit("1e-07")
        self.epsilon.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.amsgrad = QComboBox()
        self.amsgrad.addItems(["True", "False"])        
        self.beta_1 = QLineEdit("0.9")
        self.beta_1.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.beta_2 = QLineEdit("0.999")
        self.beta_2.setValidator(QDoubleValidator(0., 1e-10, 10))
        self.main_layout.addWidget(QLabel("Learning rate:"), 0, 0)
        self.main_layout.addWidget(self.learning_rate, 0, 1)
        self.main_layout.addWidget(QLabel("Epsilon:"),1 ,0)
        self.main_layout.addWidget(self.epsilon,1, 1)
        self.main_layout.addWidget(QLabel("Beta 1:"), 2, 0)
        self.main_layout.addWidget(self.beta_1,2, 1)
        self.main_layout.addWidget(QLabel("Beta 2:"), 3, 0)
        self.main_layout.addWidget(self.beta_2,3, 1)
        self.main_layout.addWidget(QLabel("Amsgrad:"), 4, 0)
        self.main_layout.addWidget(self.amsgrad, 4, 1)        
        self.setLayout(self.main_layout)        

    def get_optimizer(self):
        return None
        
class AdadeltaUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.learning_rate = QLineEdit("0.001")
        self.learning_rate.setValidator(QDoubleValidator(0., 1., 5))
        self.epsilon = QLineEdit("1e-07")
        self.epsilon.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.rho = QLineEdit("0.95")
        self.rho.setValidator(QDoubleValidator(0., 1e5, 10))            
        self.main_layout.addWidget(QLabel("Learning rate:"), 0, 0)
        self.main_layout.addWidget(self.learning_rate, 0, 1)
        self.main_layout.addWidget(QLabel("rho:"), 1, 0)
        self.main_layout.addWidget(self.rho,1 , 1)
        self.main_layout.addWidget(QLabel("epsilon:"),2 ,0)
        self.main_layout.addWidget(self.epsilon,2, 1)
        self.setLayout(self.main_layout)
        
    def get_optimizer(self):
        return None
        
class AdagradUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.learning_rate = QLineEdit("0.01")
        self.learning_rate.setValidator(QDoubleValidator(0., 1., 5))
        self.epsilon = QLineEdit("1e-07")
        self.epsilon.setValidator(QDoubleValidator(0., 1e-10, 10))              
        self.initial_accumulator_value = QLineEdit("0.1")
        self.initial_accumulator_value.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.main_layout.addWidget(QLabel("Learning rate:"), 0, 0)
        self.main_layout.addWidget(self.learning_rate, 0, 1)
        self.main_layout.addWidget(QLabel("Epsilon:"),1 ,0)
        self.main_layout.addWidget(self.epsilon,1, 1)
        self.main_layout.addWidget(QLabel("Initial_accumulator_value:"), 2, 0)
        self.main_layout.addWidget(self.initial_accumulator_value,2 , 1)
        self.setLayout(self.main_layout)
        
    def get_optimizer(self):
        return None

class AdamaxUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.learning_rate = QLineEdit("0.01")
        self.learning_rate.setValidator(QDoubleValidator(0., 1., 5))
        self.epsilon = QLineEdit("1e-07")
        self.epsilon.setValidator(QDoubleValidator(0., 1e-10, 10))               
        self.beta_1 = QLineEdit("0.9")
        self.beta_1.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.beta_2 = QLineEdit("0.999")
        self.beta_2.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.main_layout.addWidget(QLabel("Learning rate:"), 0, 0)
        self.main_layout.addWidget(self.learning_rate, 0, 1)
        self.main_layout.addWidget(QLabel("Epsilon:"),1 ,0)
        self.main_layout.addWidget(self.epsilon,1, 1)
        self.main_layout.addWidget(QLabel("Beta 1:"), 2, 0)
        self.main_layout.addWidget(self.beta_1,2, 1)
        self.main_layout.addWidget(QLabel("Beta 2:"), 3, 0)
        self.main_layout.addWidget(self.beta_2,3, 1)
        self.setLayout(self.main_layout)
        
    def get_optimizer(self):
        return None

class NadamUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.learning_rate = QLineEdit("0.01")
        self.learning_rate.setValidator(QDoubleValidator(0., 1., 5))
        self.epsilon = QLineEdit("1e-07")
        self.epsilon.setValidator(QDoubleValidator(0., 1e-10, 10))               
        self.beta_1 = QLineEdit("0.9")
        self.beta_1.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.beta_2 = QLineEdit("0.999")
        self.beta_2.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.main_layout.addWidget(QLabel("Learning rate:"), 0, 0)
        self.main_layout.addWidget(self.learning_rate, 0, 1)
        self.main_layout.addWidget(QLabel("Epsilon:"),1 ,0)
        self.main_layout.addWidget(self.epsilon,1, 1)
        self.main_layout.addWidget(QLabel("Beta 1:"), 2, 0)
        self.main_layout.addWidget(self.beta_1,2, 1)
        self.main_layout.addWidget(QLabel("Beta 2:"), 3, 0)
        self.main_layout.addWidget(self.beta_2,3, 1)
        self.setLayout(self.main_layout)
        
    def get_optimizer(self):
        return None

class FtrlUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QGridLayout()
        self.main_layout.setAlignment(Qt.AlignTop)        
        self.learning_rate = QLineEdit("0.001")
        self.learning_rate.setValidator(QDoubleValidator(0., 1., 5))
        self.learning_rate_power = QLineEdit("0.5")
        self.learning_rate_power.setValidator(QDoubleValidator(0., 1., 5))
        self.initial_accumulator_value = QLineEdit("0.1")
        self.initial_accumulator_value.setValidator(QDoubleValidator(0., 1e-10, 10))  
        self.l1_regularization_strength = QLineEdit("0.0")
        self.l1_regularization_strength.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.l2_regularization_strength = QLineEdit("0.0")
        self.l2_regularization_strength.setValidator(QDoubleValidator(0., 1e-10, 10))        
        self.l2_shrinkage_regularization_strength = QLineEdit("0.0")
        self.l2_shrinkage_regularization_strength.setValidator(QDoubleValidator(0., 1e-10, 10))                
        self.main_layout.addWidget(QLabel("Learning rate:"), 0, 0)
        self.main_layout.addWidget(self.learning_rate, 0, 1)
        self.main_layout.addWidget(QLabel("Initial_accumulator_value:"),1 ,0)
        self.main_layout.addWidget(self.initial_accumulator_value,1, 1)
        self.main_layout.addWidget(QLabel("l1_regularization_strength"), 2, 0)
        self.main_layout.addWidget(self.l1_regularization_strength,2, 1)
        self.main_layout.addWidget(QLabel("l2_regularization_strength:"), 3, 0)
        self.main_layout.addWidget(self.l2_regularization_strength,3, 1)
        self.main_layout.addWidget(QLabel("l2_shrinkage_regularization_strength"), 4, 0)
        self.main_layout.addWidget(self.l2_shrinkage_regularization_strength, 4 , 1)
        self.setLayout(self.main_layout)

    def get_optimizer(self):
        return None

#Thanks to stackoverflow
class CheckableComboBox(QComboBox):

    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        # Make the lineedit the same color as QPushButton
        palette = qApp.palette()
        palette.setBrush(QPalette.Base, palette.button())
        self.lineEdit().setPalette(palette)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):

        if object == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if object == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.updateText()

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elidedText)

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def currentData(self):
        # Return the list of selected items data
        res = "Selected Metrics : "
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                res += str(self.model().item(i).data())
        return res