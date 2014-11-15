TWILIO REDDIT SCRAPER README
Name: Aansh Kapadia
Date: 10/01/14

	Purpose: 
		the point of this program was to extract the top headline from 		 reddit.com's homepage and then using twilio, call a phone number 		and read back the headline text outloud using twilio's voice command function.

	Scraping Reddit:
		In order to succesfully scrape the top headline from reddit.com I used a python parser called lxml and a python library called BeautifulSoup. The documentation for both of these were good so it was not difficult to learn how to use them. The way I got the top headline from reddit 
		was by looping through the different titles until I found the one with "rank" equal to "1", meaning that it was the top headline (had the most upvotes).

	Twilio:
		After I scraped reddit I passed the string containing the top headline to a function that properly formatted the string into a twimlet URL so that I could succesfully use twilio's voice command feature. Then I used twilio's "client.calls.create" function and passed in 1) the phone number I wanted to call, 2) my twilio phone number, and 3) the message.

	Time: ~2 hours to complete.
