import sys
from plugins.Toolbar.ToolBar import ToolBarWidget
from plugins.NetworkControl.NetworkController import NetworkControllerWidget
from plugins.Layerselectors.LayerSelector import LayersSelectorWidget
from plugins.LayerControllers.LayerControllers import DenseLayerControlWidget, Conv2DLayerControlWidget
from plugins.NetworkCanvas.NetworkCanvas import NetworkCanvasWidget
from PySide2.QtWidgets import QMainWindow, QApplication, QSplitter, QLabel
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()     
        
        self.setWindowTitle("Neural Network Studio")        
        self.main_splitter = QSplitter(Qt.Horizontal)
        
        self.child_splitter1 = QSplitter(Qt.Vertical)
        self.child_splitter2 = QSplitter(Qt.Vertical)
        
        self.child_splitter1.addWidget(LayersSelectorWidget())
        self.child_splitter1.addWidget(NetworkControllerWidget())
        
        self.child_splitter2.addWidget(Conv2DLayerControlWidget())
        
        self.main_splitter.addWidget(self.child_splitter1)
        self.main_splitter.addWidget(NetworkCanvasWidget())
        self.main_splitter.addWidget(self.child_splitter2)
        
        self.addToolBar(ToolBarWidget())
        self.setCentralWidget(self.main_splitter)
                   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())