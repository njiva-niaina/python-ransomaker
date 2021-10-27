from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(310, 435)
        # Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setMinimumSize(QtCore.QSize(310, 435))
        Form.setMaximumSize(QtCore.QSize(310, 435))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("QPushButton#pushButton{\n"
"    background-color:rgba(2,65,118,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:focus{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2,65,118,100);\n"
"    background-position:calc(100% - 10px) center;\n"
"}\n"
"\n"
"QPushButton#pushButton{\n"
"    background-color:rgba(2,65,118,200);\n"
"}\n"
"\n"
"\n"
"")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 290, 410))
        self.widget.setStyleSheet("background-color: rgb(16, 30, 41,204);\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 290, 190))
        self.label.setObjectName("label")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 250, 250, 30))
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 300, 250, 30))
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 200, 250, 30))
        self.lineEdit_1.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgba(255,255,255,250);\n"
"padding-bottom:7px")
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 350, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 110, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/icons8-ransomware-64.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 250, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(0, 125, 236, 255);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Adresse IP"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Port"))
        self.lineEdit_1.setPlaceholderText(_translate("Form", "Nom du fichier"))
        self.pushButton.setText(_translate("Form", "Générer les ransomfiles"))
        self.label_3.setText(_translate("Form", "Ransomaker"))
import resource_rc
