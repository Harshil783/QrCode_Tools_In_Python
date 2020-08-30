information = { "__author__": "Harshil Pandey",
"__copyright__": "Copyright (C) 2020, Harshil Pandey",
"__credits__": "harshil Pandey",
"__license__": "The Apache-2.0 License",
"__version__": "1.1",
"__maintainer__": "Harshil Pandey",
"__email__": "harshipandey57@gmail.com",
"__status__": "Stable"}
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import qdarkgraystyle
import requests

class checkUpdate(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(checkUpdate,self).__init__(parent)
        self.update1 = uic.loadUi(r'UI/update.ui',self)
        self.updatesa()
    def updatesa(self):
            response = requests.get(
                'https://raw.githubusercontent.com/Harshil783/QrCode_Tools_In_Python/master/version.txt')
            data = float(response.text.replace("__version__ = '","").replace("'",""))
            local_version = float(information["__version__"])
            f = False
            if local_version < data:
                #print("Software Need TO Be Updated")
                QMessageBox.warning(self, "Updates Available", "Some Updates Are Available,Download Them")
                try:
                    response = requests.get('https://github.com/Harshil783/QrCode_Tools_In_Python/releases/latest/download/QrCode.Tools.zip',stream = True)
                    open('update.zip', 'wb').write(response.content)
                    with ZipFile('update.zip', 'r') as zipObj: # Extract all the contents of zip file in current directory
                        zipObj.extractall(path=l)
                    os.remove('update.zip')
                except Exception:
                    QMessageBox.warning(self, "Error", "Connection Error")
            else:
                QMessageBox.information(self, "Updated", "Software Up-to Date")

# sub1 = checkUpdate()
# sub1.show()
# time.sleep(1)
# exit()
app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkgraystyle.load_stylesheet())
window = checkUpdate()