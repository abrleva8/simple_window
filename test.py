from PyQt5 import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QItemDelegate, QWidget


class PopupView(QWidget):
    def __init__(self, parent=None):
        super(PopupView, self).__init__(parent)
        self.setWindowFlags(Qt.Popup)

class ItemDelegate(QItemDelegate):
    def __init__(self, parent):
        super(ItemDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        return PopupView(parent)

    def updateEditorGeometry(self, editor, option, index):
        editor.move(QCursor.pos())