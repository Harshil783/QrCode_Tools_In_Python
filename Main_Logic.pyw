from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMenuBar,QAction,QMessageBox
from PyQt5.QtGui import *
import sys
import os
from PIL import Image
from pyzbar.pyzbar import decode
import qdarkgraystyle
path = os.path.abspath(os.getcwd())
import qrcode

class Ui(QtWidgets.QMainWindow):
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(925, 485)
        self.button = self.findChild(QtWidgets.QPushButton, 'qrgenerator')
        self.button.clicked.connect(self.QrCodeGenerator) # Remember to pass the definition/method, not the return value!
        self.input = self.findChild(QtWidgets.QLineEdit, 'qredit')
        self.button1 = self.findChild(QtWidgets.QPushButton, 'qropen')#raw_type_result
        self.button1.clicked.connect(self.OpenQRCode)
        exitAct = QtWidgets.QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(app.quit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Menu')
        fileMenu.addAction(exitAct)
        #self.menu1.triggered.connect(qApp.quit)
        self.show()

    def QrCodeGenerator(self):
        # Generate QR code
        self.url = qrcode.make(self.qredit.text())
        if self.qredit.text() == '':
            QMessageBox.warning(self, "Error", "Please Type In Something To Generate Qr Code")
        else:
            fname = QFileDialog.getSaveFileName(self, 'Open file', path,"Image files (*.png)")[0]
            if fname == '':
                QMessageBox.warning(self, "Error", "Specify Name To Save File!")
            else:
                self.url.save(fname,"PNG")

    def OpenQRCode(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', path,"Image files (*.jpg *.gif *.png *.svg)")[0]
        try:
            data = decode(Image.open(fname))
            self.label_2.setPixmap(QPixmap(fname))
            data1 = str(data[0][0]).replace("b'",'').replace("'","")
            type1 = str(data[0][1])
            self.result1 = self.findChild(QtWidgets.QLineEdit, 'raw_text_result')
            self.result1.setText(data1)#'raw_type_result'
            self.result2 = self.findChild(QtWidgets.QLineEdit, 'raw_type_result')
            self.result2.setText(type1)
        except AttributeError:
            pass

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkgraystyle.load_stylesheet())
window = Ui()
app.exec_()
