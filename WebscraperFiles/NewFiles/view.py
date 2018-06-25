# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from software import Software


class CustomLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        self.clicked.emit()


class CustomLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(CustomLineEdit, self).__init__(parent)
        self.timer = QtCore.QTimer()
        self.suggestions = ["Enter a team",
                            "Enter a description", "Enter a year"]
        self.suggestionIndex = 0
        self.timer.timeout.connect(self.setSuggestions)
        self.timer.start(1000)

    # def mousePressEvent(self, event):
    #     super(CustomLineEdit, self).mousePressEvent(event)

    def focusInEvent(self, event):
        super(CustomLineEdit, self).focusInEvent(event)
        self.clear()
        self.timer.stop()

    def setSuggestions(self):
        if self.suggestionIndex > 2:
            self.suggestionIndex = 0
        self.setText(self.suggestions[self.suggestionIndex])
        self.suggestionIndex += 1


class CustomListWidget(QtWidgets.QWidget):
    def __init__(self, font, parent=None):
        super(CustomListWidget, self).__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        font.setPointSize(10)
        # font.setFamily(fontName)
        # font.setPointSize(12)
        font.setBold(True)
        self.teamLabel = QtWidgets.QLabel()
        self.teamLabel.setFont(font)
        self.teamLabel.setWordWrap(True)
        self.teamLabel.setStyleSheet('''
        QLabel {
            color: rgb(255, 255, 255);
            background: transparent;
        }
        ''')
        # font = QtGui.QFont()
        # font.setFamily(fontName)
        # font.setPointSize(12)
        font.setBold(False)
        self.descriptionLabel = QtWidgets.QLabel()
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignJustify)
        self.descriptionLabel.setStyleSheet('''
        QLabel {
            color: rgb(255, 255, 255);
            background: transparent;
            padding-right: 20px;
        }
        ''')
        # font = QtGui.QFont()
        # font.setFamily(fontName)
        # font.setPointSize(12)
        self.yearLabel = QtWidgets.QLabel()
        self.yearLabel.setFont(font)
        self.yearLabel.setWordWrap(True)
        self.yearLabel.setStyleSheet('''
        QLabel {
            color: rgb(255, 255, 255);
            background: transparent;
        }
        ''')
        self.textQVBoxLayout.addWidget(self.teamLabel)
        self.textQVBoxLayout.addWidget(self.descriptionLabel)
        self.textQVBoxLayout.addWidget(self.yearLabel)
        self.setLayout(self.textQVBoxLayout)

    def setTeamLabel(self, text):
        self.teamLabel.setText(text)

    def setDescriptionLabel(self, text):
        self.descriptionLabel.setText(text)

    def setYearLabel(self, text):
        self.yearLabel.setText(text)


class Ui_Form(object):
    def setupUi(self, Form):

        # Fonts
        fontDb = QtGui.QFontDatabase()
        fontId = fontDb.addApplicationFont('fonts/Raleway-Light.ttf')
        families = fontDb.applicationFontFamilies(fontId)
        self.font1 = QtGui.QFont(families[0])
        # fontId = fontDb.addApplicationFont('fonts/ReenieBeanie.ttf')
        # families = fontDb.applicationFontFamilies(fontId)
        # self.font2 = QtGui.QFont(families[0])
        # fontId = fontDb.addApplicationFont('fonts/Dosis-Regular.ttf')
        # families = fontDb.applicationFontFamilies(fontId)
        # self.font3 = QtGui.QFont(families[0])
        # End of Fonts

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
                           "outline: 0;\n"
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

        # View All Button
        self.label = CustomLabel(self.page)
        # self.label.setFont(self.font3)
        # self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(
            self.label, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # End of View All Button

        spacerItem = QtWidgets.QSpacerItem(
            20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem)

        # Close Button (1/3)
        self.label_3 = CustomLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(
            self.label_3, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        # End of Close Button (1/3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_5 = QtWidgets.QLabel(self.page)
        # font = QtGui.QFont()
        # font.setFamily("Century Gothic")
        # font.setPointSize(50)
        self.font1.setPointSize(60)
        self.label_5.setFont(self.font1)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(
            self.label_5, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_6 = QtWidgets.QLabel(self.page)
        # font = QtGui.QFont()
        # font.setFamily("Century Gothic")
        # font.setPointSize(26)
        self.font1.setPointSize(24)
        self.label_6.setFont(self.font1)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(
            self.label_6, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(
            360, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Line Edit
        self.lineEdit_2 = CustomLineEdit(self.page)
        # font = QtGui.QFont()
        # font.setFamily("Century Gothic")
        # font.setPointSize(20)
        self.font1.setPointSize(24)
        self.lineEdit_2.setFont(self.font1)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        # End of Line Edit

        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(
            360, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # Back Button (2/3)
        self.label_11 = CustomLabel(self.page_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(
            self.label_11, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # End of Back Button (2/3)

        spacerItem4 = QtWidgets.QSpacerItem(
            20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_11.addItem(spacerItem4)

        # Close Button (2/3)
        self.label_12 = CustomLabel(self.page_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(
            self.label_12, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        # End of Close Button (2/3)

        self.horizontalLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        # font = QtGui.QFont()
        # font.setFamily("Century Gothic")
        # font.setPointSize(26)
        self.font1.setPointSize(24)
        self.label_2.setFont(self.font1)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(
            self.label_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_4 = QtWidgets.QLabel(self.page_3)
        # font = QtGui.QFont()
        # font.setFamily("Century Gothic")
        # font.setPointSize(26)
        self.font1.setPointSize(24)
        self.label_4.setFont(self.font1)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(
            self.label_4, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Scrape Button
        self.label_13 = CustomLabel(self.page_3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(
            self.label_13, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # End of Scrape Button

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        # Back Button (3/3)
        self.label_7 = CustomLabel(self.page_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(
            self.label_7, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # End of Back Button (3/3)

        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_7.addItem(spacerItem6)

        # Close Button (3/3)
        self.label_8 = CustomLabel(self.page_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(
            self.label_8, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        # End of Close Button (3/3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        # font = QtGui.QFont()
        # font.setFamily("Century Gothic")
        # font.setPointSize(26)
        self.font1.setPointSize(26)
        self.label_9.setFont(self.font1)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_9.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.progressBar = QtWidgets.QProgressBar(self.page_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_8.addWidget(self.progressBar)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.label_10 = QtWidgets.QLabel(self.page_2)
        # font = QtGui.QFont()
        # font.setFamily("Century Gothic")
        # font.setPointSize(16)
        self.counter = 0
        self.font1.setPointSize(16)
        self.label_10.setFont(self.font1)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(
            self.label_10, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)

        # Custom List Widget
        self.softwareListWidget = QtWidgets.QListWidget(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.softwareListWidget.setFont(font)
        self.softwareListWidget.setStyleSheet("QScrollBar:vertical {\n"
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
        self.softwareListWidget.setObjectName("softwareListWidget")
        self.horizontalLayout_9.addWidget(self.softwareListWidget)
        # self.softwareListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        # End of Custom List Widget

        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem11 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        # self.stackedWidget.addWidget(self.page_2)
        self.doSomething(self.stackedWidget, self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def doSomething(self, sw, w):
        sw.addWidget(w)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate(
            "Form", "<html><head/><body><p><img src=\":/Image_2/BookIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_3.setText(_translate(
            "Form", "<html><head/><body><p><img src=\":/Image_1/CloseIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_5.setText(_translate("Form", "Hi, I\'m Sara"))
        self.label_6.setText(_translate("Form", "What are you looking for ?"))
        # self.lineEdit_2.setText(_translate("Form", "Enter a year"))
        self.label_11.setText(_translate(
            "Form", "<html><head/><body><p><img src=\":/Image_3/BackIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_12.setText(_translate(
            "Form", "<html><head/><body><p><img src=\":/Image_1/CloseIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_2.setText(_translate(
            "Form", "I don\'t think I have that year."))
        self.label_4.setText(_translate(
            "Form", "Would you like me to search the interweb ?"))
        self.label_13.setText(_translate(
            "Form", "<html><head/><body><p><img src=\":/Image_4/ForwardIcon.png\" height=\"50\"/></p></body></html>"))
        self.label_7.setText(_translate(
            "Form", "<html><head/><body><p><img src=\":/Image_3/BackIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_8.setText(_translate(
            "Form", "<html><head/><body><p><img src=\":/Image_1/CloseIcon.png\" height=\"30\"/></p></body></html>"))
        self.label_9.setText("Let me see what I can find...")
        self.label_10.setText(_translate("Form", "Results ( 0 )"))
        __sortingEnabled = self.softwareListWidget.isSortingEnabled()
        self.softwareListWidget.setSortingEnabled(False)
        self.softwareListWidget.setSortingEnabled(__sortingEnabled)

    def addSoftware(self, software):
        softwareWidget = CustomListWidget(self.font1)
        softwareWidget.setTeamLabel(software.team)
        softwareWidget.setDescriptionLabel(software.description)
        softwareWidget.setYearLabel(str(software.year))
        softwareWidgetItem = QtWidgets.QListWidgetItem(self.softwareListWidget)
        softwareWidgetItem.setSizeHint(softwareWidget.sizeHint())
        self.softwareListWidget.addItem(softwareWidgetItem)
        self.softwareListWidget.setItemWidget(
            softwareWidgetItem, softwareWidget)


import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
