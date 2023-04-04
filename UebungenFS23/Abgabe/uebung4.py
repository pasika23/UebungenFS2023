from PyQt5.QtWidgets import *
import csv

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GUI Programmierung')

        #layout erzeugen
        # layout = ... (QV)
        layout = QFormLayout()

        # Elemente erzeugen
        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.gdatum = QDateEdit()
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Land auswählen","Schweiz", "Deutschland", "Oesterreich"])
        self.button = QPushButton('Save')


        # Elemente dem Layout hinzufügen 
        layout.addRow('Vorname:', self.vorname)
        layout.addRow('Name:', self.name)
        layout.addRow('Geburtsdatum:', self.gdatum)
        layout.addRow('Adresse:', self.adresse)
        layout.addRow('PLZ:', self.plz)
        layout.addRow('Ort:', self.ort)
        layout.addRow('Land:', self.land)
        layout.addRow(self.button)

        #Menu erstellen        
        menubar = self.menuBar()
        
        filemenu = menubar.addMenu('File')
        
        save = QAction('Save', self)       
        filemenu.addAction(save) 

        quit = QAction('Quit', self)       
        filemenu.addAction(quit)
        
        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

        self.button.clicked.connect(self.speichern)
        save.triggered.connect(self.speichern)
        quit.triggered.connect(self.schliessen)

       

    def speichern(self):
        file = open('output.csv', 'w', encoding='utf-8')        
        writer = csv.writer(file, delimiter=',')
        writer.writerow([self.vorname.text(), 
                self.name.text(), 
                self.gdatum.date().toString('dd.MM.yyyy'), 
                self.adresse.text(), 
                self.plz.text(), 
                self.ort.text(),                       
                self.land.currentText()])      
        file.close()

    def schliessen(self):
        self.close()

app = QApplication([])
win = Fenster()
app.exec()

