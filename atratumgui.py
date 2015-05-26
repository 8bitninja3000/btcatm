# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atratmgui.ui'
#
# Created: Thu May 14 22:00:05 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 615)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.status = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garamond"))
        font.setPointSize(10)
        self.status.setFont(font)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName(_fromUtf8("status"))
        self.verticalLayout_3.addWidget(self.status)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.price = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garamond"))
        font.setPointSize(48)
        font.setUnderline(False)
        self.price.setFont(font)
        self.price.setAlignment(QtCore.Qt.AlignCenter)
        self.price.setObjectName(_fromUtf8("price"))
        self.verticalLayout_3.addWidget(self.price)
        self.hline = QtGui.QFrame(self.centralwidget)
        self.hline.setLineWidth(4)
        self.hline.setFrameShape(QtGui.QFrame.HLine)
        self.hline.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline.setObjectName(_fromUtf8("hline"))
        self.verticalLayout_3.addWidget(self.hline)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.usdlim = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garamond"))
        font.setPointSize(10)
        self.usdlim.setFont(font)
        self.usdlim.setAlignment(QtCore.Qt.AlignCenter)
        self.usdlim.setObjectName(_fromUtf8("usdlim"))
        self.horizontalLayout_3.addWidget(self.usdlim)
        self.vline = QtGui.QFrame(self.centralwidget)
        self.vline.setLineWidth(4)
        self.vline.setFrameShape(QtGui.QFrame.VLine)
        self.vline.setFrameShadow(QtGui.QFrame.Sunken)
        self.vline.setObjectName(_fromUtf8("vline"))
        self.horizontalLayout_3.addWidget(self.vline)
        self.timestamp = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garamond"))
        font.setPointSize(10)
        self.timestamp.setFont(font)
        self.timestamp.setAlignment(QtCore.Qt.AlignCenter)
        self.timestamp.setObjectName(_fromUtf8("timestamp"))
        self.horizontalLayout_3.addWidget(self.timestamp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.hline_2 = QtGui.QFrame(self.centralwidget)
        self.hline_2.setLineWidth(4)
        self.hline_2.setFrameShape(QtGui.QFrame.HLine)
        self.hline_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline_2.setObjectName(_fromUtf8("hline_2"))
        self.verticalLayout_2.addWidget(self.hline_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Message = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garamond"))
        font.setPointSize(14)
        self.Message.setFont(font)
        self.Message.setAlignment(QtCore.Qt.AlignCenter)
        self.Message.setObjectName(_fromUtf8("Message"))
        self.verticalLayout.addWidget(self.Message)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.no = QtGui.QPushButton(self.centralwidget)
        self.no.setObjectName(_fromUtf8("no"))
        self.horizontalLayout_2.addWidget(self.no)
        self.yes = QtGui.QPushButton(self.centralwidget)
        self.yes.setObjectName(_fromUtf8("yes"))
        self.horizontalLayout_2.addWidget(self.yes)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.BV = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garamond"))
        font.setPointSize(11)
        self.BV.setFont(font)
        self.BV.setAlignment(QtCore.Qt.AlignCenter)
        self.BV.setObjectName(_fromUtf8("BV"))
        self.verticalLayout.addWidget(self.BV)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.status.setText(_translate("MainWindow", "Status: working", None))
        self.price.setText(_translate("MainWindow", "Price?", None))
        self.usdlim.setText(_translate("MainWindow", "Limit:", None))
        self.timestamp.setText(_translate("MainWindow", "As of:", None))
        self.Message.setText(_translate("MainWindow", "Press any button to scan the qr code.", None))
        self.no.setText(_translate("MainWindow", "No", None))
        self.yes.setText(_translate("MainWindow", "Yes", None))
        self.BV.setPlaceholderText(_translate("MainWindow", "Place holder for BV", None))

