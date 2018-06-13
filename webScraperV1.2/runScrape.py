from webScraper import Parser
from intelligentParser import Summarizer


def getYear(prompt=''):
	while True:
		try:
			year = int(input(prompt))
			if(year < 2008 or year > 2017):
				raise Exception
			break
		except Exception:
			print('\nInvalid input. ')
			prompt = 'Please enter a valid year between 2008 and 2017 inclusive: '
	return str(year)
	
year = getYear('Please enter a year: ')
print('\nExtracting iGEM ' + year + ' software...')

p = Parser()
teamInfo = p.getData(year)

summarizer = Summarizer()
summary = ''
teamsWithSoftware = 0

for i in range(len(teamInfo)):
	result = summarizer.summarize(teamInfo[i][1])
	
	## Notes: - Original summary accessed by result['meanDescription']
	##			- No error messages - only 'Unable to retrive <team name> software.'
	##			  at teamInfo[i][1]
	if result['Success'] and len(result['TopNDescription']) > 0:
		teamInfo[i][1] = result['TopNDescription']
		print(teamInfo[i][0])
		print(teamInfo[i][1])
		teamsWithSoftware += 1
	else:	
		teamInfo[i][1] = 'Unable to retrieve ' + teamInfo[i][0] + ' software.'

