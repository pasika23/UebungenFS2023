from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtGui import *

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UebungenFS23/Abgabe/showmap.ui',self)
        self.show()

        self.button.clicked.connect(self.clickbutton)
    
    def clickbutton(self):
        l = self.laenge.text()
        b = self.breite.text()

        link = f"https://www.google.ch/maps/place/{b},{l}" 
        print(link)
        QDesktopServices.openUrl(QUrl(link))

app = QApplication([])
win = UIFenster()
app.exec()