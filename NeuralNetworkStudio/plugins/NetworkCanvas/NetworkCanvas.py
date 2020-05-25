from PySide2.QtWidgets import QWidget, QTableView
from PySide2 import QtCore
from PySide2.QtGui import QStandardItem, QStandardItemModel
from plugins.LayerBox.LayerBox import LayerBoxWidget

class NetworkCanvasWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.accept()
            
    def dropEvent(self, event):
        tmp = QStandardItemModel()
        tmp.dropMimeData(event.mimeData(), event.dropAction(), 0, 0, QtCore.QModelIndex())
        self.add_to_layout(LayerBoxWidget(tmp.index(0, 0).data()))
        
    def add_to_layout(self, layer):
        pass
    