from PyQt5 import QtCore, QtGui, QtWidgets
from software import Software


class SoftwareWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SoftwareWidget, self).__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()

        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        font.setBold(True)
        self.teamLabel = QtWidgets.QLabel()
        self.teamLabel.setFont(font)
        self.teamLabel.setWordWrap(True)

        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.descriptionLabel = QtWidgets.QLabel()
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setWordWrap(True)
        # self.descriptionLabel.setContentsMargins

        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.yearLabel = QtWidgets.QLabel()
        self.yearLabel.setFont(font)
        self.yearLabel.setWordWrap(True)

        self.textQVBoxLayout.addWidget(self.teamLabel)
        self.textQVBoxLayout.addWidget(self.descriptionLabel)
        self.textQVBoxLayout.addWidget(self.yearLabel)
        # self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        # self.allQHBoxLayout.addWidget(self.teamLabel, 0)
        # self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.textQVBoxLayout)
        # self.descriptionLabel.setStyleSheet('''
        # word-wrap: normal;
        # ''')
        # self.yearLabel.setStyleSheet('''
        # color: rgb(255, 0, 0);
        # ''')

    def setTeamLabel(self, text):
        self.teamLabel.setText(text)

    def setDescriptionLabel(self, text):
        self.descriptionLabel.setText(text)

    def setYearLabel(self, text):
        self.yearLabel.setText(text)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.softwareLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(True)
        # font.setWeight(75)
        self.softwareLabel.setFont(font)
        self.softwareLabel.setObjectName("softwareLabel")
        self.verticalLayout.addWidget(
            self.softwareLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.instructionsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.instructionsLabel.setFont(font)
        self.instructionsLabel.setWordWrap(True)
        self.instructionsLabel.setObjectName("label")
        self.verticalLayout.addWidget(self.instructionsLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.enterYearLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.enterYearLabel.setFont(font)
        self.enterYearLabel.setObjectName("enterYearLabel")
        self.horizontalLayout.addWidget(self.enterYearLabel)
        self.yearLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        self.yearLineEdit.setFont(font)
        self.yearLineEdit.setText("")
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.horizontalLayout.addWidget(self.yearLineEdit)
        self.checkCsvPushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkCsvPushButton.setFont(font)
        self.checkCsvPushButton.setObjectName("checkCsvPushButton")
        self.horizontalLayout.addWidget(self.checkCsvPushButton)
        self.scrapePushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.scrapePushButton.setFont(font)
        self.scrapePushButton.setObjectName("scrapePushButton")
        self.horizontalLayout.addWidget(self.scrapePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.resultsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(10)
        self.resultsLabel.setFont(font)
        self.resultsLabel.setObjectName("resultsLabel")
        self.verticalLayout.addWidget(
            self.resultsLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # self.resultsTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        # font = QtGui.QFont()
        # font.setFamily("Tw Cen MT")
        # self.resultsTextBrowser.setFont(font)
        # self.resultsTextBrowser.setObjectName("resultsTextBrowser")
        # self.verticalLayout.addWidget(self.resultsTextBrowser)

        self.softwareListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.softwareListWidget.setObjectName("softwareListWidget")
        self.verticalLayout.addWidget(self.softwareListWidget)

        # software = Software("UofC", "It was pretty good.", "2017")
        # self.addSoftware(software)
        # self.addSoftware(software)

        # customJunk = SoftwareWidget()
        # customJunk.setTeamLabel("UofC")
        # customJunk.setDescriptionLabel("Good")
        # customJunk.setYearLabel("2017")
        # notCustomJunk = QtWidgets.QListWidgetItem(self.softwareListWidget)
        # notCustomJunk.setSizeHint(customJunk.sizeHint())
        # self.softwareListWidget.addItem(notCustomJunk)
        # self.softwareListWidget.setItemWidget(notCustomJunk, customJunk)

        self.stopPushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stopPushButton.setFont(font)
        self.stopPushButton.setObjectName("stopPushButton")
        self.stopPushButton.setEnabled(False)
        self.verticalLayout.addWidget(self.stopPushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "iGEM Software Aggregator"))
        self.softwareLabel.setText(_translate(
            "MainWindow", "iGEM Software Aggregator"))
        self.instructionsLabel.setText(_translate(
            "MainWindow", "Instructions: Choose \"Check CSV\" if you have already scraped the year you\'ve entered. Choose \"Scrape\" if not."))
        self.enterYearLabel.setText(_translate(
            "MainWindow", "Enter year here:"))
        self.checkCsvPushButton.setText(_translate("MainWindow", "Check CSV"))
        self.scrapePushButton.setText(_translate("MainWindow", "Scrape"))
        self.resultsLabel.setText(_translate("MainWindow", "Results"))
        # self.resultsTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        #                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        #                                            "p, li { white-space: pre-wrap; }\n"
        #                                            "</style></head><body style=\" font-family:\'Tw Cen MT\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
        #                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.stopPushButton.setText(_translate("MainWindow", "Stop"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def addSoftware(self, software):
        softwareWidget = SoftwareWidget()
        softwareWidget.setTeamLabel(software.team)
        softwareWidget.setDescriptionLabel(software.description)
        softwareWidget.setYearLabel(str(software.year))
        softwareWidgetItem = QtWidgets.QListWidgetItem(self.softwareListWidget)
        softwareWidgetItem.setSizeHint(softwareWidget.sizeHint())
        self.softwareListWidget.addItem(softwareWidgetItem)
        self.softwareListWidget.setItemWidget(
            softwareWidgetItem, softwareWidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
