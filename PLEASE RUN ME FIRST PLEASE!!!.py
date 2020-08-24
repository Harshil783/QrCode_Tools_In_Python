import subprocess
import os
current = os.getcwd()
switch = os.chdir(current + '\qdarkgraystyle-develop\qdarkgraystyle-develop')
subprocess.call(['python', 'setup.py', 'install']) #This is the theme for app Don't Remove Else Beauty will be lost
subprocess.call(['pip', 'install' ,'qrcode']) #Generating QR Code
subprocess.call(['pip', 'install' ,'PIL']) #For Png Generation
subprocess.call(['pip', 'install' ,'PyQt5']) #Using For GUI
subprocess.call(['pip', 'install' ,'pyzbar'])
