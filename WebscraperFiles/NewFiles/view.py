# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        Form.setStyleSheet("QWidget {\n"
"background: rgb(4, 15, 15);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background: rgb(4, 15, 15);\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"}\n"
"\n"
"QListWidget {\n"
"background: rgb(4, 15, 15);\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"background: rgb(16, 61, 61);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"background: rgb(87, 115, 122);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_5 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_6 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(360, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(360, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(26)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.progressBar = QtWidgets.QProgressBar(self.page_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_8.addWidget(self.progressBar)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.label_10 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QScrollBar:vertical {\n"
"border: 1px solid #ffffff;\n"
"background: white;\n"
"width: 10px;\n"
"margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(4, 15, 15), stop: 0.5 rgb(4, 15, 15), stop:1 rgb(4, 15, 15));\n"
"min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(4, 15, 15), stop: 0.5 rgb(4, 15, 15),  stop:1 rgb(4, 15, 15));\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0  rgb(4, 15, 15), stop: 0.5 rgb(4, 15, 15),  stop:1 rgb(4, 15, 15));\n"
"height: 0 px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_9.addWidget(self.listWidget)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><img src=\":/Image_2/BookIcon.png\" height=\"30\"/><span style=\" font-size:16pt;\"> View All</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><img src=\":/Image_1/CloseIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_5.setText(_translate("Form", "Hi, I\'m Gabe"))
        self.label_6.setText(_translate("Form", "What kind of software are you looking for ?"))
        self.lineEdit_2.setText(_translate("Form", "Enter a description"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><img src=\":/Image_3/BackIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><img src=\":/Image_1/CloseIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"center\">Let me see what I can find...</p></body></html>"))
        self.label_10.setText(_translate("Form", "Results (1) :"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Software 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Software 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "Software 3"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "Software 4"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "Software 5"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "Software 6"))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "Software 7"))
        item = self.listWidget.item(7)
        item.setText(_translate("Form", "Software 8"))
        item = self.listWidget.item(8)
        item.setText(_translate("Form", "Software 9"))
        item = self.listWidget.item(9)
        item.setText(_translate("Form", "Software 10"))
        item = self.listWidget.item(10)
        item.setText(_translate("Form", "Software 11"))
        item = self.listWidget.item(11)
        item.setText(_translate("Form", "Software 12"))
        item = self.listWidget.item(12)
        item.setText(_translate("Form", "Software 13"))
        item = self.listWidget.item(13)
        item.setText(_translate("Form", "Software 14"))
        item = self.listWidget.item(14)
        item.setText(_translate("Form", "Software 15"))
        item = self.listWidget.item(15)
        item.setText(_translate("Form", "Software 16"))
        item = self.listWidget.item(16)
        item.setText(_translate("Form", "Software 17"))
        item = self.listWidget.item(17)
        item.setText(_translate("Form", "Software 18"))
        item = self.listWidget.item(18)
        item.setText(_translate("Form", "Software 19"))
        item = self.listWidget.item(19)
        item.setText(_translate("Form", "Software 20"))
        item = self.listWidget.item(20)
        item.setText(_translate("Form", "Software 21"))
        item = self.listWidget.item(21)
        item.setText(_translate("Form", "Software 22"))
        item = self.listWidget.item(22)
        item.setText(_translate("Form", "Software 23"))
        item = self.listWidget.item(23)
        item.setText(_translate("Form", "Software 24"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

