from PyQt5 import QtCore, QtGui, QtWidgets
from software import Software
from webScraper import Parser
from intelligentParser import Summarizer
from bs4 import BeautifulSoup
import view
import sys
import requests
import csv


class Thread(QtCore.QThread):
    progress = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal()
    # cancelled = QtCore.pyqtSignal()
    result = QtCore.pyqtSignal(Software)

    def __init__(self, year):
        QtCore.QThread.__init__(self)
        self.year = year
        self.parser = Parser()

    def __del__(self):
        self.wait()

    def getData(self):
        teamInfo = self.parser.getData(self.year, self.progress)
        summarizer = Summarizer()
        summary = ''
        teamsWithSoftware = 0
        for i in range(len(teamInfo)):
            result = summarizer.summarize(teamInfo[i][1])
            if result['Success'] and len(result['TopNDescription']) > 0:
                teamInfo[i][1] = result['TopNDescription']
                teamsWithSoftware += 1
            else:
                teamInfo[i][1] = 'Unable to retrieve ' + \
                    teamInfo[i][0] + ' software.'
            software = Software(teamInfo[i][0], teamInfo[i][1], self.year)
            self.result.emit(software)
            self.progress.emit(50 / len(teamInfo))

    def run(self):
        self.getData()
        self.finished.emit()

    # def cancel(self):
    #     self.cancelled.emit()


class Ui(QtWidgets.QWidget, view.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # View All Button
        self.label.clicked.connect(self.viewAll)
        # End of View All Button

        # Close Button (1/3)
        self.label_3.clicked.connect(self.close)
        # End of Close Button (1/3)

        # Search Line Edit
        self.lineEdit_2.returnPressed.connect(self.startSearching)
        # self.lineEdit_2.mousePressEvent = self.erase
        # End of Search Line Edit

        # Back Button (2/3)
        self.label_11.clicked.connect(self.back)
        # End of Back Button (2/3)

        # Close Button (2/3)
        self.label_12.clicked.connect(self.close)
        # End of Close Button (2/3)

        # Scrape Button
        self.label_13.clicked.connect(self.startScraping)
        # End of Scrape Button

        # Back Button (3/3)
        self.label_7.clicked.connect(self.back)
        # End of Back Button (3/3)

        # Close Button (3/3)
        self.label_8.clicked.connect(self.close)
        # End of Close Button (3/3)

        self.setFocus()

    def mousePressEvent(self, event):
        focusedWidget = QtWidgets.QApplication.focusWidget()
        if isinstance(focusedWidget, view.CustomLineEdit):
            self.lineEdit_2.timer.start(1000)
            self.lineEdit_2.clearFocus()
        if isinstance(focusedWidget, QtWidgets.QListWidget):
            self.softwareListWidget.clearSelection()

    # def erase(self, event):
    #     if self.timer.isActive():
    #         self.lineEdit_2.setText("")
    #         self.timer.stop()

    def viewAll(self):
        self.counter = 0
        self.progressBar.hide()
        self.label_9.setText("All Software")
        self.softwareListWidget.clear()
        with open('software.csv', 'r', encoding='utf-8') as csvFile:
            csvReader = csv.reader(csvFile)
            for line in csvReader:
                software = Software(line[0], line[1], line[2])
                self.addSoftware(software)
                self.counter += 1
                self.label_10.setText("Results ( " + str(self.counter) + " )")
        self.stackedWidget.setCurrentIndex(2)

    def startSearching(self):
        self.progressBar.hide()
        self.softwareListWidget.clear()
        self.year = int(self.lineEdit_2.text())
        if not self.inDb(self.year):
            self.reset()
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.counter = 0
            self.label_9.setText("Software from " + str(self.year))
            with open('software.csv', 'r', encoding='utf-8') as csvFile:
                csvReader = csv.reader(csvFile)
                for line in csvReader:
                    if (int(line[2]) == self.year):
                        software = Software(line[0], line[1], line[2])
                        self.addSoftware(software)
                        self.counter += 1
                        self.label_10.setText(
                            "Results ( " + str(self.counter) + " )")
            self.stackedWidget.setCurrentIndex(2)

    def back(self):
        # self.lineEdit_2.clear()
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit_2.timer.start(1000)
        self.lineEdit_2.clearFocus()

    def startScraping(self):
        self.counter = 0
        self.label_9.setText("Let me see what I can find...")
        self.progressBar.show()
        self.label_10.setText(
            "Results ( " + str(self.counter) + " )")
        self.softwareListWidget.clear()
        self.year = int(self.lineEdit_2.text())
        self.thread = Thread(self.year)
        self.progressBar.setValue(0)
        self.thread.progress.connect(self.updateProgressBar)
        self.thread.result.connect(self.populate)
        self.thread.finished.connect(self.finish)
        # self.thread.cancelled.connect(self.cancel)
        self.thread.start()
        self.stackedWidget.setCurrentIndex(2)

    def updateProgressBar(self, val):
        self.progressBar.setValue(self.progressBar.value() + val)

    def inDb(self, year):
        with open('software.csv', 'r', encoding='utf-8') as csvFile:
            csvReader = csv.reader(csvFile)
            for line in csvReader:
                if (int(line[2]) == self.year):
                    return True

    def populate(self, software):
        self.addSoftware(software)
        self.counter += 1
        self.label_10.setText("Results ( " + str(self.counter) + " )")
        with open('software.csv', 'a', encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
            csvWriter.writerow(
                [software.team, "" + software.description + "", str(software.year)])

    def reset(self):
        self.progressBar.setValue(0)

    def finish(self):
        self.progressBar.setValue(100)
        # infoMessage = QtWidgets.QMessageBox()
        # infoMessage.setIcon(QtWidgets.QMessageBox.Information)
        # infoMessage.setText("Scrape finished!")
        # infoMessage.setWindowTitle("Finished")
        # infoMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # infoMessage.exec_()
        self.label_9.setText("Is it me you're looking for ?")
        self.progressBar.hide()
        self.reset()

    # def cancel(self):
    #     infoMessage = QtWidgets.QMessageBox()
    #     infoMessage.setIcon(QtWidgets.QMessageBox.Information)
    #     infoMessage.setText("Scrape cancelled!")
    #     infoMessage.setWindowTitle("Cancelled")
    #     infoMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #     infoMessage.exec_()
    #     self.reset()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    ui.show()
    app.exec_()


if __name__ == '__main__':
    main()
