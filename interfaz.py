import imp
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QDialog
from PyQt5 import uic
from concecionario import Concesionario
from PyQt5.QtGui import QStandardItemModel

class VentanaConcesionario(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        uic.loadUi("interfaz/MainWindowConcesionario.ui", self)
        self.setFixedSize(self.size())
        self.Concesionario = Concesionario()
        self.dialogoAgregarCarro = DialogoAgregarCarro

    def configurar(self):
        # configurar qlistview
        self.list_view_carros.setModel(QStandardItemModel())

        #enlazar los botones
        self.pbutton_registrar_carro.clicked.connect(self.abrir_dialogo_registrar_carro)

    def CargarDatos():
        pass

    def abrir_dialogo_registrar_carro(self):
        respuesta = self.dialogoAgregarCarro.exec()
        if respuesta == QDialog.Accepted:
            color = self.dialogoAgregarCarro.le_color.text()
            placa = self.dialogoAgregarCarro.le_placa.text()
            marca = self.dialogoAgregarCarro.le_marca.text()
            modelo = self.dialogoAgregarCarro.le_modelo.text()
            precio = float(self.dialogoAgregarCarro.le_precio.text())
            año = self.dialogoAgregarCarro.le_ano.text()
            self.Concesionario.Cargar_catalogo(color,placa,marca,modelo,precio,año)


class DialogoAgregarCarro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("interfaz/Dialogo_agregarCarro.ui", self)
        self.setFixedSize(self.size())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = VentanaConcesionario()
    win.show()

    sys.exit(app.exec_())





