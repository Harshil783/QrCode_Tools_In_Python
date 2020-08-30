from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMenuBar,QAction,QMessageBox,QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import os
from PIL import Image
from pyzbar.pyzbar import decode
import qdarkgraystyle
path = os.path.abspath(os.getcwd())
import qrcode
import time

#print("Software Up-to Date")
#def updating(self):

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(r'UI/main.ui', self)
        self.setFixedSize(925, 485)
        self.button = self.findChild(QtWidgets.QPushButton, 'qrgenerator')
        self.button.clicked.connect(self.QrCodeGenerator) # Remember to pass the definition/method, not the return value!
        self.input = self.findChild(QtWidgets.QLineEdit, 'qredit')
        self.exitAct = self.findChild(QtWidgets.QMenu,'menuMenu')
        self.aboutApp = self.findChild(QtWidgets.QAction,'actionAbout')
        self.aboutApp.triggered.connect(self.aboutwindow)
        self.label1 = self.findChild(QtWidgets.QLabel,'image_1')
        self.actionQuit = self.findChild(QtWidgets.QAction,'actionExit')
        self.actionupdates = self.findChild(QtWidgets.QAction,'actionUpdates')
        self.actionupdates.triggered.connect(self.check_Updates)
        self.actionQuit.triggered.connect(app.quit)
        self.show()

    def check_Updates(self):
        import updater

    def aboutwindow(self):
        import about

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

    
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
 
    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
    
            event.accept()
        else:
            event.ignore()
    
    def setpixmap(self, image):
        super().setPixmap(image)

    def set_image(self, file_path):
        self.label1.setPixmap(QPixmap(file_path))
        try:
            data = decode(Image.open(file_path))
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