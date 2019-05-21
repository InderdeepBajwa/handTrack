
import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from ui.main_ui import Ui_Dialog

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.text = QtWidgets.QLabel("Open a video to start the analysis")
        self.button = QtWidgets.QPushButton("Open New Video")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.handleNewWindow)

    def handleNewWindow(self):
        self.show()



class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("File opened!")


        self.setLayout(self.layout)

        
        

if __name__ == "__main__":
    # Initiating the application
    app = QtWidgets.QApplication([])

    
    # Loading file browser
    widget = MyWidget()

    widget.resize(800,450)
    
    # Showing file picker
    widget.show()

    # Showing analysis

    sys.exit(app.exec_())


