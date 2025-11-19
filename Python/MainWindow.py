import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from MainWindowUI import Ui_MainWindow

mapping = {

}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow(mapping)
        self.ui.setupUi(self)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()