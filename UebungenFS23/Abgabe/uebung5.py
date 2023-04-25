from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.parse 

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
        self.button1 = QPushButton('Auf Karte zeigen')
        self.button2 = QPushButton('Laden')
        self.button3 = QPushButton('Speichern')


        # Elemente dem Layout hinzufügen 
        layout.addRow('Vorname:', self.vorname)
        layout.addRow('Name:', self.name)
        layout.addRow('Geburtsdatum:', self.gdatum)
        layout.addRow('Adresse:', self.adresse)
        layout.addRow('PLZ:', self.plz)
        layout.addRow('Ort:', self.ort)
        layout.addRow('Land:', self.land)
        layout.addRow(self.button1)
        layout.addRow(self.button2)
        layout.addRow(self.button3)

# -------------------------------------------------------------------------------------------------------

        #Menu erstellen        
        menubar = self.menuBar()
        
        filemenu = menubar.addMenu('File')
        viewmenu = menubar.addMenu('View')
        
        save = QAction('Speichern...', self)       
        filemenu.addAction(save)

        load = QAction('Laden...', self)       
        filemenu.addAction(load) 

        quit = QAction('Quit', self)       
        filemenu.addAction(quit)

        map = QAction('Karte...', self)       
        viewmenu.addAction(map)


# -------------------------------------------------------------------------------------------------------
   
        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

# -------------------------------------------------------------------------------------------------------

        self.button1.clicked.connect(self.maps)
        self.button2.clicked.connect(self.laden)
        self.button3.clicked.connect(self.speichern)
        save.triggered.connect(self.speichern)
        quit.triggered.connect(self.schliessen)
        map.triggered.connect(self.maps)
        load.triggered.connect(self.laden)

       
    def speichern(self):
        filename,filter = QFileDialog.getSaveFileName(self,'Datei speichern','','Text File (*.txt)')

        if filename == '':
            print('Abgebrochen')
        else:        
            file = open(filename, 'w', encoding='utf-8')        
            
            v = self.vorname.text()
            n = self.name.text() 
            g = self.gdatum.date().toString('dd.MM.yyyy')
            a = self.adresse.text()
            p = self.plz.text()
            o = self.ort.text()                       
            l = self.land.currentText()

            file.write(f'{v},{n},{g},{a},{p},{o},{l}')     
            file.close()

    def schliessen(self):
        self.close()

    def laden(self):
       
        filename,filter = QFileDialog.getOpenFileName(self,'Datei öffnen','','Text File (*.txt)')

        if filename == '':
            print('Abgebrochen')
        else:
            file = open(filename, 'r', encoding='utf-8') 

            for line in file: 
                line = line.strip() 
                daten = line.split(',')
                datum1 = daten[2].split('.')
                datum2 = QDate(int(datum1[2]),int(datum1[1]),int(datum1[0]))        

                self.vorname.setText(daten[0])
                self.name.setText(daten[1])
                self.gdatum.setDate(datum2)
                self.adresse.setText(daten[3])
                self.plz.setText(daten[4])
                self.ort.setText(daten[5])
                self.land.setCurrentText(daten[6])

            print(daten)

            file.close() 

    def maps(self):
        a = self.adresse.text()
        p = self.plz.text()
        o = self.ort.text()
        l = self.land.currentText()
        link = f"https://www.google.ch/maps/place/{a}+{p}+{o}+{l}" 
        print(link)
        QDesktopServices.openUrl(QUrl(link))
        
# -------------------------------------------------------------------------------------------------------

app = QApplication([])
win = Fenster()
app.exec()

