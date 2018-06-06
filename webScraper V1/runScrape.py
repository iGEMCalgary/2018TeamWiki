from webScraper import Parser
from intelligentParser import Summarizer

year = input("Please enter a year: ")

p = Parser()
teamInfo = p.getData(year)

summarizer = Summarizer()
summary = ''

for i in range(len(teamInfo)):
	teamInfo[i][1] = summarizer.summarize(teamInfo[i][1]) 

