from PyQt5 import QtWidgets, uic
from clases.calculadora import Calculadora


class VentanaCalculadora(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_calculadora.ui", self)
        self.show()
        self.boton_sumar.clicked.connect(self.botonSumarClick)

    def botonSumarClick(self):
        # Usar los nombres correctos del .ui
        try:
            num1 = int(self.adit_numero1.text())
            num2 = int(self.edit_numero2.text())
        except Exception:
            self.label_Resultado.setText("Entrada no válida")
            return
        cal = Calculadora(num1, num2)
        cal.calcularSuma()
        self.label_Resultado.setText(str(cal.resultado))