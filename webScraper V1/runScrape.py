from webScraper import Parser
from intelligentParser import Summarizer

p = Parser()
teamInfo = p.getData('2008')

summarizer = Summarizer()
summary = ''

for i in range(len(teamInfo)):
	teamInfo[i][1] = summarizer.summarize(teamInfo[i][1]) 

