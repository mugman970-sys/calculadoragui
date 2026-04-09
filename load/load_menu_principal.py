from PyQt5 import QtWidgets, uic
from load.load_ventana_calculadora import VentanaCalculadora

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)
        self.showMaximized()
        self.actionCalculadora.triggered.connect(self.ingresarCalculadora)
        self.actionSalir.triggered.connect(self.salir)
    def ingresarCalculadora(self):
        vc = VentanaCalculadora()
        vc.exec_()
    def salir(self):
        self.close()