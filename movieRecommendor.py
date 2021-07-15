
# Import library for web scrapping
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

# Main Function for scraping
def main(emotion):

	if(emotion == "Sad"):
		urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Disgust"):
		urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Anger"):
		urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Anticipation"):
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Fear"):
		urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Enjoyment"):
		urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

	elif(emotion == "Trust"):
		urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'


	elif(emotion == "Surprise"):
		urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'


	response = HTTP.get(urlhere)
	data = response.text

	# Parsing the data using
	# BeautifulSoup
	soup = SOUP(data, "lxml")

	# Extract movie titles from the
	# data using regex
	title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
	return title


if __name__ == '__main__':

	emotion = input("Enter the emotion: ")
	a = main(emotion)
	count = 0

	if(emotion == "Disgust" or emotion == "Anger"
						or emotion=="Surprise"):

		for i in a:


			tmp = str(i).split('>;')

			if(len(tmp) == 3):
				print(tmp[1][:-3])

			if(count > 13):
				break
			count += 1
	else:
		for i in a:
			tmp = str(i).split('>')

			if(len(tmp) == 3):
				print(tmp[1][:-3])

			if(count > 11):
				break
			count+=1
