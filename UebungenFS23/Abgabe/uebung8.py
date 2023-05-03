from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt 
import numpy as np 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Polynomfunktion ploten')

        layout_top = QVBoxLayout()
        layout_bottom = QFormLayout()

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)

        self.koeff = QLineEdit('3,4,2')
        self.xmin = QLineEdit('0')
        self.xmax = QLineEdit('10')
        self.anz = QLineEdit('20')
        self.farbe = QComboBox()
        self.farbe.addItems(['rot','grün','blau','schwarz'])
        button = QPushButton('Plot')

        layout_top.addWidget(self.canvas)
        layout_bottom.addRow('Koeffizienten:',self.koeff)
        layout_bottom.addRow('min:',self.xmin)
        layout_bottom.addRow('max:',self.xmax)
        layout_bottom.addRow('Anzahl Punkte:',self.anz)
        layout_bottom.addRow('Farbe:',self.farbe)
        layout_bottom.addRow(button)

        layout_top.addLayout(layout_bottom)

        center = QWidget()
        center.setLayout(layout_top)

        self.setCentralWidget(center)

        self.show()

        button.clicked.connect(self.plot)

    def plot(self):
        plt.clf()
        k = self.koeff.text()
        fa = self.farbe.currentText()
        a = int(self.xmin.text())
        b = int(self.xmax.text())
        anzahl = int(self.anz.text())
        try:
            k_eval = [float(x) for x in k.split(',')]
            f = np.poly1d(k_eval) 
            x = np.linspace(a,b,anzahl) 
            y = f(x)
            farbe = 'k'
            if fa == 'rot':
                farbe = 'r'
            elif fa == 'grün':
                farbe = 'g'
            elif fa == 'blau':
                farbe = 'b'
            code = f'{farbe}o-'

            plt.plot(x,y,str(code)) 
            #plt.axis('equal')
            self.canvas.draw()
        except:
            QMessageBox.critical(self, 'Fehler', 'überprüfen!')


app = QApplication([])
win = Fenster()
app.exec()
