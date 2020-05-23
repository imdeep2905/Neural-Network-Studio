import sys
from plugins.Toolbar.ToolBar import ToolBarWidget
from plugins.NetworkControl.NetworkController import NetworkControllerWidget
from plugins.Layerselectors.LayerSelector import LayersSelectorWidget
from plugins.LayerControllers.LayerControllers import DenseLayerControlWidget, Conv2DLayerControlWidget
from PySide2.QtWidgets import QApplication, QSplitter

class MainWindow(QApplication):
    def __init__(self):
        super().__init__()
        
        
if __name__ == "__main__":
    sys.exit(MainWindow().exec_())