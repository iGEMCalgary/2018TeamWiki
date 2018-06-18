from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup
from software import Software
from webScraper import Parser
from intelligentParser import Summarizer
import sys
import view
import requests
import csv


class Thread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    cancelled = pyqtSignal()
    result = pyqtSignal(Software)

    def __init__(self, year):
        QThread.__init__(self)
        self.year = year
        self.p = Parser()

    def __del__(self):
        self.wait()

    def getData(self):
        teamInfo = self.p.getData(self.year)
        self.progress.emit(50)
        summarizer = Summarizer()
        summary = ''
        teamsWithSoftware = 0
        for i in range(len(teamInfo)):
            result = summarizer.summarize(teamInfo[i][1])
            if result['Success'] and len(result['TopNDescription']) > 0:
                teamInfo[i][1] = result['TopNDescription']
                # print(teamInfo[i][0])
                # print(teamInfo[i][1])
                teamsWithSoftware += 1
            else:
                teamInfo[i][1] = 'Unable to retrieve ' + \
                    teamInfo[i][0] + ' software.'
            software = Software(teamInfo[i][0], teamInfo[i][1], self.year)
            self.result.emit(software)
            self.progress.emit(50 / len(teamInfo))

    # def getLinks(self, teamWikisPageContent):
    #     links = []
    #     for link in teamWikisPageContent.findAll('a'):
    #         links.append(link['href'] + "/Software")
    #     self.progress.emit(25)
    #     return links

    # def getLinksWithContent(self, links):
    #     linksWithContent = []
    #     for i in range(0, len(links), 1):
    #         wikiSource = requests.get(links[i]).text
    #         if "There is currently no text in this page." in wikiSource or "In order to be considered for the" in \
    #                 wikiSource or "you must fill this page." in wikiSource or "This page is used by the judges to " \
    #                 "evaluate your team for the" in wikiSource or "Regardless of the topic, iGEM projects often create " \
    #                 "or adapt computational tools to move the project forward." in wikiSource:
    #             pass
    #         else:
    #             linksWithContent.append(links[i])
    #     self.progress.emit(25)
    #     return linksWithContent

    # def getLinkDescriptions(self, linksWithContent, year):
    #     software = []
    #     for i in range(0, len(linksWithContent), 1):
    #         description = ""
    #         wikiWithContentSource = requests.get(linksWithContent[i]).text
    #         wikiWithContentSoup = BeautifulSoup(wikiWithContentSource, 'lxml')
    #         wikiWithContentContent = wikiWithContentSoup.find(
    #             'div', id='bodyContent')
    #         paragraphs = []
    #         for paragraph in wikiWithContentContent.findAll('p'):
    #             temp = "".join(line.strip()
    #                            for line in paragraph.text.split("\n"))
    #             if "<style" in str(paragraph) or "</style>" in str(paragraph) or "<script" in str(paragraph) or \
    #                     "</script>" in str(paragraph) or len(temp) == 0:
    #                 pass
    #             else:
    #                 paragraphs.append("".join(line.strip()
    #                                           for line in paragraph.text.split("\n")))
    #         j = 0
    #         while len(description) < 500 and j < len(paragraphs):
    #             k = 0
    #             while len(description) < 500 and k < len(paragraphs[j]):
    #                 description += paragraphs[j][k]
    #                 k += 1
    #             j += 1
    #             description += " "
    #         description += "..."
    #         software = Software(linksWithContent[i].split(
    #             "/")[3].split(":")[1], description, year)
    #         self.result.emit(software)
    #         self.progress.emit(50 / len(linksWithContent))

    # def scrape(self, year):
    #     teamWikisPageSource = requests.get(
    #         'http://igem.org/Team_Wikis?year=' + str(year)).text
    #     teamWikisPageSoup = BeautifulSoup(teamWikisPageSource, 'lxml')
    #     teamWikisPageContent = teamWikisPageSoup.find('div', id='content_Page')
    #     links = self.getLinks(teamWikisPageContent)
    #     linksWithContent = self.getLinksWithContent(links)
    #     linkDescriptions = self.getLinkDescriptions(linksWithContent, year)

    def run(self):
        # self.scrape(self.year)
        self.getData()
        self.finished.emit()

    def cancel(self):
        self.cancelled.emit()


class Ui(QtWidgets.QMainWindow, view.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.checkCsvPushButton.clicked.connect(self.startChecking)
        self.scrapePushButton.clicked.connect(self.startScraping)

    def startChecking(self):
        self.softwareListWidget.clear()
        try:
            self.year = int(self.yearLineEdit.text())
            if not self.alreadyScraped(self.year):
                self.reset()
                infoMessage = QtWidgets.QMessageBox()
                infoMessage.setIcon(QtWidgets.QMessageBox.Information)
                infoMessage.setText(
                    "Year not yet scraped. Press \"Scrape\" to scrape the year you've entered.")
                infoMessage.setWindowTitle("Not Yet Scraped")
                infoMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
                infoMessage.exec_()
            else:
                with open('software2.csv', 'r', encoding='utf-8') as csvFile:
                    csvReader = csv.reader(csvFile)
                    for line in csvReader:
                        if (int(line[2]) == self.year):
                            software = Software(line[0], line[1], line[2])
                            self.addSoftware(software)
        except Exception:
            errorMessage = QtWidgets.QMessageBox()
            errorMessage.setIcon(QtWidgets.QMessageBox.Critical)
            errorMessage.setText("Please enter a year.")
            errorMessage.setWindowTitle("Invalid Input")
            errorMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
            errorMessage.exec_()

    def startScraping(self):
        self.softwareListWidget.clear()
        try:
            self.year = int(self.yearLineEdit.text())
            if not self.alreadyScraped(self.year):
                self.thread = Thread(self.year)
                self.progressBar.setValue(0)
                self.thread.progress.connect(self.updateProgressBar)
                self.thread.result.connect(self.populate)
                self.thread.finished.connect(self.finish)
                self.thread.cancelled.connect(self.cancel)
                self.thread.start()
                self.checkCsvPushButton.setEnabled(False)
                self.scrapePushButton.setEnabled(False)
                self.stopPushButton.setEnabled(True)
                self.stopPushButton.clicked.connect(self.thread.cancel)
            else:
                self.reset()
                infoMessage = QtWidgets.QMessageBox()
                infoMessage.setIcon(QtWidgets.QMessageBox.Information)
                infoMessage.setText(
                    "Year already scraped. Press \"Check CSV\" to view software.")
                infoMessage.setWindowTitle("Already Scraped")
                infoMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
                infoMessage.exec_()
        except Exception:
            errorMessage = QtWidgets.QMessageBox()
            errorMessage.setIcon(QtWidgets.QMessageBox.Critical)
            errorMessage.setText("Please enter a year.")
            errorMessage.setWindowTitle("Invalid Input")
            errorMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
            errorMessage.exec_()

    def updateProgressBar(self, val):
        self.progressBar.setValue(self.progressBar.value() + val)

    def alreadyScraped(self, year):
        with open('software2.csv', 'r', encoding='utf-8') as csvFile:
            csvReader = csv.reader(csvFile)
            for line in csvReader:
                if (int(line[2]) == self.year):
                    return True

    def populate(self, software):
        self.addSoftware(software)
        with open('software2.csv', 'a', encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
            csvWriter.writerow(
                [software.team, "" + software.description + "", str(software.year)])

    def reset(self):
        self.progressBar.setValue(0)
        self.checkCsvPushButton.setEnabled(True)
        self.scrapePushButton.setEnabled(True)
        self.stopPushButton.setEnabled(False)

    def finish(self):
        self.progressBar.setValue(100)
        infoMessage = QtWidgets.QMessageBox()
        infoMessage.setIcon(QtWidgets.QMessageBox.Information)
        infoMessage.setText("Scrape finished!")
        infoMessage.setWindowTitle("Finished")
        infoMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
        infoMessage.exec_()
        self.reset()

    def cancel(self):
        infoMessage = QtWidgets.QMessageBox()
        infoMessage.setIcon(QtWidgets.QMessageBox.Information)
        infoMessage.setText("Scrape cancelled!")
        infoMessage.setWindowTitle("Cancelled")
        infoMessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
        infoMessage.exec_()
        self.reset()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    ui.showMaximized()
    app.exec_()


if __name__ == '__main__':
    main()
