from PyQt5 import uic, QtCore, QtGui, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="cadastro_produtos",
    auth_plugin='mysql_native_password'
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
        self.labelCodigo.setText(_translate("MainWindow", "C??DIGO:"))
        self.labelDesc.setText(_translate("MainWindow", "DESCRI????O:"))
        self.labelPreco.setText(_translate("MainWindow", "PRE??O:"))
        self.radioInfo.setText(_translate("MainWindow", "Inform??tica"))
        self.radioEletro.setText(_translate("MainWindow", "Eletr??nicos"))
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
        print("Categoria Inform??tica selecionada. \n")
        categoria = "Informatica"
    elif cadastro.radioEletro.isChecked():
        print("Categoria Eletr??nicos selecionada. \n")
        categoria = "Eletronicos"
    else:
        print("Categoria Alimentos selecionada. \n")
        categoria = "Alimentos"

    print("C??digo: ", linha1)
    print("Descri????o: ", linha2)
    print("Pre??o: ", linha3)
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES(%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    cadastro.linhaCodigo.setText("")
    cadastro.linhaDesc.setText("")
    cadastro.linhaPreco.setText("")


def funcao_consultar():
    consultar.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * from produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    consultar.tableWidget.setRowCount(len(dados_lidos))
    consultar.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            consultar.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def funcao_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Produtos Cadastrados: ")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110, 750, "C??DIGO")
    pdf.drawString(210, 750, "PRODUTO")
    pdf.drawString(310, 750, "PRE??O")
    pdf.drawString(410, 750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410, 750 - y, str(dados_lidos[i][4]))


    pdf.save()
    print("PDF GERADO COM SUCESSO!")


def funcao_excluir():
    linha = consultar.tableWidget.currentRow()
    consultar.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))


def funcao_editar():
    global numero_id
    linha = consultar.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id=" + str(valor_id))
    produto = cursor.fetchall()
    editar.show()

    numero_id = valor_id

    editar.lineEdit.setText(str(produto[0][0]))
    editar.lineEdit_2.setText(str(produto[0][1]))
    editar.lineEdit_3.setText(str(produto[0][2]))
    editar.lineEdit_4.setText(str(produto[0][3]))
    editar.lineEdit_5.setText(str(produto[0][4]))


def funcao_salvar():
    #pega o numero do id
    global numero_id
    #valor digitado no lineedit
    codigo = editar.lineEdit_2.text()
    descricao = editar.lineEdit_3.text()
    preco = editar.lineEdit_4.text()
    categoria = editar.lineEdit_5.text()
    #atualizar o DATABASE
    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET codigo = '{}', descricao = '{}', preco = '{}', categoria ='{}' WHERE id = {}".format(codigo,descricao,preco,categoria,numero_id))
    banco.commit()
    #atualizar as janelas
    editar.close()
    consultar.close()
    funcao_consultar()


app = QtWidgets.QApplication([])
cadastro = uic.loadUi("Cadastro1.ui")
consultar = uic.loadUi("Consultar1.ui")
editar = uic.loadUi("Editar1.ui")
cadastro.buttonEnviar.clicked.connect(funcao_principal)
cadastro.buttonConsulta.clicked.connect(funcao_consultar)
consultar.buttonPDF.clicked.connect(funcao_pdf)
consultar.buttonExcluir.clicked.connect(funcao_excluir)
consultar.buttonEditar.clicked.connect(funcao_editar)
editar.buttonSalvar.clicked.connect(funcao_salvar)


cadastro.show()
app.exec()
