from PyQt5 import uic, QtCore, QtGui, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 531)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(110, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(20)
        font.setUnderline(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelCodigo = QtWidgets.QLabel(self.centralwidget)
        self.labelCodigo.setGeometry(QtCore.QRect(70, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(16)
        self.labelCodigo.setFont(font)
        self.labelCodigo.setObjectName("labelCodigo")
        self.labelDesc = QtWidgets.QLabel(self.centralwidget)
        self.labelDesc.setGeometry(QtCore.QRect(70, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(16)
        self.labelDesc.setFont(font)
        self.labelDesc.setObjectName("labelDesc")
        self.labelPreco = QtWidgets.QLabel(self.centralwidget)
        self.labelPreco.setGeometry(QtCore.QRect(70, 250, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(16)
        self.labelPreco.setFont(font)
        self.labelPreco.setObjectName("labelPreco")
        self.linhaCodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.linhaCodigo.setGeometry(QtCore.QRect(190, 150, 191, 31))
        self.linhaCodigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linhaCodigo.setObjectName("linhaCodigo")
        self.linhaDesc = QtWidgets.QLineEdit(self.centralwidget)
        self.linhaDesc.setGeometry(QtCore.QRect(190, 200, 191, 31))
        self.linhaDesc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linhaDesc.setObjectName("linhaDesc")
        self.linhaPreco = QtWidgets.QLineEdit(self.centralwidget)
        self.linhaPreco.setGeometry(QtCore.QRect(190, 250, 191, 31))
        self.linhaPreco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linhaPreco.setObjectName("linhaPreco")
        self.radioInfo = QtWidgets.QRadioButton(self.centralwidget)
        self.radioInfo.setGeometry(QtCore.QRect(270, 340, 101, 17))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(12)
        self.radioInfo.setFont(font)
        self.radioInfo.setObjectName("radioInfo")
        self.radioEletro = QtWidgets.QRadioButton(self.centralwidget)
        self.radioEletro.setGeometry(QtCore.QRect(270, 370, 101, 17))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(12)
        self.radioEletro.setFont(font)
        self.radioEletro.setObjectName("radioEletro")
        self.radioAlimentos = QtWidgets.QRadioButton(self.centralwidget)
        self.radioAlimentos.setGeometry(QtCore.QRect(270, 400, 91, 16))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(12)
        self.radioAlimentos.setFont(font)
        self.radioAlimentos.setObjectName("radioAlimentos")
        self.labelCategoria = QtWidgets.QLabel(self.centralwidget)
        self.labelCategoria.setGeometry(QtCore.QRect(146, 370, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(16)
        self.labelCategoria.setFont(font)
        self.labelCategoria.setObjectName("labelCategoria")
        self.buttonEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEnviar.setGeometry(QtCore.QRect(170, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(16)
        self.buttonEnviar.setFont(font)
        self.buttonEnviar.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.buttonEnviar.setObjectName("buttonEnviar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitulo.setText(_translate("MainWindow", "Cadastro de Produtos"))
        self.labelCodigo.setText(_translate("MainWindow", "CÓDIGO:"))
        self.labelDesc.setText(_translate("MainWindow", "DESCRIÇÃO:"))
        self.labelPreco.setText(_translate("MainWindow", "PREÇO:"))
        self.radioInfo.setText(_translate("MainWindow", "Informática"))
        self.radioEletro.setText(_translate("MainWindow", "Eletrônicos"))
        self.radioAlimentos.setText(_translate("MainWindow", "Alimentos"))
        self.labelCategoria.setText(_translate("MainWindow", "CATEGORIA"))
        self.buttonEnviar.setText(_translate("MainWindow", "ENVIAR"))


if __name__ == "__cadastroProj__":#COLOCAR O NOME IGUAL O DO ARQUIVO
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def funcao_principal():
    linha1 = cadastro.linhaCodigo.text()
    linha2 = cadastro.linhaDesc.text()
    linha3 = cadastro.linhaPreco.text()
    categoria = ""

    if cadastro.radioInfo.isChecked():
        print("Categoria Informática selecionada. \n")
        categoria = "Informatica"
    elif cadastro.radioEletro.isChecked():
        print("Categoria Eletrônicos selecionada. \n")
        categoria = "Eletronicos"
    else:
        print("Categoria Alimentos selecionada. \n")
        categoria = "Alimentos"

    print("Código: ", linha1)
    print("Descrição: ", linha2)
    print("Preço: ", linha3)
    cursor = banco.cursor()
    comando_SQL = "insert into produtos (codigo, descricao, preco, categoria) VALUES(%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execite(comando_SQL, dados)
    banco.commit()


app = QtWidgets.QApplication([])
cadastro = uic.loadUi("Cadastro1.ui")
cadastro.buttonEnviar.clicked.connect(funcao_principal)

cadastro.show()
app.exec()
