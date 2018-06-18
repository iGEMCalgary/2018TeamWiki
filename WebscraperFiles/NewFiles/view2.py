from PyQt5 import QtCore, QtGui, QtWidgets
import homepage
import resultspage
import sys


class View(QtWidgets.QWidget):
    def __init__(self):
        super(View, self).__init__()

        # self.list = QtWidgets.QListWidget()
        # self.list.insertItem(0, 'Home')
        # self.list.insertItem(1, 'Results')

        self.homeStack = QtWidgets.QMainWindow()
        self.resultsStack = QtWidgets.QWidget()

        self.setupHomeUI()
        self.setupResultsUI()

        self.stack = QtWidgets.QStackedWidget(self)
        self.stack.addWidget(self.homeStack)
        self.stack.addWidget(self.resultsStack)

        # hbox = QtWidgets.QHBoxLayout(self)
        # hbox.addWidget(self.list)
        # hbox.addWidget(self.stack)

        # self.setLayout(hbox)
        # self.list.currentRowChanged.connect(self.display)
        self.setWindowTitle('Demo')
        # self.setFixedSize(self.stack.sizeHint())
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def setupHomeUI(self):
        homeUi = homepage.Ui_MainWindow()
        homeUi.setupUi(self.homeStack)
        homeUi.lineEdit.returnPressed.connect(self.displayResults)

    def setupResultsUI(self):
        resultsUi = resultspage.Ui_Form()
        resultsUi.setupUi(self.resultsStack)
        resultsUi.label_4.mousePressEvent = self.displayHome

    def displayHome(self, event):
        self.stack.setCurrentIndex(0)

    def displayResults(self):
        self.stack.setCurrentIndex(1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
