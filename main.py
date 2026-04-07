from load.load_ventana_calculadora import VentanaCalculadora
from PyQt5 import QtWidgets
#para poder cargar la interfaz y se pueda cerrar
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaCalculadora()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()