from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import qdarkgraystyle

class aboutme(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(aboutme,self).__init__(parent)
        self.ui()
        self.show()
    def ui(self):
        self.lol = uic.loadUi(r'UI/about.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkgraystyle.load_stylesheet())
window = aboutme()