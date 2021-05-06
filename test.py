import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets


class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle("The simple program")
        self.setGeometry(300, 250, 350, 250)

        self.new_text = QtWidgets.QLabel(self)

        self.text = QtWidgets.QLabel(self)
        self.text.setText("The base text")
        self.text.move(100, 100)
        self.text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Click me")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        global i
        if i % 2 == 0:
            self.new_text.setText("The second text")
            self.new_text.move(100, 50)
            self.new_text.adjustSize()
        else:
            self.new_text.clear()
        i += 1


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    i = 0
    application()
