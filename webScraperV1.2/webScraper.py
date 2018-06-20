from bs4 import BeautifulSoup
import requests
import webbrowser
import time
import sys
from html.parser import HTMLParser
import lxml
from lxml.html.clean import Cleaner

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.strict = False
		self.convert_charrefs= True
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)
		
class Parser():	

	def stripTags(self, text):
		s = MLStripper()
		s.feed(text)
		return s.get_data()
	
	##
	#	getSoftLinks:
	#		Returns all populated software wikis links for the year (array)
	#		Note: Year functionality not implemented
	##
	
	def getSoftLinks(self, year):	
		links = []							# All possible software pages
		linksWithSoftware = []		# All populated software pages
		
		try:
			source = requests.get('http://igem.org/Team_Wikis?year=' + year).text

		except requests.ConnectionError as e:
			print(e)
		except Exception as e:
			print(e.__class__.__name__)
		
		soup = BeautifulSoup(source, 'lxml')
		content = soup.find('div', id='content_Page')

		for wiki in content.findAll('a'):
			links.append(wiki['href'] + "/Software")

		for i in range(0, len(links), 1):
			wikiSource = requests.get(links[i]).text
			if "There is currently no text in this page." in wikiSource or\
				"In order to be considered for the" in wikiSource or\
				"you must fill this page." in wikiSource or\
				"This page is used by the judges to evaluate your team for the" in wikiSource or\
				"Regardless of the topic, iGEM projects often create or adapt computational tools to move the project forward." in wikiSource:
				pass
			else:
				linksWithSoftware.append(links[i])
		return linksWithSoftware
		
	##
	#	getData
	# Returns code for the wiki
	##	
		
	def getData(self,year):
		softData = []
		linksWithSoftware = self.getSoftLinks(year)
		counter = 0
		for i in range(0, len(linksWithSoftware), 1):
			softwareWikiSource = requests.get(linksWithSoftware[i]).text
			soup = BeautifulSoup(softwareWikiSource, 'lxml')
			
			for tag in soup():
				for attribute in ['class', 'id', 'name', 'style']:
					del tag[attribute]			
					
			[tag.decompose() for tag in soup("script")]
			[tag.decompose() for tag in soup("style")]
			
			content = soup.find('body')	

			content = self.stripTags(str(content))

			if len(content) > 500:
				softData.append([])
				# Extract team name from links
				linkParts = linksWithSoftware[i].split(':')
				teamName = linkParts[2].split('/')
				try:
					softData[len(softData)-1].append(teamName[0])
				except Exception as e:
					print(e)
					softData[len(softData)-1].append('')
				softData[len(softData)-1].append(content)

		return softData