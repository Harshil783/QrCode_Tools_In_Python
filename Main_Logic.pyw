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
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(925, 485)
        self.button = self.findChild(QtWidgets.QPushButton, 'qrgenerator')
        self.button.clicked.connect(self.QrCodeGenerator) # Remember to pass the definition/method, not the return value!
        self.input = self.findChild(QtWidgets.QLineEdit, 'qredit')
        self.button1 = self.findChild(QtWidgets.QPushButton, 'qropen')
        self.button1.clicked.connect(self.OpenQRCode)
        self.readqr = self.findChild(QtWidgets.QPushButton,'qropen_2')
        self.readqr.clicked.connect(self.ReadQR)
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
            self.url.save("filename.png","PNG")

    def OpenQRCode(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', path,"Image files (*.jpg *.gif *.png *.svg)")[0]
        self.label_2.setPixmap(QPixmap(fname))
    
    def ReadQR(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', path,"Image files (*.jpg *.gif *.png *.svg)")[0]
        data = decode(Image.open(fname))
        data1 = str(data[0][0]).replace('b','')
        self.result1 = self.findChild(QtWidgets.QLineEdit, 'raw_text_result')
        self.result1.setText(data1)
        


app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkgraystyle.load_stylesheet())
window = Ui()
app.exec_()