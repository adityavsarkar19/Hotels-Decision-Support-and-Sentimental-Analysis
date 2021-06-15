# Hotels-Decision-Support-and-Sentimental-Analysis
CS - 2376: Data Mining &amp; Warehousing Mini Project

Contributors:
1. Aditya Sarkar
2. Pritish Dugar
3. Sahil Verma

## Data Mining (Webscraping + API)
The hotel data has been scraped from TripAdvisor using BeautifulSoup4 in the codebase from [this repository](https://github.com/Pro509/webscraper.git).

1. [Bangkok](https://www.tripadvisor.com/Hotels-g293916-Bangkok-Hotels.html)
2. [Singapore](https://www.tripadvisor.com/Hotels-g294265-Singapore-Hotels.html)
3. [Kuala Lumpur](https://www.tripadvisor.com/Hotels-g298570-Kuala_Lumpur_Wilayah_Persekutuan-Hotels.html)

### Geocode Tagging
Using the hotel name and address data available on TripAdvisor, we have forward searched approximate geocodes [Longitude, Latitude] through [Mapbox's API](https://www.mapbox.com/).

### Sentiment Visualization
`pip install -r requirements.txt` before using the mapping notebook (mapbox API key is ***recommended***).
