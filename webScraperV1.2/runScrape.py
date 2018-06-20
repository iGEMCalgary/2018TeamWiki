from webScraper import Parser
from intelligentParser import Summarizer
import time

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
	
start = time.time()
	
p = Parser()
teamInfo = p.getData(year)

summarizer = Summarizer()
summary = ''
teamsToRemove = []

for i in range(len(teamInfo)):
	result = summarizer.summarize(teamInfo[i][1])
	
	## Notes: - Original summary accessed by result['MeanDescription'] - or topNDescription
	##			- No error messages - only 'Unable to retrive <team name> software.'
	##			  at teamInfo[i][1]
	if result['Success'] and len(result['MeanDescription']) > 0:
		teamInfo[i][1] = result['MeanDescription']
	else:	
		teamsToRemove.append(i)
	
for i in range(len(teamsToRemove)-1, -1, -1):
	del(teamInfo[teamsToRemove[i]])
	
# for i in range(len(teamInfo)):
	# print(teamInfo[i][0])
	# print(teamInfo[i][1])

# print('Number of teams with software: ' + str(len(teamInfo)))

end = time.time()

# print('Time elapsed: ' + str(end-start))
