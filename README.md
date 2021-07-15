# Movie-Recommendor-based-on-Emotion

IMDb offers all the movies for all genre. Therefore the movie titles can be scraped from the IMDb list to recommend to the user.IMDb does not have an API, for accessing information on movies and TV Series. Therefore we have to perform scraping. Scraping is used for accessing information from a website which is usually done with APIs.
Installation

```sh


## Install BeautifulSoup and lxml,
 ## Open terminal and write

pip install beautifulsoup4
pip install lxml

```

The scraper is written in Python and uses lxml for parsing the webpages. BeautifulSoup is used for pulling data out of HTML and XML files.


The correspondence of every emotion with genre of movies is listed below:



Sad – Drama
Disgust – Musical
Anger – Family
Anticipation – Thriller
Fear – Sport
Enjoyment – Thriller
Trust – Western
Surprise – Film-Noir

Based on the input emotion, the corresponding genre would be selected and all the top 5 movies of that genre would be recommended to the user.
